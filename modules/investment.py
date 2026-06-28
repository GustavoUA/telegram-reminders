import random
import yfinance as yf
from config import INVESTMENTS


DESCRIPTIONS = {
    "BTC-USD": {
        "name": "Bitcoin",
        "emoji": "₿",
        "reason": "Principal criptomoneda del mercado. Ideal para seguir el sentimiento del mercado cripto."
    },
    "GC=F": {
        "name": "Oro",
        "emoji": "🥇",
        "reason": "Activo refugio utilizado cuando aumenta la incertidumbre económica."
    },
    "MSFT": {
        "name": "Microsoft",
        "emoji": "💻",
        "reason": "Líder en software, cloud e inteligencia artificial."
    },
    "NVDA": {
        "name": "NVIDIA",
        "emoji": "🤖",
        "reason": "Empresa líder en chips para Inteligencia Artificial."
    },
    "AAPL": {
        "name": "Apple",
        "emoji": "🍎",
        "reason": "Una de las compañías tecnológicas más sólidas del mundo."
    },
    "AMZN": {
        "name": "Amazon",
        "emoji": "📦",
        "reason": "Gigante del comercio electrónico y líder en servicios cloud."
    },
    "GOOGL": {
        "name": "Alphabet",
        "emoji": "🌐",
        "reason": "Google continúa siendo una referencia en IA, publicidad y búsqueda."
    },
    "META": {
        "name": "Meta",
        "emoji": "📱",
        "reason": "Importante apuesta por la Inteligencia Artificial y las redes sociales."
    }
}


def get_investment_tip():

    try:

        ticker = random.choice(INVESTMENTS)

        stock = yf.Ticker(ticker)

        info = stock.fast_info

        price = info.get("lastPrice")

        previous = info.get("previousClose")

        if price is None or previous is None:
            raise Exception()

        variation = ((price - previous) / previous) * 100

        data = DESCRIPTIONS.get(ticker)

        arrow = "📈" if variation >= 0 else "📉"

        return f"""💰 Radar de inversión

{data['emoji']} {data['name']}

💵 Precio
{price:.2f}

{arrow} Variación
{variation:+.2f} %

📌 Motivo

{data['reason']}

⚠️ Información orientativa. No constituye asesoramiento financiero.
"""

    except Exception:

        return """💰 Radar de inversión

Hoy no ha sido posible obtener información del mercado.
"""