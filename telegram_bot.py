import os

from dotenv import load_dotenv

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

from database import Database


# ============================================================
# CONFIGURACIÓN
# ============================================================

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("No se encontró TELEGRAM_TOKEN en el archivo .env")

db = Database()

VERSION = "Hermes 1.0"


# ============================================================
# INTERESES DISPONIBLES
# ============================================================

AVAILABLE_INTERESTS = [

    ("weather", "🌤 Tiempo"),
    ("news", "📰 Noticias"),
    ("cyber", "🔐 Ciberseguridad"),
    ("motogp", "🏍 MotoGP"),
    ("formula1", "🏎 Fórmula 1"),
    ("football", "⚽ Fútbol"),
    ("jobs", "💼 Empleo IT"),
    ("ai", "🤖 Inteligencia Artificial"),

]


# ============================================================
# ESTADO TEMPORAL
# ============================================================

# Intereses seleccionados antes de pulsar "Guardar"
user_sessions = {}

# Usuarios que están escribiendo la ciudad
waiting_city = {}
# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "📰 Mis intereses",
                callback_data="menu_interests"
            )
        ],

        [
            InlineKeyboardButton(
                "📍 Mi ciudad",
                callback_data="menu_city"
            )
        ],

        [
            InlineKeyboardButton(
                "👤 Mi perfil",
                callback_data="menu_profile"
            )
        ],

        [
            InlineKeyboardButton(
                "ℹ️ Ayuda",
                callback_data="menu_help"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# TECLADO DE INTERESES
# ============================================================

def interests_keyboard(chat_id):

    seleccionados = user_sessions.get(chat_id, [])

    keyboard = []

    for key, nombre in AVAILABLE_INTERESTS:

        icono = "✅" if key in seleccionados else "⬜"

        keyboard.append(

            [

                InlineKeyboardButton(

                    f"{icono} {nombre}",

                    callback_data=f"toggle_interest:{key}"

                )

            ]

        )

    keyboard.append(

        [

            InlineKeyboardButton(
                "💾 Guardar",
                callback_data="save_interests"
            )

        ]

    )

    keyboard.append(

        [

            InlineKeyboardButton(
                "🔙 Volver",
                callback_data="back_main"
            )

        ]

    )

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# MENÚ CIUDAD
# ============================================================

def city_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "✏️ Cambiar ciudad",
                callback_data="change_city"
            )

        ],

        [

            InlineKeyboardButton(
                "🔙 Volver",
                callback_data="back_main"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# MENÚ PERFIL
# ============================================================

def profile_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "🔙 Volver",
                callback_data="back_main"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# MENÚ AYUDA
# ============================================================

def help_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "🔙 Volver",
                callback_data="back_main"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)
# ============================================================
# START
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    if not db.user_exists(user.id):

        db.add_user(

            chat_id=user.id,

            first_name=user.first_name or "",

            last_name=user.last_name or "",

            username=user.username or ""

        )

        mensaje = f"""
🤖 *Bienvenido a Hermes*

Hola *{user.first_name}*.

Tu cuenta ha sido registrada correctamente.

Ya puedes comenzar a configurar Hermes.

Versión: {VERSION}
"""

    else:

        db.update_last_seen(user.id)

        mensaje = f"""
🤖 *Bienvenido de nuevo*

Hola *{user.first_name}*.

Selecciona una opción del menú.
"""

    await update.message.reply_text(

        mensaje,

        parse_mode="Markdown",

        reply_markup=main_menu()

    )


# ============================================================
# AYUDA
# ============================================================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

"""
🤖 *HERMES*

Comandos disponibles

/start

/help

También puedes utilizar el menú inferior para acceder a todas las funciones.

Powered by Gustavo Ucar de Armas
""",

        parse_mode="Markdown"

    )


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

async def show_main_menu(query):

    await query.edit_message_text(

        "🤖 *Menú principal*\n\nSelecciona una opción.",

        parse_mode="Markdown",

        reply_markup=main_menu()

    )
# ============================================================
# PANTALLA PERFIL
# ============================================================

async def show_profile(query):

    chat_id = query.from_user.id

    user = db.get_user(chat_id)

    intereses = db.get_interests(chat_id)

    if intereses:
        lista = "\n".join(f"• {i}" for i in intereses)
    else:
        lista = "Sin configurar"

    ciudad = user.get("city", "Sin configurar")

    mensaje = f"""
👤 *MI PERFIL*

Nombre:
{user["first_name"]}

Usuario:
@{user["username"]}

Ciudad:
{ciudad}

Intereses:
{lista}
"""

    await query.edit_message_text(

        mensaje,

        parse_mode="Markdown",

        reply_markup=profile_keyboard()

    )


# ============================================================
# PANTALLA CIUDAD
# ============================================================

