import feedparser
from bs4 import BeautifulSoup

from config import MOTOGP_RSS
from modules.translator import translate


def clean_html(html):

    return BeautifulSoup(
        html,
        "html.parser"
    ).get_text(" ", strip=True)


def get_motogp_news():

    for rss in MOTOGP_RSS:

        try:

            feed = feedparser.parse(rss)

            if not feed.entries:
                continue

            noticia = feed.entries[0]

            titulo = translate(noticia.title)

            enlace = noticia.link

            resumen = ""

            if hasattr(noticia, "summary"):

                resumen = clean_html(
                    noticia.summary
                )

                resumen = translate(resumen)

                resumen = resumen[:300]

            texto = f"""🏍️ MotoGP

📰 {titulo}
"""

            if resumen:

                texto += f"""

📌 Resumen

{resumen}
"""

            texto += f"""

🔗 {enlace}
"""

            return texto

        except Exception:

            continue

    return """🏍️ MotoGP

No hay noticias disponibles.
"""
