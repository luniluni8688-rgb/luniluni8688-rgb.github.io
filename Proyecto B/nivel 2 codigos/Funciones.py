import random
print("¡Es hora de jugar!!")
print("Tendran un tiro cada uno, y quien saque el numero mas grande gana")
#Funcion que tira los dados
def tirardados():
 dado1= random.randint(1, 6)
 dado2 = random.randint(1, 6)
 suma = dado1 + dado2
 return suma
#Aca cada jugador juega su partida
jugador1 = tirardados()
print("El jugador 1 tiene un total de", jugador1,"puntos")   
jugador2 = tirardados()
print("El jugador 2 tiene en total", jugador2,"puntos")

if jugador1 > jugador2:
 print("El jugador 1 gano esta vez")  
else:   
 if jugador2 > jugador1:
  print("El jugador 2 gana esta vez") 
 else:
  print("Empataron!")

