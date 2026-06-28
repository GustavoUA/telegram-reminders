import feedparser
import random
from config import AI_RSS


def get_ai_news():
    """
    Devuelve una noticia aleatoria de IA obtenida desde las fuentes RSS.
    """

    try:
        feed_url = random.choice(AI_RSS)
        feed = feedparser.parse(feed_url)

        if not feed.entries:
            return (
                "🤖 IA\n\n"
                "No se encontraron noticias disponibles.\n"
            )

        noticia = feed.entries[0]

        titulo = noticia.title
        enlace = noticia.link

        return f"""🤖 IA

📰 {titulo}

🔗 {enlace}
"""

    except Exception:
        return (
            "🤖 IA\n\n"
            "No se pudo obtener la noticia de IA.\n"
        )