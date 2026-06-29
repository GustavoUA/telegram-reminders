import random

QUOTES = [

    "El éxito es la suma de pequeños esfuerzos repetidos cada día.",

    "La disciplina supera al talento cuando el talento no se esfuerza.",

    "No tienes que ser el mejor, solo mejor que ayer.",

    "Cada entrenamiento cuenta, incluso cuando no tienes ganas.",

    "Los grandes resultados llegan después de muchos pequeños pasos.",

    "Nunca abandones un objetivo por el tiempo que llevará conseguirlo.",

    "La constancia convierte lo imposible en inevitable.",

    "Hoy es una nueva oportunidad para mejorar.",

    "La motivación te hace empezar; el hábito te hace continuar.",

    "El dolor de hoy será la fuerza de mañana.",

    "Haz hoy lo que otros no quieren para vivir mañana como otros no pueden.",

    "Cada kilómetro recorrido fortalece también tu mente.",

    "No importa lo lento que avances, siempre estarás por delante del que no lo intenta.",

    "Los límites suelen estar mucho más en la mente que en el cuerpo.",

    "Las oportunidades aparecen cuando estás preparado para aprovecharlas.",

    "La excelencia no es un acto, es un hábito.",

    "El esfuerzo nunca engaña.",

    "Las metas grandes se consiguen con pequeñas acciones diarias.",

    "Si puedes soñarlo, puedes conseguirlo.",

    "Nunca dejes de aprender."
]


def get_quote():

    frase = random.choice(QUOTES)

    return f"""
━━━━━━━━━━━━━━━━━━━━━━

💪 *FRASE DEL DÍA*

_{frase}_

━━━━━━━━━━━━━━━━━━━━━━
"""
