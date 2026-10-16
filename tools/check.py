"""Validação estática: rotas, âncoras, assets e metadados. Não usa dependências."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1] / "public"


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links, self.ids, self.metas = [], set(), {}
        self.h1, self.lang, self.title = 0, None, False
        self.errors = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                self.errors.append(f"ID duplicado: {a['id']}")
            self.ids.add(a["id"])
        if tag == "h1": self.h1 += 1
        if tag == "html": self.lang = a.get("lang")
        if tag == "title": self.title = True
        if tag == "meta": self.metas[a.get("name", a.get("property"))] = a.get("content")
        if tag == "img" and "alt" not in a: self.errors.append("Imagem sem alt")
        for key in ("href", "src"):
            if key in a: self.links.append(a[key])


def check(root=ROOT, base_path="", production=False):
    root = Path(root).resolve()
    base_path = base_path.rstrip("/")
    docs = {p: Document(p.read_text(encoding="utf-8")) for p in root.rglob("*.html")}
    errors, external = [], set()
    if not docs:
        errors.append("Nenhuma página HTML encontrada.")
    for path, doc in docs.items():
        label = str(path.relative_to(root))
        errors.extend(f"{label}: {e}" for e in doc.errors)
        if doc.h1 != 1: errors.append(f"{label}: esperado um h1")
        if doc.lang != "pt-BR": errors.append(f"{label}: idioma incorreto")
        if not doc.title or not doc.metas.get("description"): errors.append(f"{label}: metadados ausentes")
        if not production and "noindex" not in doc.metas.get("robots", ""): errors.append(f"{label}: prévia sem noindex")
        if production and path.name != "404.html" and not doc.metas.get("og:url"):
            errors.append(f"{label}: endereço de compartilhamento ausente")
        for href in doc.links:
            u = urlsplit(href)
            if u.scheme in ("http", "https"):
                external.add(href)
                continue
            if u.scheme == "mailto": continue
            if u.scheme or u.netloc:
                errors.append(f"{label}: esquema inesperado: {href}")
                continue
            url_path = unquote(u.path)
            if url_path.startswith("/"):
                if base_path and not url_path.startswith(base_path + "/"):
                    errors.append(f"{label}: link sai do caminho do projeto: {href}")
                    continue
                target = root / url_path[len(base_path):].lstrip("/")
            else:
                target = path.parent / url_path
            if not u.path: target = path
            if target.is_dir(): target /= "index.html"
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"{label}: link fora da pasta do site: {href}")
                continue
            if not target.is_file():
                errors.append(f"{label}: destino inexistente: {href}")
            elif u.fragment and target in docs and unquote(u.fragment) not in docs[target].ids:
                errors.append(f"{label}: âncora inexistente: {href}")
    for url in sorted(external): print(f"EXTERNO (revisão independente): {url}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: {len(docs)} páginas; links internos, âncoras, imagens e metadados verificados.")
    print("Pacote de publicação verificado." if production else "Prévia com noindex; app-ads.txt aguarda as linhas reais.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--base-path", default="")
    parser.add_argument("--production", action="store_true")
    args = parser.parse_args()
    sys.exit(check(args.root, args.base_path, args.production))
