import requests
from urllib.parse import quote


# ============================================================
# CONFIGURACIÓN
# ============================================================

DEFAULT_CITY = "Puerto de la Cruz"

DEFAULT_LAT = 28.4133

DEFAULT_LON = -16.5485


# ============================================================
# API GEOCODING
# ============================================================

GEOCODING_URL = (
    "https://geocoding-api.open-meteo.com/v1/search"
    "?name={city}"
    "&count=1"
    "&language=es"
    "&format=json"
)


# ============================================================
# API WEATHER
# ============================================================

WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude={lat}"
    "&longitude={lon}"
    "&current="
    "temperature_2m,"
    "relative_humidity_2m,"
    "apparent_temperature,"
    "weather_code,"
    "wind_speed_10m"
    "&daily="
    "temperature_2m_max,"
    "temperature_2m_min,"
    "sunrise,"
    "sunset,"
    "precipitation_probability_max"
    "&timezone=auto"
)
# ============================================================
# OBTENER COORDENADAS
# ============================================================

def get_coordinates(city):

    try:

        url = GEOCODING_URL.format(

            city=quote(city)

        )

        response = requests.get(

            url,

            timeout=10

        )

        response.raise_for_status()

        data = response.json()

        if "results" not in data:

            return (

                DEFAULT_CITY,

                DEFAULT_LAT,

                DEFAULT_LON

            )

        result = data["results"][0]

        return (

            result["name"],

            result["latitude"],

            result["longitude"]

        )

    except Exception:

        return (

            DEFAULT_CITY,

            DEFAULT_LAT,

            DEFAULT_LON

        )
# ============================================================
# ICONOS DEL TIEMPO
# ============================================================

def weather_icon(code: int) -> str:

    if code == 0:
        return "☀️"

    if code in [1, 2]:
        return "🌤"

    if code == 3:
        return "☁️"

    if code in [45, 48]:
        return "🌫"

    if code in [51, 53, 55]:
        return "🌦"

    if code in [61, 63, 65]:
        return "🌧"

    if code in [66, 67]:
        return "🌨"

    if code in [71, 73, 75]:
        return "❄️"

    if code in [80, 81, 82]:
        return "🌦"

    if code in [95, 96, 99]:
        return "⛈"

    return "🌤"


# ============================================================
# DESCRIPCIÓN DEL TIEMPO
# ============================================================

def weather_description(code: int) -> str:

    descriptions = {

        0: "Despejado",

        1: "Poco nuboso",

        2: "Parcialmente nuboso",

        3: "Cubierto",

        45: "Niebla",

        48: "Niebla helada",

        51: "Llovizna ligera",

        53: "Llovizna",

        55: "Llovizna intensa",

        61: "Lluvia ligera",

        63: "Lluvia",

        65: "Lluvia intensa",

        66: "Lluvia helada",

        67: "Lluvia helada intensa",

        71: "Nieve ligera",

        73: "Nieve",

        75: "Nieve intensa",

        80: "Chubascos",

        81: "Chubascos fuertes",

        82: "Chubascos muy fuertes",

        95: "Tormenta",

        96: "Tormenta con granizo",

        99: "Tormenta intensa"

    }

    return descriptions.get(code, "Sin datos")
# ============================================================
# ICONOS DEL TIEMPO
# ============================================================

def weather_icon(code: int) -> str:

    if code == 0:
        return "☀️"

    if code in [1, 2]:
        return "🌤"

    if code == 3:
        return "☁️"

    if code in [45, 48]:
        return "🌫"

    if code in [51, 53, 55]:
        return "🌦"

    if code in [61, 63, 65]:
        return "🌧"

    if code in [66, 67]:
        return "🌨"

    if code in [71, 73, 75]:
        return "❄️"

    if code in [80, 81, 82]:
        return "🌦"

    if code in [95, 96, 99]:
        return "⛈"

    return "🌤"


# ============================================================
# DESCRIPCIÓN DEL TIEMPO
# ============================================================

def weather_description(code: int) -> str:

    descriptions = {

        0: "Despejado",

        1: "Poco nuboso",

        2: "Parcialmente nuboso",

        3: "Cubierto",

        45: "Niebla",

        48: "Niebla helada",

        51: "Llovizna ligera",

        53: "Llovizna",

        55: "Llovizna intensa",

        61: "Lluvia ligera",

        63: "Lluvia",

        65: "Lluvia intensa",

        66: "Lluvia helada",

        67: "Lluvia helada intensa",

        71: "Nieve ligera",

        73: "Nieve",

        75: "Nieve intensa",

        80: "Chubascos",

        81: "Chubascos fuertes",

        82: "Chubascos muy fuertes",

        95: "Tormenta",

        96: "Tormenta con granizo",

        99: "Tormenta intensa"

    }

    return descriptions.get(code, "Sin datos")
# ============================================================
# OBTENER TIEMPO
# ============================================================

def get_weather(city=DEFAULT_CITY):

    try:

        # Obtener coordenadas de la ciudad
        city_name, latitude, longitude = get_coordinates(city)

        response = requests.get(

            WEATHER_URL.format(

                lat=latitude,

                lon=longitude

            ),

            timeout=10

        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        daily = data["daily"]

        icon = weather_icon(current["weather_code"])

        description = weather_description(current["weather_code"])

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

🌤 *TIEMPO*

📍 {city_name}

{icon} {description}

🌡 Temperatura: *{current['temperature_2m']}°C*

🤗 Sensación térmica: *{current['apparent_temperature']}°C*

⬆ Máxima: *{daily['temperature_2m_max'][0]}°C*

⬇ Mínima: *{daily['temperature_2m_min'][0]}°C*

💧 Humedad: *{current['relative_humidity_2m']}%*

💨 Viento: *{current['wind_speed_10m']} km/h*

🌧 Probabilidad de lluvia: *{daily['precipitation_probability_max'][0]}%*

🌅 Amanecer: {daily['sunrise'][0][-5:]}

🌇 Atardecer: {daily['sunset'][0][-5:]}

━━━━━━━━━━━━━━━━━━━━━━
"""

    except Exception as e:

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

🌤 *TIEMPO*

No ha sido posible obtener la información meteorológica.

Error:

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""


# ============================================================
# PRUEBA
# ============================================================

if __name__ == "__main__":

    print(get_weather("Madrid"))