async def show_city(query):

    chat_id = query.from_user.id

    user = db.get_user(chat_id)

    ciudad = user.get("city", "Sin configurar")

    mensaje = f"""
📍 *MI CIUDAD*

Ciudad actual:

{ciudad}

Pulsa "Cambiar ciudad" para modificarla.
"""

    await query.edit_message_text(

        mensaje,

        parse_mode="Markdown",

        reply_markup=city_keyboard()

    )


# ============================================================
# PANTALLA INTERESES
# ============================================================

async def show_interests(query):

    chat_id = query.from_user.id

    if chat_id not in user_sessions:

        user_sessions[chat_id] = db.get_interests(chat_id)

    await query.edit_message_text(

        "📰 *Selecciona los intereses que quieres recibir diariamente.*",

        parse_mode="Markdown",

        reply_markup=interests_keyboard(chat_id)

    )


# ============================================================
# PANTALLA AYUDA
# ============================================================

async def show_help(query):

    await query.edit_message_text(

"""
🤖 *HERMES*

Powered by Gustavo Ucar de Armas

Versión 1.0

Próximamente:

• Briefing diario
• IA
• Noticias
• Deportes
• Ciberseguridad
• Panel Web
""",

        parse_mode="Markdown",

        reply_markup=help_keyboard()

    )
# ============================================================
# CALLBACKS
# ============================================================

async def callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    chat_id = query.from_user.id

    # ========================================================
    # MENÚ PRINCIPAL
    # ========================================================

    if data == "menu_profile":

        await show_profile(query)
        return

    if data == "menu_city":

        await show_city(query)
        return

    if data == "menu_interests":

        await show_interests(query)
        return

    if data == "menu_help":

        await show_help(query)
        return

    # ========================================================
    # VOLVER
    # ========================================================

    if data == "back_main":

        if chat_id in user_sessions:

            del user_sessions[chat_id]

        await show_main_menu(query)

        return

    # ========================================================
    # CAMBIAR INTERÉS
    # ========================================================

    if data.startswith("toggle_interest:"):

        interest = data.split(":")[1]

        seleccionados = user_sessions.get(chat_id, []).copy()

        if interest in seleccionados:

            seleccionados.remove(interest)

        else:

            seleccionados.append(interest)

        user_sessions[chat_id] = seleccionados

        await query.edit_message_reply_markup(

            reply_markup=interests_keyboard(chat_id)

        )

        return

    # ========================================================
    # GUARDAR INTERESES
    # ========================================================

    if data == "save_interests":

        intereses = user_sessions.get(chat_id, [])

        db.set_interests(chat_id, intereses)

        await query.edit_message_text(

            "✅ *Intereses guardados correctamente.*",

            parse_mode="Markdown",

            reply_markup=main_menu()

        )

        return

    # ========================================================
    # CAMBIAR CIUDAD
    # ========================================================

    if data == "change_city":

        waiting_city[chat_id] = True

        await query.edit_message_text(

            """
📍 *Nueva ciudad*

Escribe ahora el nombre de la ciudad.

Ejemplo:

Madrid
Barcelona
Londres
París
""",

            parse_mode="Markdown"

        )

        return
from telegram.ext import (
    MessageHandler,
    filters,
)

# ============================================================
# MENSAJES DE TEXTO
# ============================================================

async def text_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_user.id

    if waiting_city.get(chat_id):

        city = update.message.text.strip()

        waiting_city.pop(chat_id, None)

        # Guardar ciudad en SQLite
        db.set_city(chat_id, city)

        await update.message.reply_text(

            f"""✅ Ciudad guardada correctamente.

📍 Ciudad actual:

{city}
""",

            reply_markup=main_menu()

        )

        return

    await update.message.reply_text(

        "Utiliza el menú para navegar.",

        reply_markup=main_menu()

    )


# ============================================================
# COMANDOS DESCONOCIDOS
# ============================================================

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "❌ Comando no reconocido.\n\nUtiliza /start."

    )


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(update, context):

    print("=" * 60)
    print("ERROR")
    print(context.error)
    print("=" * 60)


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("HERMES 1.0")
    print("Powered by Gustavo Ucar de Armas")
    print("=" * 60)

    app = Application.builder().token(TOKEN).build()

    # -----------------------------
    # COMANDOS
    # -----------------------------

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # -----------------------------
    # BOTONES
    # -----------------------------

    app.add_handler(CallbackQueryHandler(callbacks))

    # -----------------------------
    # MENSAJES
    # -----------------------------

    app.add_handler(

        MessageHandler(

            filters.TEXT & ~filters.COMMAND,

            text_messages

        )

    )

    # -----------------------------
    # COMANDOS DESCONOCIDOS
    # -----------------------------

    app.add_handler(

        MessageHandler(

            filters.COMMAND,

            unknown

        )

    )

    # -----------------------------
    # ERRORES
    # -----------------------------

    app.add_error_handler(error_handler)

    print("🤖 Hermes iniciado correctamente.")
    print("Esperando mensajes...")

    app.run_polling()


# ============================================================
# INICIO
# ============================================================

if __name__ == "__main__":

    main()
