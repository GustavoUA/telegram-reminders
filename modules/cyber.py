import random
import feedparser
from deep_translator import GoogleTranslator


# ============================================================
# RSS CIBERSEGURIDAD
# ============================================================

RSS_FEEDS = [

    "https://feeds.feedburner.com/TheHackersNews",

    "https://www.bleepingcomputer.com/feed/"

]

MAX_NEWS = 3


# ============================================================
# CONSEJOS
# ============================================================

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

    "Mantén activado Microsoft Defender o tu antivirus.",

    "Descarga software únicamente desde sitios oficiales.",

    "No compartas códigos de verificación con nadie.",

    "Bloquea automáticamente el equipo cuando te ausentes.",

    "Revisa periódicamente los permisos de las aplicaciones móviles.",

    "Utiliza contraseñas de al menos 14 caracteres.",

    "Comprueba siempre la dirección web antes de introducir tus credenciales.",

    "Actualiza también el firmware del router de casa.",

    "Evita guardar contraseñas en el navegador si compartes el equipo.",

    "Activa las alertas de inicio de sesión en tus cuentas importantes.",

    "Elimina aplicaciones que ya no utilices."
]


# ============================================================
# LIMPIAR TITULOS
# ============================================================

def clean_title(title):

    title = title.replace("\n", " ")

    title = " ".join(title.split())

    return title.strip()

# ============================================================
# TRADUCIR TEXTO
# ============================================================

def translate(text):

    try:

        return GoogleTranslator(
            source="auto",
            target="es"
        ).translate(text)

    except Exception:

        return text

# ============================================================
# OBTENER CIBERSEGURIDAD
# ============================================================

def get_cyber():

    try:

        noticias = []

        for rss in RSS_FEEDS:

            feed = feedparser.parse(rss)

            if not feed.entries:

                continue

            for entry in feed.entries[:MAX_NEWS]:

                titulo = clean_title(entry.title)
                
                titulo = translate(titulo)
                
                noticias.append(f"• {titulo}")

            if noticias:

                break
        # Si ninguna fuente devuelve noticias
        if not noticias:

            consejo = random.choice(TIPS)

            return f"""
━━━━━━━━━━━━━━━━━━━━━━

🔐 *CIBERSEGURIDAD*

No hay noticias disponibles.

💡 *CONSEJO DEL DÍA*

{consejo}

━━━━━━━━━━━━━━━━━━━━━━
"""

        consejo = random.choice(TIPS)

        texto = f"""
━━━━━━━━━━━━━━━━━━━━━━

🔐 *CIBERSEGURIDAD*

📰 *ÚLTIMAS NOTICIAS*

"""

        texto += "\n".join(noticias)

        texto += f"""

💡 *CONSEJO DEL DÍA*

{consejo}

━━━━━━━━━━━━━━━━━━━━━━
"""

        return texto
    except Exception as e:

        consejo = random.choice(TIPS)

        return f"""
━━━━━━━━━━━━━━━━━━━━━━

🔐 *CIBERSEGURIDAD*

No ha sido posible obtener las noticias.

💡 *CONSEJO DEL DÍA*

{consejo}

━━━━━━━━━━━━━━━━━━━━━━

Error:

{e}

━━━━━━━━━━━━━━━━━━━━━━
"""


# ============================================================
# PRUEBA
# ============================================================

if __name__ == "__main__":

    print(get_cyber())