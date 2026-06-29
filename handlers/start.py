from telegram import Update
from telegram.ext import ContextTypes

from database import Database
from keyboards.main import main_keyboard

db = Database()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    db.add_user(
        chat_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name or "",
        username=user.username or ""
    )

    await update.message.reply_text(

f"""
🤖 Bienvenido a Hermes

Hola {user.first_name}.

Ya formas parte de Hermes.

Cada día recibirás un briefing personalizado con la información que realmente te interesa.

Pulsa una opción del menú.
""",

        reply_markup=main_keyboard()

    )
