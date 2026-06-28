```python
from datetime import datetime

DIAS = {
    0: {
        "titulo": "💪 Entrenamiento funcional",
        "descripcion": "Trabaja fuerza, estabilidad y movilidad."
    },
    1: {
        "titulo": "🏃 Carrera",
        "descripcion": "Rodaje suave de 5 km.\nRitmo recomendado: 5:45 - 6:00 min/km."
    },
    2: {
        "titulo": "💪 Entrenamiento funcional",
        "descripcion": "Trabajo de fuerza y core."
    },
    3: {
        "titulo": "🏃 Carrera",
        "descripcion": "Series o cambios de ritmo."
    },
    4: {
        "titulo": "🚶 Descanso activo",
        "descripcion": "Caminar, estirar o movilidad."
    },
    5: {
        "titulo": "🏃 Tirada libre",
        "descripcion": "Rodaje cómodo de 5-8 km."
    },
    6: {
        "titulo": "😴 Descanso",
        "descripcion": "Recuperación completa."
    }
}


def get_training():

    hoy = datetime.now().weekday()

    entreno = DIAS[hoy]

    return f"""🏃 Entrenamiento de hoy

{entreno['titulo']}

📌 Objetivo

{entreno['descripcion']}
"""
```
