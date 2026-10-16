"""Servidor de prévia local. Somente Python padrão; nenhuma instalação necessária."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import argparse

ROOT = Path(__file__).resolve().parents[1] / "public"


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, base_path="", **kwargs):
        self.base_path = base_path.rstrip("/")
        super().__init__(*args, **kwargs)

    def translate_path(self, path):
        parts = urlsplit(path)
        if self.base_path:
            if parts.path == self.base_path:
                parts = parts._replace(path="/")
            elif parts.path.startswith(self.base_path + "/"):
                parts = parts._replace(path=parts.path[len(self.base_path):])
            else:
                return str(Path(self.directory) / "__outside_preview_mount__")
        return super().translate_path(urlunsplit(parts))

    def list_directory(self, path):
        self.send_error(404)

    def send_error(self, code, message=None, explain=None):
        if code != 404:
            return super().send_error(code, message, explain)
        body = (Path(self.directory) / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=4173)
    parser.add_argument("--directory", type=Path, default=ROOT)
    parser.add_argument("--base-path", default="")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(PreviewHandler, directory=str(args.directory.resolve()), base_path=args.base_path))
    print(f"Prévia: http://127.0.0.1:{args.port}{args.base_path}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
