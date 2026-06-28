```python
import random
from pathlib import Path

DATA_FILE = Path("data/quotes.txt")


def get_motivation():
    """
    Devuelve una frase motivadora aleatoria.
    """

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            frases = [
                linea.strip()
                for linea in f.readlines()
                if linea.strip()
            ]

        if not frases:
            return (
                "💪 Frase del día\n\n"
                "Hoy no hay ninguna frase disponible."
            )

        frase = random.choice(frases)

        return f"""💪 Frase del día

"{frase}"
"""

    except Exception:
        return (
            "💪 Frase del día\n\n"
            "No se pudo cargar la frase de hoy."
        )
```
