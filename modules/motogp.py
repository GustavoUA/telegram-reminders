import feedparser


# ============================================================
# RSS MOTOGP
# ============================================================

RSS_FEEDS = [

    "https://es.motorsport.com/rss/motogp/news/",

]


# ============================================================
# CONFIGURACIÓN
# ============================================================

MAX_NEWS = 3

TITLE = "🏍 *MOTOGP*"

# ============================================================
# LIMPIAR TÍTULOS
# ============================================================

def clean_title(title):

    title = title.replace("\n", " ")

    title = " ".join(title.split())

    return title.strip()

# ============================================================
# OBTENER NOTICIAS
# ============================================================

def get_motogp():

    noticias = []

    for rss in RSS_FEEDS:

        try:

            feed = feedparser.parse(rss)

            if not feed.entries:
                continue

            for entry in feed.entries[:MAX_NEWS]:

                titulo = clean_title(entry.title)

                noticias.append(f"• {titulo}")

            if noticias:
                break

        except Exception:
            continue

    if not noticias:

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

{TITLE}

No hay noticias disponibles.

━━━━━━━━━━━━━━━━━━━━━━
"""

    mensaje = f"""
━━━━━━━━━━━━━━━━━━━━━━

{TITLE}

"""

    mensaje += "\n\n".join(noticias)


    mensaje += """

━━━━━━━━━━━━━━━━━━━━━━
"""

    return mensaje

