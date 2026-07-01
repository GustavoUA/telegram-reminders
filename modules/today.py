from modules.formatter import create_briefing


def get_today(
    nombre="Usuario",
    ciudades=None,
    intereses=None
):

    return create_briefing(
        nombre=nombre,
        ciudades=ciudades,
        intereses=intereses
    )