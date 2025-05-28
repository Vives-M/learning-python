# Dans cet exercice, vous allez devoir inverser l'ordre des lettres d'un mot.

# Dans cet exemple-ci, le mot est 'Docstring' **votre script doit donc retourner la chaîne de caractère 'Gnirtscod'. **

# Pour valider l'exercice, il faut que la première lettre de votre chaîne de caractère résultat soit en majuscule
# ('Gnirtscod' et non 'gnirtscoD').


mot = 'Docstring'
mot_lowcase = mot.lower()
# join permet de fusionner les éléments pour obtenir la chaîne inversée.
mot_lowcase_inverse = ''.join(reversed(mot_lowcase))
# reversed retourne un itérable inversé
mot_capitalize = mot_lowcase_inverse.capitalize()
print(mot_capitalize)


# Refacto avec les slice :
# print("Docstring"[::-1].capitalize())
