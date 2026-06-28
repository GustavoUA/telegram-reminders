
import random
from pathlib import Path

DATA_FILE = Path("data/curiosities.txt")


def get_curiosity():
    """
    Devuelve una curiosidad informática aleatoria.
    """

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            curiosidades = [
                linea.strip()
                for linea in f.readlines()
                if linea.strip()
            ]

        if not curiosidades:
            return (
                "💻 Curiosidad informática\n\n"
                "No hay curiosidades disponibles.\n"
            )

        curiosidad = random.choice(curiosidades)

        return f"""💻 Curiosidad informática

{curiosidad}
"""

    except Exception:
        return (
            "💻 Curiosidad informática\n\n"
            "No se pudo cargar la curiosidad del día.\n"
        )
