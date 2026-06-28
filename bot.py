import random
import locale
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
from modules.security import get_security_tip
from modules.ai import get_ai_news
from modules.tech import get_tech_news
from modules.investment import get_investment_tips
from modules.curiosity import get_curiosity
from modules.training import get_training
from modules.motivation import get_motivation


# ==================================================
# CONFIGURACIÓN
# ==================================================

TIMEZONE = ZoneInfo("Atlantic/Canary")

try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
except:
    pass


# ==================================================
# SALUDOS
# ==================================================

MORNING = [
    f"☀️ Buenos días, {USER_NAME}.",
    f"🌅 ¡Buenos días, {USER_NAME}!",
    f"☕ Buenos días, {USER_NAME}. Aquí tienes tu briefing diario.",
    f"🌞 Buenos días, {USER_NAME}. Espero que tengas un gran día."
]

AFTERNOON = [
    f"🌤️ Buenas tardes, {USER_NAME}.",
    f"☀️ Buenas tardes, {USER_NAME}.",
    f"🌞 Espero que estés teniendo una buena tarde, {USER_NAME}.",
    f"☕ Buenas tardes. Aquí tienes las novedades del día."
]

NIGHT = [
    f"🌙 Buenas noches, {USER_NAME}.",
    f"⭐ Buenas noches, {USER_NAME}.",
    f"🌌 Espero que hayas tenido un gran día.",
    f"🌙 Buenas noches. Aquí tienes el resumen del día."
]


def get_greeting():

    hour = datetime.now(TIMEZONE).hour

    if 6 <= hour < 12:
        return random.choice(MORNING)

    elif 12 <= hour < 20:
        return random.choice(AFTERNOON)

    else:
        return random.choice(NIGHT)


# ==================================================
# TELEGRAM
# ==================================================

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


# ==================================================
# MENSAJE
# ==================================================

def build_message():

    now = datetime.now(TIMEZONE)

    try:
        fecha = now.strftime("%A, %d de %B de %Y").capitalize()
    except:
        fecha = now.strftime("%d/%m/%Y")

    hora = now.strftime("%H:%M")

    message = f"""
╔══════════════════════════════╗
            🤖 HERMES
╚══════════════════════════════╝

{get_greeting()}

📅 {fecha}
🕒 {hora} (Canarias)

━━━━━━━━━━━━━━━━━━━━━━
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

    message += "\n━━━━━━━━━━━━━━━━━━━━━━\n\n".join(sections)

    message += f"""

━━━━━━━━━━━━━━━━━━━━━━

🤖 {HERMES_VERSION}

Powered by Python + GitHub Actions

🚀 ¡Que tengas un gran día!
"""

    return message.strip()


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    try:

        mensaje = build_message()

        send_telegram(mensaje)

        print("✅ Hermes ejecutado correctamente.")

    except Exception as e:

        print("❌ Error:", e)

        raise
