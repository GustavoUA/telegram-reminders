import random
from pathlib import Path

DATA_FILE = Path("data/security_tips.txt")


def get_security_tips():

    try:

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            tips = [
                x.strip()
                for x in f.readlines()
                if x.strip()
            ]

        return f"""🔐 Consejo de ciberseguridad

{random.choice(tips)}
"""

    except Exception:

        return """🔐 Consejo de ciberseguridad

No hay consejos disponibles.
"""
