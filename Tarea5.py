money = 2000
hunger = 18
price_icecream = 100

# Suponemos:
# Cada iteración incrementa el hambre un 20%
# Cada helado baja el hambre un 50%

while money > price_icecream:
    if hunger <= 85:
        hunger = hunger + 20
        if hunger > 100:
            hunger = 100
        print("Im not hungry!")
        print("You have " + str(money) + " left")
    else:
        money = money - price_icecream
        price_icecream = price_icecream + price_icecream * 0.2
        hunger = hunger - 50
        print ("Im hungry! Im going to buy an icecream")
        print("You have " + str(money) + " left")

print("I dont have enough money to buy an icecream")