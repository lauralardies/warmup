dinero = 2000
hambre = 18
coste_helado = 100

# Suponemos:
# Cada iteración incrementa el hambre un 20%
# Cada helado baja el hambre un 50%

while dinero > coste_helado:
    if hambre <= 85:
        print("Im not hungry!")
        print("You have " + str(dinero) + " left")
        hambre = hambre + 20
        if hambre > 100:
            hambre = 100
    else:
        print ("Im hungry!")
        print("You have " + str(dinero) + " left")
        dinero = dinero - coste_helado
        coste_helado = coste_helado + coste_helado * 0.2
        hambre = hambre - 50

print("I dont have enough money to buy an icecream")
 