import feedparser
from bs4 import BeautifulSoup
from config import TECH_RSS


def get_tech():

    for rss in TECH_RSS:

        try:

            feed = feedparser.parse(rss)

            if not feed.entries:
                continue

            noticia = feed.entries[0]

            titulo = noticia.title

            enlace = noticia.link

            resumen = ""

            if hasattr(noticia, "summary"):

                resumen = BeautifulSoup(
                    noticia.summary,
                    "html.parser"
                ).get_text(separator=" ", strip=True)

                resumen = resumen.replace("\n", " ")

                resumen = " ".join(resumen.split())

                resumen = resumen[:250]

            texto = f"""💻 Tecnología

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

    return """💻 Tecnología

No se pudo obtener la noticia tecnológica.
"""
