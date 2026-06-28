
import feedparser
from config import TECH_RSS


def clean_html(text):
    """Elimina etiquetas HTML sencillas."""

    replacements = [
        ("<p>", ""),
        ("</p>", ""),
        ("<br>", ""),
        ("<br/>", ""),
        ("<br />", ""),
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    return text


def get_tech_news():
    """
    Obtiene la noticia tecnológica más reciente.
    """

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
                resumen = clean_html(noticia.summary)
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

No ha sido posible obtener noticias tecnológicas hoy.
"""
