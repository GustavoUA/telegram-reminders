import feedparser
from config import CYBER_RSS


def get_cyber_news():
    """
    Obtiene la última noticia de ciberseguridad en español.
    """

    for rss in CYBER_RSS:
        try:
            feed = feedparser.parse(rss)

            if not feed.entries:
                continue

            noticia = feed.entries[0]

            titulo = noticia.title
            enlace = noticia.link

            resumen = ""

            if hasattr(noticia, "summary"):
                resumen = noticia.summary

                # Eliminar etiquetas HTML sencillas
                resumen = (
                    resumen.replace("<p>", "")
                           .replace("</p>", "")
                           .replace("<br>", "")
                           .replace("<br/>", "")
                )

                resumen = resumen[:220]

            texto = f"""🛡️ Ciberseguridad

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

    return """🛡️ Ciberseguridad

No ha sido posible obtener noticias hoy.
"""