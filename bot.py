import os
import asyncio

from dotenv import load_dotenv

from telegram import Bot
from telegram.constants import ParseMode

from database import Database
from modules.formatter import create_briefing


# ============================================================
# CONFIGURACIÓN
# ============================================================

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError(
        "No se encontró TELEGRAM_TOKEN en el archivo .env"
    )

bot = Bot(token=TOKEN)

db = Database()


# ============================================================
# LOG
# ============================================================

def log(message):

    print(f"[HERMES] {message}")


# ============================================================
# GENERAR MENSAJE
# ============================================================
def build_message(user):

    nombre = user.get("first_name", "Usuario")

    chat_id = user["chat_id"]

    ciudades = db.get_cities(chat_id)

    intereses = db.get_interests(chat_id)

    return create_briefing(

        nombre=nombre,

        ciudades=ciudades,

        intereses=intereses

    )

# ============================================================
# ENVIAR BRIEFING A UN USUARIO
# ============================================================

async def send_to_user(user):

    try:

        chat_id = user["chat_id"]

        mensaje = build_message(user)

        await bot.send_message(

            chat_id=chat_id,

            text=mensaje,

            parse_mode=ParseMode.MARKDOWN,

            disable_web_page_preview=True

        )

        log(

            f"Briefing enviado a {user['first_name']} ({chat_id})"

        )

        db.update_last_seen(chat_id)

        return True

    except Exception as e:

        log(

            f"ERROR enviando a {user['chat_id']} -> {e}"

        )

        return False


# ============================================================
# ENVIAR A TODOS LOS USUARIOS
# ============================================================

async def send_all():

    usuarios = db.get_all_users()

    if not usuarios:

        log("No existen usuarios registrados.")

        return

    log(

        f"Usuarios registrados: {len(usuarios)}"

    )

    enviados = 0

    errores = 0

    for usuario in usuarios:

        ok = await send_to_user(usuario)

        if ok:

            enviados += 1

        else:

            errores += 1

        await asyncio.sleep(1)

    log("--------------------------------")

    log(f"Enviados : {enviados}")

    log(f"Errores  : {errores}")

    log("--------------------------------")
# ============================================================
# MAIN
# ============================================================

async def main():

    log("======================================")
    log("HERMES - Briefing Diario")
    log("======================================")

    await send_all()

    db.close()

    log("Proceso finalizado correctamente.")


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        log("Proceso cancelado por el usuario.")

    except Exception as e:

        log(f"ERROR GENERAL -> {e}")

