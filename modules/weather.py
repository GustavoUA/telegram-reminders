import requests
from config import CITIES

WEATHER_CODES = {
    0: "☀️ Despejado",
    1: "🌤️ Poco nuboso",
    2: "⛅ Parcialmente nublado",
    3: "☁️ Nublado",
    45: "🌫️ Niebla",
    48: "🌫️ Niebla con escarcha",
    51: "🌦️ Llovizna ligera",
    53: "🌦️ Llovizna moderada",
    55: "🌧️ Llovizna intensa",
    61: "🌧️ Lluvia ligera",
    63: "🌧️ Lluvia moderada",
    65: "🌧️ Lluvia intensa",
    71: "❄️ Nieve ligera",
    73: "❄️ Nieve moderada",
    75: "❄️ Nieve intensa",
    80: "🌦️ Chubascos ligeros",
    81: "🌧️ Chubascos moderados",
    82: "🌧️ Chubascos intensos",
    95: "⛈️ Tormenta",
    96: "⛈️ Tormenta con granizo",
    99: "⛈️ Tormenta fuerte con granizo"
}


def get_city_weather(name, lat, lon):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,wind_speed_10m,weather_code"
    )

    r = requests.get(url, timeout=20)
    r.raise_for_status()

    data = r.json()["current"]

    temp = round(data["temperature_2m"])
    sensation = round(data["apparent_temperature"])
    humidity = data["relative_humidity_2m"]
    wind = round(data["wind_speed_10m"])
    code = data["weather_code"]

    weather = WEATHER_CODES.get(code, "🌍 Sin datos")

    return f"""📍 {name}

{weather}

🌡️ Temperatura: {temp}°C
🥵 Sensación: {sensation}°C
💧 Humedad: {humidity}%
💨 Viento: {wind} km/h
"""


def get_weather():

    text = "🌤️ TIEMPO\n\n"

    try:

        for city, coords in CITIES.items():

            text += get_city_weather(
                city,
                coords["lat"],
                coords["lon"]
            )

            text += "\n"

        return text

    except Exception:

        return """🌤️ TIEMPO

No se ha podido obtener la información meteorológica.
"""