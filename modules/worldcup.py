import feedparser
from deep_translator import GoogleTranslator


# ============================================================
# RSS MUNDIAL
# ============================================================

RSS_FEEDS = [

    "https://www.fifa.com/rss-feeds/news",

    "https://feeds.bbci.co.uk/sport/football/rss.xml"

]

MAX_NEWS = 5


# ============================================================
# TRADUCTOR
# ============================================================

def translate(text):

    try:

        return GoogleTranslator(

            source="auto",

            target="es"

        ).translate(text)

    except Exception:

        return text


# ============================================================
# LIMPIAR TEXTO
# ============================================================

def clean(text):

    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text.strip()


# ============================================================
# OBTENER INFORMACIÓN DEL MUNDIAL
# ============================================================

def get_worldcup():

    try:

        noticias = []

        for rss in RSS_FEEDS:

            feed = feedparser.parse(rss)

            if not feed.entries:

                continue

            for entry in feed.entries:

                titulo = clean(entry.title)

                titulo_es = translate(titulo)

                texto = titulo_es.lower()

                # Solo noticias relacionadas con el Mundial
                if (
                    "mundial" in texto or
                    "world cup" in texto or
                    "fifa" in texto or
                    "copa del mundo" in texto or
                    "2026" in texto
                ):

                    noticias.append(f"• {titulo_es}")

                if len(noticias) >= MAX_NEWS:

                    break

            if noticias:

                break

        if not noticias:

            return """
━━━━━━━━━━━━━━━━━━━━━━

🏆 *MUNDIAL 2026*

No hay noticias disponibles.

━━━━━━━━━━━━━━━━━━━━━━
"""

        texto = f"""
━━━━━━━━━━━━━━━━━━━━━━

🏆 *MUNDIAL 2026*

📰 *DESTACADO DEL DÍA*

"""

        texto += "\n".join(noticias)

        texto += """

━━━━━━━━━━━━━━━━━━━━━━
"""

        return texto

    except Exception as e:

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

🏆 *MUNDIAL 2026*

No ha sido posible obtener la información.

Error:

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""


# ============================================================
# PRUEBA
# ============================================================

if __name__ == "__main__":

    print(get_worldcup())
