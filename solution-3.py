
def pregunta_1(n: float, T: float, V: float, a: float, b: float) -> float:


    resultado = n*T*8.314 / (V-n*b) - a*(n**2)/V**2

    return round(resultado,3)
def pregunta_2(cantidad: int, precio: float) -> float:

    if cantidad > 100:
        return  precio * 0.75 * cantidad
    elif cantidad > 50:
        return  precio * 0.82 * cantidad
    elif cantidad >= 20:
        return  precio * 0.9 * cantidad
    elif cantidad >= 10:
        return  precio * 0.95 * cantidad
    else:
        return precio * cantidad

def pregunta_3(monedas: int, estrella: bool, vidas: int) -> str:
    if vidas == 0:
        return "Game Over"
    elif estrella == True and monedas >= 50:
        return "Invencible y Bonus"
    elif eazstrella:
        return "Invencible"
    elif monedas >= 100:
        return  "Vida Extra"
    elif monedas >= 50:
        return  "Bonus"
    else:
        return "Continuar"


    return None

def pregunta_4(cafeina: float) -> int:
    horas = 0
    if cafeina < 20:
        return  0
    while cafeina >= 20:
        horas += 1
        cafeina /= 2
    return  horas


