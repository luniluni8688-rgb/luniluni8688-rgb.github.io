import random

print("¡Es hora de jugar!!")
cantidad = int(input("¿Cuántas veces queres tirar los dados?: "))

tiros = 0
total = 0

while tiros < cantidad:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print("Tu primer tiro dio", dado1, "y el segundo", dado2, "dándote", suma, "puntos")
    total += suma
    tiros += 1

print("La sumatoria final de tus puntos es de", total)
