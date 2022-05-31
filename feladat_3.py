#A galaxis őrzői;2;2014-08-01;170;773 

class Marvel():
  def __init__(self, sor):
    film, fazis, bemutato, koltseg, bevetel = sor.strip().split(";")
    self.film = film
    self.fazis = fazis
    self.bemutato = bemutato
    self.koltseg = int(koltseg)
    self.bevetel = int(bevetel)
    self.ev = int(bemutato[:4])
    self.honap = bemutato[5:7]
    self.nap = bemutato[8:10]
    
    
with open("marvel.txt",encoding="utf-8") as f:
 lista = [Marvel(sor) for sor in f]

#3.1
print(f"{len(lista)}")

#3.2
koltsegek = sum([sor.koltseg for sor in lista])
atlag = koltsegek / len(lista)
print(f"{round(atlag, 2)}Milko")

#3.3
x = 0
for sor in lista:
  if sor.bevetel - sor.koltseg > x:
    x = sor.bevetel - sor.koltseg
    film = sor.film

print(film)


bekeres = int(input("3.4: írjon be egy évszámot: "))

kereso = [sor for sor in lista if sor.ev == bekeres]

print(f"a {bekeres}-ban/ben megjelent marvel filmek:")

[print(f" {sor.film}") for sor in kereso]