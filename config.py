import os

# ==========================================
# TELEGRAM
# ==========================================

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# ==========================================
# USUARIO
# ==========================================

USER_NAME = "Gustavo"

# ==========================================
# CIUDADES
# ==========================================

CITIES = {
    "San Cristóbal de La Laguna": {
        "lat": 28.4874,
        "lon": -16.3159
    },
    "Puerto de la Cruz": {
        "lat": 28.4134,
        "lon": -16.5487
    }
}

# ==========================================
# FUENTES RSS
# ==========================================

CYBER_RSS = [
    "https://www.welivesecurity.com/es/feed/",
    "https://cybersecuritynews.es/feed/"
]

AI_RSS = [
    "https://openai.com/news/rss.xml"
]

TECH_RSS = [
    "https://www.xataka.com/feedburner.xml"
]

# ==========================================
# ACTIVOS DE INVERSIÓN
# ==========================================

INVESTMENTS = [
    "BTC-USD",
    "GC=F",      # Oro
    "MSFT",
    "NVDA",
    "AAPL",
    "AMZN",
    "GOOGL",
    "META"
]

# ==========================================
# FRASES MOTIVADORAS
# ==========================================

QUOTES = [
    "Cada pequeño paso te acerca a tu objetivo.",
    "La disciplina vence a la motivación.",
    "Haz hoy lo que otros no quieren para vivir mañana como otros no pueden.",
    "Nunca es tarde para empezar.",
    "La constancia supera al talento cuando el talento no trabaja.",
    "No cuentes los días. Haz que los días cuenten.",
    "No esperes el momento perfecto. Haz perfecto el momento.",
    "El éxito es la suma de pequeños esfuerzos repetidos cada día.",
    "No importa lo lento que avances mientras no te detengas.",
    "El futuro depende de lo que hagas hoy.",
    "Cada entrenamiento cuenta.",
    "Tu único rival eres tú mismo.",
    "Si fuera fácil, todo el mundo lo haría.",
    "Hazlo con miedo, pero hazlo.",
    "Nunca subestimes el poder de la constancia."
]

# ==========================================
# HORARIO HERMES
# ==========================================

MORNING_HOUR = "08:00"

# ==========================================
# VERSION
# ==========================================

HERMES_VERSION = "Hermes Lite v1.0"