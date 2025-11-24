vidas=int(input("Estas por enbarcarte en una gran aventura ¿cuantas vidas tienes?"))
if vidas>=5:
    print("Este nivel sera Facil")
if vidas<5 and vidas>2:
    print("Este es un nivel Medio, sobreviviras bastante tiempo")
if vidas<3 and vidas>0:
    print("Este va a ser un nivel Dificil")
if vidas==0:
    print("Sera casi imposible que pases este nivel ")