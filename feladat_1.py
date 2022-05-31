"""[1] Kérjen be a felhasználótól egy 
karakterláncot. Ha a szöveg több,
mint 8 karakter hosszú, írja ki azt
a terminálra visszafelé, csupa kisbetűv
"""
bekeres = input("írjon be legalább 9 karakterből álló szöveget: ")
if len(bekeres) > 8:
  bekeres = bekeres.lower()
  bekeres = bekeres[::-1]
  print(bekeres)
else:
  print(f"A(z) {bekeres} kevesebb, mint 9 karakter hosszú!")