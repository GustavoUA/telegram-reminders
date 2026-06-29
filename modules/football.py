import feedparser

RSS_URL = "https://www.marca.com/rss/futbol.xml"


def get_football(limit=2):

    try:

        feed = feedparser.parse(RSS_URL)

        if not feed.entries:

            return """
━━━━━━━━━━━━━━━━━━━━━━

⚽ *FÚTBOL*

No hay noticias disponibles.

━━━━━━━━━━━━━━━━━━━━━━
"""

        texto = """
━━━━━━━━━━━━━━━━━━━━━━

⚽ *FÚTBOL*

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

⚽ *FÚTBOL*

No ha sido posible obtener las noticias.

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""

