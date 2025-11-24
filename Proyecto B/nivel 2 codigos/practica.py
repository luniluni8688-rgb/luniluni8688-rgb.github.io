def juego():
    print("bienvenido al juego del gato y los tacos")
    personaje = input("Dime el nombre de un personaje: ")
    vidas = int(input("¿cuantas vidas quieres jugar? "))
    print("hola", personaje, "tienes", vidas, "vidas")
    print("ahora", personaje, "lo que tienes que hacer es ver si el gato ha comido los tacos")
    puntaje = 0
    while True:
        comer = input("¿el gato comio los tacos? (si/no): ")
        if comer == "si":
            puntaje += 1
            print("bien", personaje, "tienes", puntaje, "puntos")
        if puntaje == 3:
            puntaje = 0
            print("felicidades", personaje, "ganaste el juego")
            break
        if comer == "no":
            vidas -= 1
            print("mala suerte", personaje, "te quedan", vidas, "vidas")
        if vidas == 0:
            print("perdiste", personaje, "intentalo de nuevo")
            return  # Sale de la función para reiniciar

while True:
    juego()
