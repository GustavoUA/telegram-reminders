from database import Database

from modules.languages.es import TEXT as ES
from modules.languages.en import TEXT as EN
from modules.languages.fr import TEXT as FR
from modules.languages.it import TEXT as IT

db = Database()

LANGUAGES = {

    "es": ES,
    "en": EN,
    "fr": FR,
    "it": IT

}


def get_text(chat_id):

    language = db.get_language(chat_id)

    return LANGUAGES.get(language, ES)
