import random
from datetime import datetime

# Diccionario de horóscopos base
horoscopes = {
    "aries": [
        "Hoy es un día para tomar decisiones valientes.",
        "Cuidado con los impulsos, pero no dejes de soñar.",
        "Tu energía atraerá nuevas oportunidades."
    ],
    "tauro": [
        "Tómate un momento para ti hoy.",
        "El esfuerzo constante será recompensado.",
        "No temas pedir ayuda si la necesitas."
    ],
    "geminis": [
        "Una conversación inesperada te abrirá puertas.",
        "La creatividad será tu aliada.",
        "Hoy es un buen día para escribir o comunicarte."
    ],
    "cancer": [
        "Busca el confort en tu entorno más cercano.",
        "No ignores tu intuición.",
        "El autocuidado será clave hoy."
    ],
    "leo": [
        "Brillarás con luz propia.",
        "Un reto se convierte en tu escenario.",
        "Hoy, liderarás sin darte cuenta."
    ],
    "virgo": [
        "Un detalle hará toda la diferencia.",
        "Tu análisis salvará el día.",
        "La organización te dará paz mental."
    ],
    "libra": [
        "Equilibra tus emociones y decisiones.",
        "Una nueva conexión puede surgir.",
        "Tu diplomacia será admirada."
    ],
    "escorpio": [
        "Mira más allá de las apariencias.",
        "Tu pasión puede inspirar a otros.",
        "No temas mostrar tu vulnerabilidad."
    ],
    "sagitario": [
        "Hoy, la aventura te encuentra a ti.",
        "Confía en tu optimismo.",
        "Una idea loca puede funcionar."
    ],
    "capricornio": [
        "Paso a paso, alcanzarás tus metas.",
        "La paciencia será tu mayor virtud.",
        "Confía en tu plan, incluso si no todos lo entienden."
    ],
    "acuario": [
        "La innovación está de tu lado.",
        "Tu perspectiva única será valorada.",
        "Hoy, piensa en el futuro sin miedo."
    ],
    "piscis": [
        "La sensibilidad será una fuerza, no una debilidad.",
        "Conéctate con tu lado artístico.",
        "Alguien necesita tu apoyo, ofrécelo."
    ]
}

def get_user_sign():
    print("Bienvenido/a a tu Horóscopo del Día ✨")
    print("Por favor, ingresa tu signo zodiacal (ej. Aries, Tauro, Géminis...):")
    user_input = input("> ").strip().lower()
    return user_input

def show_horoscope(sign):
    if sign in horoscopes:
        today = datetime.now().strftime("%d/%m/%Y")
        print(f"\n✨ Horóscopo para {sign.capitalize()} - {today} ✨")
        print(random.choice(horoscopes[sign]))
    else:
        print("\n⚠️ Lo siento, ese signo no es válido. Intenta nuevamente.")

def main():
    sign = get_user_sign()
    show_horoscope(sign)

if __name__ == "__main__":
    main()
