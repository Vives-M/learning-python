# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").
# Stockez cette valeur dans une variable  nombres. nombres est une chaîne de caractères (str).

nombres = input("Saisissez une liste de nombres séparés par une virgue (exemple : 1,2,3,4) :")

# Utilisez la fonction split pour transformer cette chaîne de caractères en une variable de type liste.
# liste est une liste de chaîne de caractères.

liste = nombres.split(',')

# Transformez liste en une liste d'entiers liste_entiers, en utilisant la fonction  int.
# Vous devrez convertir chaque élément un par un ! Utilisez une boucle.

liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)


# Calculez et affichez la somme des nombres dans la liste.

somme = 0
for nombre in liste_entiers:
    somme += nombre

print(f"la somme de vos nombres {liste_entiers} est : {somme}")

# Calculez et affichez la moyenne des nombres dans la liste.
moyenne = round(somme/len(liste_entiers))
print(f"La moyenne de vos nombres est de {moyenne}.")

# Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.
nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne +=1
print(f"Vous avez {nombre_au_dessus_moyenne} élément(s) au dessus de la moyenne.")
