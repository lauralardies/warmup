f = open("flag.txt", "w")
f.write("This is file flag.txt")
f.close

f = open("flag.txt", "r")
print(f.read())

# El resultado que obtenemos en la consola es el contenido del archivo flag.txt: This is file flag.txt