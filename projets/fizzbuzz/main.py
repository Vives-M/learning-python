# Ecire un programme qui affiche les nombres de 1 à 100 avec les exceptions suivantes :

nombres = list(range(1, 101))
# print(nombres)

for nombre in nombres:
# Multiples de 3 et 5 : affichage de 'FizzBuzz' à la place du nombre
    if int(nombre/3) == (nombre/3) and int(nombre/5) == (nombre/5):
        nombre = 'FizzBuzz'
        print(nombre)
# Multiples de 3 : affichage de 'Fizz' à la place du nombre
    elif int(nombre/3) == (nombre/3):
        nombre = 'Fizz'
        print(nombre)
# Multiples de 5 : affichage de 'Buzz' à la place du nombre
    elif int(nombre/5) == (nombre/5):
        nombre = 'Buzz'
        print(nombre)
    else:
        print(nombre)
