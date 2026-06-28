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
# HERMES
# ==========================================

HERMES_VERSION = "Hermes v1.1"

TIMEZONE = "Atlantic/Canary"

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
# RSS CIBERSEGURIDAD
# ==========================================

CYBER_RSS = [

    "https://www.welivesecurity.com/es/feed/",

    "https://cybersecuritynews.es/feed/",

    "https://unaaldia.hispasec.com/feed/"

]

# ==========================================
# RSS IA
# ==========================================

AI_RSS = [

    "https://openai.com/news/rss.xml",

    "https://huggingface.co/blog/feed.xml",

    "https://www.anthropic.com/news/rss.xml"

]

# ==========================================
# RSS TECNOLOGÍA
# ==========================================

TECH_RSS = [

    "https://www.xataka.com/feedburner.xml",

    "https://www.genbeta.com/feedburner.xml",

    "https://www.muylinux.com/feed/"

]

# ==========================================
# ACTIVOS DE INVERSIÓN
# ==========================================

INVESTMENTS = [

    "BTC-USD",

    "GC=F",          # Oro

    "SI=F",          # Plata

    "MSFT",

    "NVDA",

    "AAPL",

    "AMZN",

    "GOOGL",

    "META",

    "SPY",           # S&P500 ETF

    "VWCE.DE"        # Vanguard FTSE All World

]

# ==========================================
# HORARIO
# ==========================================

MORNING_HOUR = "08:00"

# ==========================================
# HISTORIAL
# ==========================================

HISTORY_FOLDER = "history"

# ==========================================
# DATA
# ==========================================

QUOTES_FILE = "data/quotes.txt"

CURIOSITIES_FILE = "data/curiosities.txt"

SECURITY_FILE = "data/security_tips.txt"

INVESTMENT_FILE = "data/investment.json"
