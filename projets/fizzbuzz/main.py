# Ecire un programme qui affiche les nombres de 1 à 100 avec les exceptions suivantes :

nombres = list(range(1, 101))
# print(nombres)

for n in nombres:
# Multiples de 3 et 5 : affichage de 'FizzBuzz' à la place du nombre
    if int(n/3) == (n/3) and int(n/5) == (n/5):
        n = 'FizzBuzz'
        print(n)
# Multiples de 3 : affichage de 'Fizz' à la place du n
    elif int(n/3) == (n/3):
        n = 'Fizz'
        print(n)
# Multiples de 5 : affichage de 'Buzz' à la place du n
    elif int(n/5) == (n/5):
        n = 'Buzz'
        print(n)
    else:
        print(n)

# Refacto :
# for n in nombres:
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)
