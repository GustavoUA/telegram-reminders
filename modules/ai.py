import feedparser
from bs4 import BeautifulSoup

from config import AI_RSS
from modules.translator import translate


def clean_html(html):
    """
    Elimina etiquetas HTML y espacios innecesarios.
    """

    text = BeautifulSoup(
        html,
        "html.parser"
    ).get_text(" ", strip=True)

    text = " ".join(text.split())

    return text


def get_ai():
    """
    Obtiene la noticia más reciente de IA.
    Si una fuente falla, prueba la siguiente.
    """

    for rss in AI_RSS:

        try:

            feed = feedparser.parse(rss)

            if not feed.entries:
                continue

            noticia = feed.entries[0]

            titulo = translate(noticia.title)

            enlace = noticia.link

            resumen = ""

            if hasattr(noticia, "summary"):

                resumen = clean_html(noticia.summary)

                resumen = translate(resumen)

                if len(resumen) > 350:
                    resumen = resumen[:350] + "..."

            texto = f"""🤖 Inteligencia Artificial

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

    return """🤖 Inteligencia Artificial

No ha sido posible obtener noticias de IA hoy.
"""
