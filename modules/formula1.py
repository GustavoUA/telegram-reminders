import feedparser

RSS_URL = "https://www.formula1.com/en/latest/all.xml"


def get_formula1(limit=2):

    try:

        feed = feedparser.parse(RSS_URL)

        if not feed.entries:

            return """
━━━━━━━━━━━━━━━━━━━━━━

🏎 *FÓRMULA 1*

No hay noticias disponibles.

━━━━━━━━━━━━━━━━━━━━━━
"""

        texto = """
━━━━━━━━━━━━━━━━━━━━━━

🏎 *FÓRMULA 1*

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

🏎 *FÓRMULA 1*

No ha sido posible obtener las noticias.

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""

