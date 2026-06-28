import requests

from datetime import datetime
from zoneinfo import ZoneInfo

from config import (
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID,
    USER_NAME,
    HERMES_VERSION
)

from modules.weather import get_weather
from modules.cybersecurity import get_cyber_news
from modules.ai import get_ai_news
from modules.tech import get_tech_news
from modules.investment import get_investment_tip
from modules.curiosity import get_curiosity
from modules.training import get_training
from modules.motivation import get_motivation
from modules.security import get_security_tips


# ==========================================
# CONFIGURACIÓN
# ==========================================

TIMEZONE = ZoneInfo("Atlantic/Canary")


# ==========================================
# SALUDO
# ==========================================

def get_greeting():

    hour = datetime.now(TIMEZONE).hour

    if 6 <= hour < 12:
        return "☀️ Buenos días"

    elif 12 <= hour < 15:
        return "🌞 Buen mediodía"

    elif 15 <= hour < 20:
        return "🌤️ Buenas tardes"

    else:
        return "🌙 Buenas noches"


# ==========================================
# ENVÍO TELEGRAM
# ==========================================

def send_telegram(text):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "disable_web_page_preview": True
        },
        timeout=30
    ).raise_for_status()


# ==========================================
# MENSAJE
# ==========================================

def build_message():

    now = datetime.now(TIMEZONE)

    fecha = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M")

    message = f"""
🤖 {HERMES_VERSION}

{get_greeting()}, {USER_NAME}

📅 {fecha}
🕒 {hora}

━━━━━━━━━━━━━━━━━━━━
"""

    sections = [

        get_weather(),

        get_cyber_news(),

        get_security_tip(),

        get_ai_news(),

        get_tech_news(),

        get_investment_tips(),

        get_curiosity(),

        get_training(),

        get_motivation()

    ]

    message += "\n━━━━━━━━━━━━━━━━━━━━\n\n".join(sections)

    message += """

━━━━━━━━━━━━━━━━━━━━

🚀 ¡Que tengas un gran día!
"""

    return message.strip()


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    try:

        mensaje = build_message()

        send_telegram(mensaje)

        print("✅ Hermes ejecutado correctamente.")

    except Exception as e:

        print("❌ Error:", e)

        raise
