print("Estas por enbarcarte en una gran aventura")
print("Jugaras 5 partidas distintas y necesitaras vidas suficientes para pasar la noche.Depende de cuantas tengas sera la dificultad.¿Preparado?.")

for i in range(5): 
  vidas=int(input("¿Cuantas vidas tienes?"))
  if vidas>=5:
      print("Este nivel sera Facil")
  if vidas<5 and vidas>2:
      print("Este es un nivel Medio, sobreviviras bastante tiempo")
  if vidas<3 and vidas>0:
       print("Este va a ser un nivel Dificil")
  if vidas==0:
       print("Sin duda no sobreviviras esta noche")