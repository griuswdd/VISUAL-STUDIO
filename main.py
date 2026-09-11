def contar_vocales(str):
    diccionario = {}
    vocales = ["a","e","i","o","u"]
    for letra in str:
        if letra in vocales:
            diccionario[letra] += 1

    return diccionario
print(contar_vocales("Hola Mundo"))