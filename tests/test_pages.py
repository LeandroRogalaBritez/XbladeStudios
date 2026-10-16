"""Regressões reais de publicação: subdiretórios, 404, metadados e conteúdo exportado."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import shutil
import unittest
from uuid import uuid4
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check import check
from prepare_pages import prepare, validate_url, SOURCE
from locales import PAGE_PAIRS, route
from html.parser import HTMLParser


class PagesTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).resolve().parents[1] / "artifacts" / "tests"
        temp_root.mkdir(parents=True, exist_ok=True)
        temporary = (temp_root / uuid4().hex).resolve()
        self.assertTrue(temporary.is_relative_to(temp_root.resolve()))
        temporary.mkdir()
        self.addCleanup(shutil.rmtree, temporary)
        self.output = temporary / "site"

    def publish(self, url):
        with redirect_stdout(StringIO()):
            return prepare(url, self.output)

    def test_project_url_links_and_deep_404(self):
        self.publish("https://example.github.io/Studio")
        with redirect_stdout(StringIO()) as result:
            code = check(self.output, "/Studio", production=True)
        self.assertEqual(code, 0, result.getvalue())
        error = (self.output / "404.html").read_text(encoding="utf-8")
        self.assertIn('href="/Studio/"', error)
        self.assertIn('href="/Studio/assets/style.css', error)
        self.assertNotIn('href="/assets/', error)

    def test_domain_root_is_supported(self):
        self.publish("https://studio.example/")
        with redirect_stdout(StringIO()) as result:
            code = check(self.output, production=True)
        self.assertEqual(code, 0, result.getvalue())
        html = (self.output / "index.html").read_text(encoding="utf-8")
        self.assertIn('content="https://studio.example/assets/share.png"', html)
        self.assertIn('rel="canonical" href="https://studio.example/"', html)

    def test_only_site_is_published_and_indexing_is_ready(self):
        self.publish("https://example.github.io/Studio")
        for excluded in ("README.md", "docs", "tools", "tests", "_headers", "_redirects"):
            self.assertFalse((self.output / excluded).exists(), excluded)
        self.assertTrue((self.output / ".nojekyll").exists())
        for path in self.output.rglob("*.html"):
            html = path.read_text(encoding="utf-8")
            self.assertNotIn('class="preview-note"', html)
            self.assertNotIn('class="preview-footer"', html)
        privacy = (self.output / "privacidade/index.html").read_text(encoding="utf-8")
        self.assertNotIn('noindex', privacy)
        self.assertIn('https://example.github.io/Studio/privacidade/', privacy)
        tree = ET.parse(self.output / "sitemap.xml")
        locations = [e.text for e in tree.findall(".//{*}loc")]
        self.assertIn("https://example.github.io/Studio/privacidade/", locations)
        self.assertFalse(any("404" in url or "purr-box" in url for url in locations))

    def test_old_privacy_addresses_keep_working(self):
        self.publish("https://example.github.io/Studio")
        for slug in ("purr-box", "normal-dev-guy"):
            html = (self.output / f"privacidade/{slug}/index.html").read_text(encoding="utf-8")
            self.assertIn('http-equiv="refresh" content="0; url=/Studio/privacidade/"', html)
            self.assertIn('href="/Studio/privacidade/"', html)

    def test_translations_keep_the_same_page_and_publish_absolute_alternates(self):
        self.publish("https://example.github.io/Studio")
        class Links(HTMLParser):
            def __init__(self, html):
                super().__init__()
                self.languages, self.alternates = {}, {}
                self.feed(html)

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == "a" and "hreflang" in attrs:
                    self.languages[attrs["hreflang"]] = attrs["href"]
                if tag == "link" and attrs.get("rel") == "alternate":
                    self.alternates[attrs["hreflang"]] = attrs["href"]

        for portuguese, english in PAGE_PAIRS.items():
            for filename, lang in ((portuguese, "pt-BR"), (english, "en")):
                with self.subTest(page=filename):
                    html = (self.output / filename).read_text(encoding="utf-8")
                    self.assertIn(f'<html lang="{lang}">', html)
                    links = Links(html)
                    for language, translated in (("pt-BR", portuguese), ("en", english)):
                        self.assertEqual(links.languages[language], "/Studio" + route(translated))
                        self.assertEqual(links.alternates[language], "https://example.github.io/Studio" + route(translated))
        error = (self.output / "en/404.html").read_text(encoding="utf-8")
        self.assertIn('href="/Studio/en/"', error)
        self.assertIn('content="noindex, follow"', error)
        old = (self.output / "en/privacy/purr-box/index.html").read_text(encoding="utf-8")
        self.assertIn('http-equiv="refresh" content="0; url=/Studio/en/privacy/"', old)

    def test_checker_rejects_a_missing_translation_or_wrong_language(self):
        self.publish("https://example.github.io/Studio")
        page = self.output / "en/privacy/index.html"
        page.write_text(page.read_text(encoding="utf-8").replace('lang="en"', 'lang="pt-BR"'), encoding="utf-8")
        with redirect_stdout(StringIO()) as result:
            self.assertEqual(check(self.output, "/Studio", production=True), 1)
        self.assertIn("idioma incorreto", result.getvalue())
        page.unlink()
        with redirect_stdout(StringIO()) as result:
            self.assertEqual(check(self.output, "/Studio", production=True), 1)
        self.assertIn("Tradução ausente", result.getvalue())

    def test_does_not_overwrite_sources_or_existing_files(self):
        with self.assertRaises(ValueError):
            prepare("https://studio.example", SOURCE / "output")
        self.output.mkdir()
        sentinel = self.output / "keep.txt"
        sentinel.write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            prepare("https://studio.example", self.output)
        self.assertEqual(sentinel.read_text(), "keep")

    def test_rejects_invalid_deployment_urls(self):
        for url in ("http://studio.example", "https://user:pass@studio.example", "https://studio.example/../secret", "https://studio.example/?x=1"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_url(url)


if __name__ == "__main__":
    unittest.main()
