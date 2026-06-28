from deep_translator import GoogleTranslator


def translate(text, target="es"):

    try:
        return GoogleTranslator(
            source="auto",
            target=target
        ).translate(text)

    except Exception:

        return text
