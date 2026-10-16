"""Páginas equivalentes. Caminhos de origem sem o prefixo do GitHub Pages."""

PAGE_PAIRS = {
    "index.html": "en/index.html",
    "jogos/index.html": "en/games/index.html",
    "suporte/index.html": "en/support/index.html",
    "privacidade/index.html": "en/privacy/index.html",
    "termos/index.html": "en/terms/index.html",
    "exclusao-de-dados/index.html": "en/data-deletion/index.html",
    "privacidade/admob/index.html": "en/privacy/ads/index.html",
    "privacidade/site/index.html": "en/privacy/site/index.html",
    "privacidade/purr-box/index.html": "en/privacy/purr-box/index.html",
    "privacidade/normal-dev-guy/index.html": "en/privacy/normal-dev-guy/index.html",
    "404.html": "en/404.html",
}


def route(filename):
    return "/" + (filename[:-10] if filename.endswith("index.html") else filename)


def translations(filename):
    for portuguese, english in PAGE_PAIRS.items():
        if filename in (portuguese, english):
            return {"pt-BR": route(portuguese), "en": route(english)}
    return {}
