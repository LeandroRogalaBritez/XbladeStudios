"""Validação estática: rotas, âncoras, assets e metadados. Não usa dependências."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
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


def check():
    docs = {p: Document(p.read_text(encoding="utf-8")) for p in ROOT.rglob("*.html")}
    errors, external = [], set()
    for path, doc in docs.items():
        label = str(path.relative_to(ROOT))
        errors.extend(f"{label}: {e}" for e in doc.errors)
        if doc.h1 != 1: errors.append(f"{label}: esperado um h1")
        if doc.lang != "pt-BR": errors.append(f"{label}: idioma incorreto")
        if not doc.title or not doc.metas.get("description"): errors.append(f"{label}: metadados ausentes")
        if "noindex" not in doc.metas.get("robots", ""): errors.append(f"{label}: prévia sem noindex")
        for href in doc.links:
            u = urlsplit(href)
            if u.scheme in ("http", "https"):
                external.add(href)
                continue
            if u.scheme == "mailto": continue
            if u.scheme or u.netloc:
                errors.append(f"{label}: esquema inesperado: {href}")
                continue
            target = (ROOT / unquote(u.path.lstrip("/"))) if u.path.startswith("/") else (path.parent / unquote(u.path))
            if not u.path: target = path
            if target.is_dir(): target /= "index.html"
            if not target.is_file():
                errors.append(f"{label}: destino inexistente: {href}")
            elif u.fragment and target in docs and unquote(u.fragment) not in docs[target].ids:
                errors.append(f"{label}: âncora inexistente: {href}")
    for url in sorted(external): print(f"EXTERNO (revisão independente): {url}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: {len(docs)} páginas; links internos, âncoras, imagens e metadados verificados.")
    print("Prévia com noindex; robots permite políticas e assets; app-ads.txt aguarda as linhas reais.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
