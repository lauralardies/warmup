shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44

if customer_basket_cost >= 100:
    print("Your final price is " + str(customer_basket_cost))
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_basket_cost = customer_basket_cost + shipping_cost
    print("Your final price including shipping is " + str(customer_basket_cost))

# El texto que se muestra al ejecutar el código es: Your final price including shipping is 86.8.

shipping_cost_per_kg = 1.20
customer_basket_cost = 101
customer_basket_weight = 44

if customer_basket_cost >= 100:
    print("Your final price is " + str(customer_basket_cost))
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_basket_cost = customer_basket_cost + shipping_cost
    print("Total basket cost including shipping is " + str(customer_basket_cost))

# Al cambiar el valor de la variable custumer_basket_cost a 101, el mensaje que aparece es: Your final price is 101.
# Diagrama de flujo: https://www.figma.com/file/ltR5i5XbhqhDFkOtIPf3mE/Shipping.py