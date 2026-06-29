import random
import feedparser


RSS_URL = "https://www.incibe.es/incibe-cert/feed"


TIPS = [

    "Utiliza siempre autenticación en dos factores (2FA).",

    "No reutilices la misma contraseña en diferentes servicios.",

    "Mantén Windows y tus aplicaciones siempre actualizadas.",

    "Desconfía de los correos que soliciten información personal.",

    "Haz copias de seguridad periódicamente.",

    "Utiliza un gestor de contraseñas.",

    "Nunca abras enlaces sospechosos recibidos por WhatsApp o correo.",

    "Evita conectarte a redes WiFi públicas sin VPN.",

    "Revisa periódicamente los dispositivos conectados a tus cuentas.",

    "Mantén activado Microsoft Defender o tu antivirus."
]


def get_cyber():

    try:

        feed = feedparser.parse(RSS_URL)

        if not feed.entries:

            return """
━━━━━━━━━━━━━━━━━━━━━━

🔐 *CIBERSEGURIDAD*

No hay noticias disponibles.

━━━━━━━━━━━━━━━━━━━━━━
"""

        noticia = feed.entries[0]

        titulo = noticia.title.strip()

        consejo = random.choice(TIPS)

        texto = f"""
━━━━━━━━━━━━━━━━━━━━━━

🔐 *CIBERSEGURIDAD*

🚨 Última noticia

• {titulo}

💡 Consejo del día

{consejo}

━━━━━━━━━━━━━━━━━━━━━━
"""

        return texto

    except Exception as e:

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

🔐 *CIBERSEGURIDAD*

No ha sido posible obtener la información.

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""
