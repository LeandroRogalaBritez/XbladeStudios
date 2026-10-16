"""Empacota HTML para Pages, preservando public/ como fonte da prévia local."""
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import re
import shutil
import xml.etree.ElementTree as ET

SOURCE = Path(__file__).resolve().parents[1] / "public"
CSP = "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'self'; form-action 'none'"


def validate_url(base_url):
    url = urlsplit(base_url)
    if (url.scheme != "https" or not url.hostname or url.username or url.password
            or url.query or url.fragment or ".." in unquote(url.path).split("/")):
        raise ValueError("Informe a URL HTTPS pública do Pages, sem credenciais, query ou fragmento.")
    return base_url.rstrip("/"), url.path.rstrip("/")


def page_route(relative):
    route = relative.as_posix()
    return route[:-10] if route.endswith("index.html") else route


def redirects():
    result = {}
    for line in (SOURCE / "_redirects").read_text(encoding="utf-8").splitlines():
        fields = line.split()
        if len(fields) == 3 and fields[2] == "301":
            result[fields[0]] = fields[1]
    return result


def prepare(base_url, output):
    base_url, base_path = validate_url(base_url)
    output = Path(output).resolve()
    source = SOURCE.resolve()
    if output == source or output.is_relative_to(source) or source.is_relative_to(output):
        raise ValueError("A saída deve ficar fora de public/ e não pode conter a pasta de origem.")
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError("Use uma pasta de saída nova ou vazia; nenhum arquivo será apagado.")
    output.mkdir(parents=True, exist_ok=True)
    old_paths = redirects()
    urls = []
    for file in sorted(source.rglob("*")):
        if file.is_symlink():
            raise ValueError(f"Links simbólicos não são aceitos no pacote: {file}")
        if not file.is_file() or file.name in {"_headers", "_redirects", "robots.txt"}:
            continue
        relative = file.relative_to(source)
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if file.suffix != ".html":
            shutil.copyfile(file, target)
            continue
        content = file.read_text(encoding="utf-8")
        route = page_route(relative)
        destination = old_paths.get("/" + route) or old_paths.get("/" + relative.as_posix())
        canonical = base_url + "/" + route
        if destination:
            canonical = base_url + destination
        # Caminhos absolutos continuam corretos mesmo na página 404 em URLs profundas.
        content = re.sub(r'\b(href|src)="/(?!/)([^"]*)"',
                         lambda m: f'{m[1]}="{base_path}/{m[2]}"', content)
        content = re.sub(r'<meta name="robots" content="[^"]*">\s*', "", content)
        content = re.sub(r'<span class="preview-note">.*?</span>', "", content)
        content = re.sub(r'<p class="preview-footer">.*?</p>', "", content)
        content = re.sub(r'<meta property="og:image" content="[^"]*">',
                         f'<meta property="og:image" content="{escape(base_url)}/assets/share.png">', content)
        metadata = [f'<link rel="canonical" href="{escape(canonical)}">',
                    f'<meta property="og:url" content="{escape(canonical)}">',
                    '<meta name="referrer" content="strict-origin-when-cross-origin">',
                    f'<meta http-equiv="Content-Security-Policy" content="{escape(CSP, quote=True)}">']
        if route == "404.html" or destination:
            metadata.append('<meta name="robots" content="noindex, follow">')
        else:
            urls.append(canonical)
        if destination:
            # GitHub Pages não oferece _redirects/301 personalizados.
            metadata.append(f'<meta http-equiv="refresh" content="0; url={escape(base_path + destination)}">')
        content = content.replace("</head>", "\n".join(metadata) + "\n</head>")
        target.write_text(content, encoding="utf-8")
    (output / ".nojekyll").write_text("", encoding="utf-8")
    (output / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap.xml\n", encoding="utf-8")
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    sitemap = ET.Element(f"{{{ns}}}urlset")
    for url in urls:
        ET.SubElement(ET.SubElement(sitemap, f"{{{ns}}}url"), f"{{{ns}}}loc").text = url
    ET.ElementTree(sitemap).write(output / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Site preparado: {base_url}/ -> {output}")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        prepare(args.base_url, args.output)
    except ValueError as error:
        parser.exit(1, f"Erro: {error}\n")
