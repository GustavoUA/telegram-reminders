from datetime import datetime

from modules.weather import get_weather
from modules.news import get_news
from modules.cyber import get_cyber
from modules.motogp import get_motogp
from modules.formula1 import get_formula1
from modules.football import get_football
from modules.quotes import get_quote
from modules.worldcup import get_worldcup
from modules.investment import get_investment

# ============================================================
# SALUDO
# ============================================================

def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "☀️ Buenos días"

    elif hour < 20:
        return "🌤 Buenas tardes"

    return "🌙 Buenas noches"


# ============================================================
# FECHA
# ============================================================

# ============================================================
# FECHA
# ============================================================

def today():

    dias = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }

    meses = {
        "January": "enero",
        "February": "febrero",
        "March": "marzo",
        "April": "abril",
        "May": "mayo",
        "June": "junio",
        "July": "julio",
        "August": "agosto",
        "September": "septiembre",
        "October": "octubre",
        "November": "noviembre",
        "December": "diciembre",
    }

    ahora = datetime.now()

    dia = dias[ahora.strftime("%A")]

    mes = meses[ahora.strftime("%B")]

    return f"{dia}, {ahora.day} de {mes} de {ahora.year}"
# ============================================================
# CREAR BRIEFING
# ============================================================

def create_briefing(

    nombre="Usuario",

    ciudades=None,

    intereses=None

):

    if ciudades is None:

        ciudades = []

    if intereses is None:

        intereses = []

    mensaje = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 *HERMES*

{greeting()} *{nombre}*

📅 {today()}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    # ============================================================
    # TIEMPO
    # ============================================================

    if "weather" in intereses:

        if ciudades:

            for ciudad in ciudades:

                mensaje += get_weather(ciudad)

        else:

            mensaje += get_weather()
        
    # ============================================================
    # NOTICIAS GENERALES
    # ============================================================

    if "news" in intereses:

        mensaje += get_news()
    # ============================================================
    # INVERSIÓN
    # ============================================================

    if "investment" in intereses:

        mensaje += get_investment()
    # ============================================================
    # CIBERSEGURIDAD
    # ============================================================

    if "cyber" in intereses:

        mensaje += get_cyber()

    # ============================================================
    # MOTOGP
    # ============================================================

    if "motogp" in intereses:

        mensaje += get_motogp()

    # ============================================================
    # FÓRMULA 1
    # ============================================================

    if "formula1" in intereses:

        mensaje += get_formula1()

    # ============================================================
    # FÚTBOL
    # ============================================================

    if "football" in intereses:

        mensaje += get_football()
    
    # ============================================================
    # MUNDIAL
    # ============================================================

    if "worldcup" in intereses:

       mensaje += get_worldcup()

    # ============================================================
    # FRASE MOTIVADORA
    # ============================================================

    mensaje += get_quote()

       # ============================================================
    # DESPEDIDA
    # ============================================================

    hora = datetime.now().hour

    if hora < 12:

        despedida = "☀️ Que tengas un excelente día."

    elif hora < 20:

        despedida = "🌤 Que tengas una excelente tarde."

    else:

        despedida = "🌙 Que tengas una excelente noche."

    mensaje += f"""

{despedida}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 *Powered by Hermes*

Desarrollado por

*Gustavo Ucar de Armas*

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    return mensaje


# ============================================================
# PRUEBA
# ============================================================

if __name__ == "__main__":

    print(

        create_briefing(

            nombre="Gustavo",

            ciudades=[

                "Puerto de la Cruz",

                "San Cristóbal de La Laguna"

            ],

            intereses=[

                "weather",

                "news",

                "cyber",

                "motogp",

                "formula1",

                "football"
                
                "Investment"

            ]

        )

    )
