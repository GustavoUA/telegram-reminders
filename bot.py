
import os
import requests
from datetime import datetime, UTC

print("🚀 Iniciando Hermes...")

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

mensaje = f"""🤖 Hermes

✅ GitHub Actions funcionando correctamente.

Fecha:
{datetime.now(UTC).strftime('%d/%m/%Y %H:%M UTC')}
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

respuesta = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    },
    timeout=30
)

print("Código HTTP:", respuesta.status_code)
print("Respuesta Telegram:", respuesta.text)

respuesta.raise_for_status()

print("✅ Mensaje enviado correctamente.")
