import feedparser


RSS_URL = "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"


def get_news(limit=2):

    try:

        feed = feedparser.parse(RSS_URL)

        if not feed.entries:

            return """
━━━━━━━━━━━━━━━━━━━━━━

📰 *EL PAÍS*

No hay noticias disponibles.

━━━━━━━━━━━━━━━━━━━━━━
"""

        texto = """
━━━━━━━━━━━━━━━━━━━━━━

📰 *EL PAÍS*

"""

        contador = 0

        for noticia in feed.entries:

            titulo = noticia.title.strip()

            texto += f"• {titulo}\n\n"

            contador += 1

            if contador >= limit:
                break

        texto += "━━━━━━━━━━━━━━━━━━━━━━"

        return texto

    except Exception as e:

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

📰 *EL PAÍS*

Error obteniendo noticias.

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""


