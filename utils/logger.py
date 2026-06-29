from datetime import datetime


def log(level, module, message):

    print(

        f"[{datetime.now()}] "

        f"[{level}] "

        f"[{module}] "

        f"{message}"

    )
