from database import Database

db = Database()


# ============================================================
# NOMBRES AMIGABLES
# ============================================================

TIMEZONE_NAMES = {

    "Atlantic/Canary": "🇮🇨 Canarias",
    "Europe/Madrid": "🇪🇸 Madrid",
    "Europe/London": "🇬🇧 Londres",
    "America/New_York": "🇺🇸 Nueva York",
    "Asia/Tokyo": "🇯🇵 Tokio"

}


LANGUAGE_NAMES = {

    "es": "🇪🇸 Español",
    "en": "🇬🇧 English",
    "fr": "🇫🇷 Français",
    "it": "🇮🇹 Italiano"

}


# ============================================================
# CONFIGURACIÓN
# ============================================================

def get_settings(chat_id):

    user = db.get_user(chat_id)

    if not user:
        return None

    ciudades = db.get_cities(chat_id)
    intereses = db.get_interests(chat_id)

    timezone = db.get_timezone(chat_id)
    briefing = db.get_briefing_time(chat_id)
    language = db.get_language(chat_id)

    timezone = TIMEZONE_NAMES.get(timezone, timezone)
    language = LANGUAGE_NAMES.get(language, language)

    texto = f"""
⚙️ *CONFIGURACIÓN DE HERMES*

👤 *Usuario*
{user["first_name"]}

🌍 *Zona horaria*
{timezone}

⏰ *Hora del briefing*
{briefing}

🌐 *Idioma*
{language}

📍 *Ciudades*
{len(ciudades)} configuradas

📰 *Intereses*
{len(intereses)} seleccionados
"""

    return texto