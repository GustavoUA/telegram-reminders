from datetime import datetime

from modules.weather import get_weather
from modules.news import get_news
from modules.cyber import get_cyber
from modules.motogp import get_motogp
from modules.formula1 import get_formula1
from modules.football import get_football
from modules.quotes import get_quote


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

    ciudad="",

    intereses=None

):

    if intereses is None:

        intereses = []

    mensaje = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 *HERMES*

{greeting()} *{nombre}*

📅 {today()}
"""

    if ciudad:

        mensaje += f"\n📍 {ciudad}"

    mensaje += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    # ============================================================
    # TIEMPO
    # ============================================================

    if "weather" in intereses:

        mensaje += get_weather(ciudad)

    


    # ============================================================
    # NOTICIAS GENERALES
    # ============================================================

    if "news" in intereses:

        mensaje += get_news()

        


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

    mensaje += despedida

    mensaje += """

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

            ciudad="Puerto de la Cruz",

            intereses=[
                "weather",
                "news",
                "cyber",
                "motogp",
                "formula1",
                "football",
            ]

        )

    )
