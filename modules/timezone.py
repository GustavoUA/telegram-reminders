from database import Database

db = Database()

TIMEZONES = {

    "canarias": "Atlantic/Canary",
    "tenerife": "Atlantic/Canary",
    "gran canaria": "Atlantic/Canary",

    "madrid": "Europe/Madrid",
    "barcelona": "Europe/Madrid",
    "españa": "Europe/Madrid",

    "londres": "Europe/London",
    "paris": "Europe/Paris",
    "roma": "Europe/Rome",
    "berlin": "Europe/Berlin",
    "lisboa": "Europe/Lisbon",

    "newyork": "America/New_York",
    "nuevayork": "America/New_York",
    "miami": "America/New_York",
    "losangeles": "America/Los_Angeles",

    "tokyo": "Asia/Tokyo",
    "dubai": "Asia/Dubai",
    "sydney": "Australia/Sydney"
}


def set_user_timezone(chat_id, city):

    city = city.lower().strip()

    if city not in TIMEZONES:
        return False, "❌ Zona horaria no reconocida."

    timezone = TIMEZONES[city]

    db.set_timezone(chat_id, timezone)

    return True, timezone
