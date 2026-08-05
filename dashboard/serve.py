"""
Local dashboard server with auto-rebuild.

    python serve.py ["path\\to\\your-novel"] [port]

Watches the workspace for markdown changes and rebuilds data.json.
Read-only: never writes to the workspace.
"""
import os, sys, time, json, threading, http.server, socketserver, functools, io, webbrowser
import build as B

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(HERE, "static")
WATCH_DIRS = ["manuscript", "characters", "places", "factions", "world", "plot", "canon", "story"]
POLL = 1.5


def snapshot(root):
    sig = {}
    for d in WATCH_DIRS:
        base = os.path.join(root, d)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, files in os.walk(base):
            dirnames[:] = [x for x in dirnames if x not in ("images", ".git")]
            for f in files:
                if f.endswith(".md"):
                    p = os.path.join(dirpath, f)
                    try:
                        sig[p] = os.path.getmtime(p)
                    except OSError:
                        pass
    return sig


def rebuild(root, quiet=False):
    data = B.build(root)
    os.makedirs(STATIC, exist_ok=True)
    tmp = os.path.join(STATIC, "data.json.tmp")
    io.open(tmp, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False))
    os.replace(tmp, os.path.join(STATIC, "data.json"))
    if not quiet:
        s = data["stats"]
        print(f"  rebuilt - {s['words']:,} words, {s['scenes']} scenes, "
              f"{s['characters']}c {s['places']}p {s['factions']}f", flush=True)
    return data


def watch(root):
    last = snapshot(root)
    while True:
        time.sleep(POLL)
        try:
            now = snapshot(root)
            if now != last:
                changed = len(set(now.items()) ^ set(last.items()))
                last = now
                print(f"\n  {changed} file(s) changed", flush=True)
                rebuild(root)
        except Exception as e:
            print(f"  watch error: {e}", flush=True)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


def local_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = args[0] if args else r"path\to\your-novel"
    port = int(args[1]) if len(args) > 1 else 8778
    # --lan exposes the dashboard to other devices on your network (phone, tablet).
    # Off by default: it makes the manuscript readable by anyone on the same wifi.
    host = "0.0.0.0" if "--lan" in sys.argv else "127.0.0.1"
    if not os.path.isdir(root):
        sys.exit(f"workspace not found: {root}")

    print(f"\n  workspace : {root}")
    rebuild(root)

    threading.Thread(target=watch, args=(root,), daemon=True).start()

    handler = functools.partial(Handler, directory=STATIC)
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    url = f"http://localhost:{port}"
    with socketserver.ThreadingTCPServer((host, port), handler) as srv:
        srv.daemon_threads = True
        print(f"  dashboard : {url}")
        if host == "0.0.0.0":
            print(f"  on wifi   : http://{local_ip()}:{port}   <- phone/tablet")
            print("              anyone on this network can read the manuscript")
        print(f"  watching  : {', '.join(WATCH_DIRS)}")
        print("  ctrl-c to stop\n", flush=True)

        # Opening a browser can block when there is no desktop session
        # (background jobs, services), which would stop the server ever
        # starting. Off-thread, and only when asked.
        if "--open" in sys.argv:
            threading.Thread(target=lambda: webbrowser.open(url), daemon=True).start()

        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\n  stopped\n")


if __name__ == "__main__":
    main()
