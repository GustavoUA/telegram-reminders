from database import Database

db = Database()


def get_settings(chat_id):

    user = db.get_user(chat_id)

    if not user:
        return None

    ciudades = db.get_cities(chat_id)
    intereses = db.get_interests(chat_id)

    texto = f"""
⚙️ *CONFIGURACIÓN DE HERMES*

👤 Usuario: {user["first_name"]}

🏙 Ciudades

"""

    if ciudades:
        for ciudad in ciudades:
            texto += f"• {ciudad}\n"
    else:
        texto += "No configuradas\n"

    texto += "\n📰 Intereses\n\n"

    if intereses:
        for interes in intereses:
            texto += f"✅ {interes}\n"
    else:
        texto += "Sin intereses configurados\n"

    return texto
