from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from database import Database

from modules.formatter import create_briefing
from modules.weather import get_weather
from modules.news import get_news
from modules.cyber import get_cyber
from modules.formula1 import get_formula1
from modules.motogp import get_motogp
from modules.football import get_football
from modules.worldcup import get_worldcup
from modules.quotes import get_quote
from modules.ai import get_ai
from modules.tech import get_tech
from modules.training import get_training
from modules.investment import get_investment
from modules.today import get_today
from modules.settings import get_settings
from modules.timezone import set_user_timezone

db = Database()

# ============================================================
# /today
# ============================================================

async def today_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    user = db.get_user(chat_id)

    if not user:

        await update.message.reply_text(
            "❌ No estás registrado. Usa /start primero."
        )

        return

    ciudades = db.get_cities(chat_id)

    intereses = db.get_interests(chat_id)

    mensaje = get_today(

        nombre=user["first_name"],

        ciudades=ciudades,

        intereses=intereses

    )

    await update.message.reply_text(

        mensaje,

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )
# ============================================================
# /weather
# ============================================================

async def weather_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    # Si el usuario escribe /weather Madrid
    if context.args:

        ciudad = " ".join(context.args)

        mensaje = get_weather(ciudad)

        await update.message.reply_text(

            mensaje,

            parse_mode=ParseMode.MARKDOWN

        )

        return

    # Si escribe solamente /weather
    ciudades = db.get_cities(chat_id)

    if not ciudades:

        await update.message.reply_text(

            "❌ No tienes ciudades configuradas."

        )

        return

    mensaje = ""

    for ciudad in ciudades:

        mensaje += get_weather(ciudad)

        mensaje += "\n"

    await update.message.reply_text(

        mensaje,

        parse_mode=ParseMode.MARKDOWN

    )

# ============================================================
# /news
# ============================================================

async def news_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_news(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /cyber
# ============================================================

async def cyber_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_cyber(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /motogp
# ============================================================

async def motogp_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_motogp(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /f1
# ============================================================

async def f1_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_formula1(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /football
# ============================================================

async def football_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_football(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /worldcup
# ============================================================

async def worldcup_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_worldcup(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /quote
# ============================================================

async def quote_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_quote(),

        parse_mode=ParseMode.MARKDOWN

    )
# ============================================================
# /ia
# ============================================================

async def ai_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_ai(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /tech
# ============================================================

async def tech_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_tech(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )


# ============================================================
# /training
# ============================================================

async def training_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_training(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )
# ============================================================
# /investment
# ============================================================

async def investment_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        get_investment(),

        parse_mode=ParseMode.MARKDOWN,

        disable_web_page_preview=True

    )
# ============================================================
# /settings
# ============================================================

async def settings_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    texto = get_settings(chat_id)

    if texto is None:

        await update.message.reply_text(
            "❌ No estás registrado. Usa /start primero."
        )

        return

    await update.message.reply_text(
        texto,
        parse_mode=ParseMode.MARKDOWN
    )
# ============================================================
# /timezone
# ============================================================

async def timezone_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = update.effective_chat.id

    if not context.args:

        actual = db.get_timezone(chat_id)

        await update.message.reply_text(
            f"""🌍 Zona horaria actual

{actual}

Ejemplos:

/timezone canarias
/timezone madrid
/timezone londres
"""
        )

        return

    ciudad = " ".join(context.args)

    ok, respuesta = set_user_timezone(
        chat_id,
        ciudad
    )

    if not ok:

        await update.message.reply_text(respuesta)

        return

    await update.message.reply_text(
        f"""✅ Zona horaria actualizada.

🌍 {respuesta}
"""
    )