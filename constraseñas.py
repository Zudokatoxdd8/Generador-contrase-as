import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = int(input("Introduce la longitud de la contraseña: "))

generar = ""

for _ in range(password):
    generar += random.choice(characters)

print("Contraseña generada:", generar)
