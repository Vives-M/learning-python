# Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1 et  nombre2.
nombre1 = input("Donnez un premier nombre : ")
nombre2 = input("Donnez un second nombre : ")

# nombre1et  nombre2sont des chaînes de caractères (str). Utilisez la fonction  isnumeric  (explication de la fonction) pour vérifier que ce sont des nombres.
# Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot cléraise:raise SystemExit("Fin du programme")
if nombre1.isnumeric and nombre2.isnumeric :
    print("les 2 nombres sont bien des nombres")
else :
    raise SystemExit("Fin du programme")

# Sinon, convertissez les deux nombres en nombres entiers avec la fonction  int.
nombre1 = int(nombre1)
nombre2 = int(nombre2)

# Créez une variable operation et utilisez input pour obtenir l'opération souhaitée par l'utilisateur.
operation = input("Choisissez une opération parmi les suivantes : + , - , / , * ")


# Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.
# Effectuez le calcul en fonction de la valeur de operation et stockez le résultat dans la variable resultat.
# Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire
# pour quitter le programme si le deuxième nombre est 0.
# Astuce : lors de la division, utilisez la fonction round pour arrondir le résultat et le rendre plus lisible !

match operation :
    case "+" :
        resultat = nombre1 + nombre2
    case "-" :
        resultat = nombre1 - nombre2
    case "*" :
        resultat = nombre1 * nombre2
    case "/" :

        if nombre2 != 0 :
            resultat = round(nombre1 / nombre2)
        else :
           raise SystemExit("La division par zéro est impossible, fin du programme")
    case _ :
        raise SystemExit("Je ne connais pas cet opérateur, fin du programme")

print(f"Résultat de {nombre1} {operation} {nombre2} = {resultat}")
