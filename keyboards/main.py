from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def main_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "📰 Mis intereses",
                callback_data="interests"
            )

        ],

        [

            InlineKeyboardButton(
                "👤 Perfil",
                callback_data="profile"
            )

        ],

        [

            InlineKeyboardButton(
                "⚙ Configuración",
                callback_data="settings"
            )

        ],

        [

            InlineKeyboardButton(
                "ℹ Ayuda",
                callback_data="help"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)
