import os
import requests
from datetime import datetime

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

mensaje = f"""🤖 Hermes

✅ GitHub Actions funcionando correctamente.

Fecha:
{datetime.utcnow().strftime('%d/%m/%Y %H:%M UTC')}
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": mensaje
})
