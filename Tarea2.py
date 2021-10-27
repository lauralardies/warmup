print("Hola mundo!")
print(chr(27)+"[0;32m"+"Hola mundo!")

# Para editar el color del texto debemos introducir el siguiente código: print(chr(27)+"[0;32m"+"Introduce text here")
# El 0 indica el estilo del texto, estos son los distintos estilos:
# 0 - sin efecto; 1 - negrita; 2 - débil; 3 - cursiva; 4 - subrayado; 5 - inverso; 6 - oculto; 7 - tachado.
# El 32  indica el color del texto, estos son los distintos colores que se pueden programar:
# 30 - negro; 31 - rojo; 32 - verde; 33 - amarillo; 34 - azul; 35 - morado; 36 - cian; 37 - blanco.

print(chr(27)+"[0;37m")
# Copiamos el código de nuevo, pero cambiamos el color a blanco de nuevo (en vez de 32, el número será 37).