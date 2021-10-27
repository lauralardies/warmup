shipping_cost_per_kg = 1.20
custumer_basket_cost = 34
custumer_basket_weight = 44

if custumer_basket_cost >= 100:
    print("Free shipping!")
else:
    shipping_cost = custumer_basket_weight * shipping_cost_per_kg
    custumer_basket_cost = custumer_basket_cost + shipping_cost
    print("Total basket cost including shipping is " + str(custumer_basket_cost))

shipping_cost_per_kg = 1.20
custumer_basket_cost = 34
custumer_basket_weight = 44

# El texto que se muestra al ejecutar el código es: Total basket cost including shipping is 86.8

if custumer_basket_cost >= 100:
    print("Free shipping!")
else:
    shipping_cost = custumer_basket_weight * shipping_cost_per_kg
    custumer_basket_cost = 101
    print("Total basket cost including shipping is " + str(custumer_basket_cost))

# Al cambiar el valor de la variable customer_basket_cost a 101, el mensaje que aparece es: Total basket cost including shipping is 101

# Diagrama de flujo: https://www.figma.com/file/ltR5i5XbhqhDFkOtIPf3mE/Shipping.py