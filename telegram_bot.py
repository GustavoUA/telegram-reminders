from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from config import TELEGRAM_TOKEN
from database import (
    init_db,
    add_user,
)

# ==========================================
# INTERESES DISPONIBLES
# ==========================================

INTERESTS = [

    ("🤖 IA", "ia"),

    ("💻 Tecnología", "tech"),

    ("🔐 Ciberseguridad", "cyber"),

    ("🏍 MotoGP", "motogp"),

    ("📈 Economía", "economy"),

    ("💼 Empleo IT", "jobs"),

]

# ==========================================
# MENÚ
# ==========================================


def build_keyboard():

    keyboard = []

    for text, value in INTERESTS:

        keyboard.append([
            InlineKeyboardButton(
                text,
                callback_data=value
            )
        ])

    keyboard.append([
        InlineKeyboardButton(
            "💾 Guardar",
            callback_data="save"
        )
    ])

    return InlineKeyboardMarkup(keyboard)


# ==========================================
# START
# ==========================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(

        chat_id=user.id,

        first_name=user.first_name,

        username=user.username

    )

    await update.message.reply_text(

        f"""
🤖 Bienvenido a Hermes

Hola {user.first_name}.

Ya estás registrado correctamente.

Ahora selecciona tus intereses.
""",

        reply_markup=build_keyboard()

    )


# ==========================================
# PERFIL
# ==========================================


async def perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    await update.message.reply_text(

f"""
👤 Perfil

Nombre:
{user.first_name}

Usuario:
@{user.username}

Chat ID:
{user.id}
"""

    )


# ==========================================
# CALLBACKS
# ==========================================


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "save":

        await query.edit_message_text(

            "✅ Preferencias guardadas."

        )

        return

    await query.answer(

        f"Has seleccionado: {query.data}",

        show_alert=True

    )


# ==========================================
# MAIN
# ==========================================


def main():

    init_db()

    app = Application.builder().token(
        TELEGRAM_TOKEN
    ).build()

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "perfil",
            perfil
        )
    )

    app.add_handler(
        CallbackQueryHandler(button)
    )

    print()

    print("===================================")
    print("      Hermes Telegram Bot")
    print("===================================")

    app.run_polling()


if __name__ == "__main__":

    main()