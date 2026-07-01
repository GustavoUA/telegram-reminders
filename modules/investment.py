import yfinance as yf


# ============================================================
# ACTIVOS
# ============================================================

ASSETS = {

    "BTC-USD": ("₿", "Bitcoin"),

    "ETH-USD": ("♦️", "Ethereum"),

    "GC=F": ("🥇", "Oro"),

    "^GSPC": ("📈", "S&P 500"),

    "^IXIC": ("💻", "Nasdaq"),

    "^IBEX": ("🇪🇸", "IBEX 35"),

    "NVDA": ("🤖", "NVIDIA"),

    "MSFT": ("🪟", "Microsoft"),

    "AAPL": ("🍎", "Apple")

}


# ============================================================
# CONSEJOS
# ============================================================

TIPS = [

    "Invierte siempre con una visión a largo plazo.",

    "Diversificar reduce el riesgo de la cartera.",

    "No inviertas dinero que puedas necesitar a corto plazo.",

    "Las caídas del mercado también generan oportunidades.",

    "Evita tomar decisiones basadas únicamente en las emociones.",

    "Revisa periódicamente tu cartera, pero evita sobreoperar.",

    "Una buena inversión comienza con una buena formación.",

    "La paciencia suele ser una de las mejores estrategias.",

    "Invierte de forma periódica para reducir el impacto de la volatilidad.",

    "Recuerda: rentabilidades pasadas no garantizan resultados futuros."

]


# ============================================================
# OBTENER DATOS
# ============================================================

def get_asset(symbol):

    try:

        ticker = yf.Ticker(symbol)

        info = ticker.fast_info

        price = info.get("lastPrice")

        previous = info.get("previousClose")

        if price is None or previous is None:

            return None

        variation = ((price - previous) / previous) * 100

        emoji, name = ASSETS[symbol]

        arrow = "📈" if variation >= 0 else "📉"

        return f"""{emoji} *{name}*

💵 {price:.2f}

{arrow} {variation:+.2f} %
"""

    except Exception:

        return None


# ============================================================
# INVERSIÓN
# ============================================================

def get_investment():

    texto = """
━━━━━━━━━━━━━━━━━━━━━━

📈 *INVERSIÓN*

"""

    activos = [

        "BTC-USD",

        "ETH-USD",

        "GC=F",

        "^GSPC",

        "^IXIC",

        "NVDA"

    ]

    encontrados = 0

    for activo in activos:

        dato = get_asset(activo)

        if dato:

            texto += dato + "\n"

            encontrados += 1

    if encontrados == 0:

        return """
━━━━━━━━━━━━━━━━━━━━━━

📈 *INVERSIÓN*

No ha sido posible obtener información del mercado.

━━━━━━━━━━━━━━━━━━━━━━
"""

    import random

    texto += f"""

💡 *CONSEJO DEL DÍA*

{random.choice(TIPS)}

⚠️ Información orientativa. No constituye asesoramiento financiero.

━━━━━━━━━━━━━━━━━━━━━━
"""

    return texto


# ============================================================
# PRUEBA
# ============================================================

if __name__ == "__main__":

    print(get_investment())