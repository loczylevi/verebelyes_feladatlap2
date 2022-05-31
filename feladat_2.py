print("""paradicsom: 1199 Ft/Kg
paprika: 1349 Ft/Kg
Vöröshagyma: 289 Ft/Kg """)
v_ertek   = None
par_ertek = None
pap_ertek = None
amig = True
lista = []
while amig:
  vasarlo = input("Kiván valamit vásárolni? ")
  if vasarlo == "igen":
    melyik = input("          Melyik termékből? ")
    if melyik == "vöröshagyma":
      mennyi_voros = float(input("Hány Kg vöröshagyma(o)-t szertne? "))
      v_ertek = mennyi_voros * 289
      lista.append(v_ertek)
                 
    if melyik == "paradicsom":
      mennyi_parad = float(input("Hány Kg paradicsom(o)-t szertne? "))
      par_ertek = mennyi_parad * 1199
      lista.append(par_ertek)
      
  
    if melyik == "paprika":
      mennyi_paprika = float(input("Hány Kg paprika(o)-t szertne? "))
      pap_ertek = mennyi_paprika * 1349
      lista.append(pap_ertek)

    elif melyik != "vöröshagyma" and melyik != "paradicsom" and melyik != "paprika":
      print("Nincs ilyen termék")

  elif vasarlo == "nem":
    break
    amig = False
    

        

print("Köszönjük a vásárlást!")
if len(lista) > 0:
  ossz = sum(lista)
  print(f"Fizetendő összeg: {ossz} Ft")
