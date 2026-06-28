import requests
from datetime import datetime

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
from modules.motivation import get_motivation
from modules.training import get_training


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


def build_message():

    today = datetime.now().strftime("%d/%m/%Y")

    message = f"""
🤖 {HERMES_VERSION}

¡Buenos días, {USER_NAME}! ☀️

📅 {today}

━━━━━━━━━━━━━━━━━━━━

"""

    sections = [
        get_weather(),
        get_cyber_news(),
        get_ai_news(),
        get_tech_news(),
        get_investment_tip(),
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


if __name__ == "__main__":

    try:

        mensaje = build_message()

        send_telegram(mensaje)

        print("✅ Hermes ejecutado correctamente.")

    except Exception as e:

        print("❌ Error:", e)

        raise
