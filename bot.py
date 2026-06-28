import os
import random
from datetime import datetime
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Coordenadas
CIUDADES = {
    "San Cristóbal de La Laguna": (28.4874, -16.3159),
    "Puerto de la Cruz": (28.4134, -16.5487)
}

FRASES = [
    "Cada pequeño paso te acerca a tu objetivo.",
    "La disciplina vence a la motivación.",
    "Hoy es un buen día para mejorar un 1%.",
    "El éxito es la suma de pequeños esfuerzos diarios.",
    "No te rindas. Todo esfuerzo tiene recompensa.",
    "Haz hoy lo que tu yo del futuro agradecerá.",
    "Nunca es tarde para empezar.",
    "La constancia siempre supera al talento.",
    "Cada entrenamiento cuenta.",
    "Cree en ti. Ya has superado cosas más difíciles."
]

CODIGOS = {
    0: "☀️ Despejado",
    1: "🌤️ Poco nuboso",
    2: "⛅ Parcialmente nublado",
    3: "☁️ Nublado",
    45: "🌫️ Niebla",
    48: "🌫️ Niebla",
    51: "🌦️ Llovizna",
    61: "🌧️ Lluvia",
    63: "🌧️ Lluvia",
    65: "🌧️ Lluvia fuerte",
    71: "❄️ Nieve",
    80: "🌦️ Chubascos",
    95: "⛈️ Tormenta"
}


def obtener_tiempo(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
    )

    r = requests.get(url, timeout=15)
    datos = r.json()["current"]

    temp = round(datos["temperature_2m"])
    codigo = datos["weather_code"]

    estado = CODIGOS.get(codigo, "🌍 Sin datos")

    return f"{temp}°C | {estado}"


mensaje = f"""🤖 Buenos días Gustavo ☀️

📅 {datetime.now().strftime("%d/%m/%Y")}

🌤️ Tiempo

"""

for ciudad, coord in CIUDADES.items():
    mensaje += f"📍 {ciudad}\n{obtener_tiempo(*coord)}\n\n"

mensaje += f"""💪 Frase del día

"{random.choice(FRASES)}"

¡Que tengas un gran día! 🚀
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)
