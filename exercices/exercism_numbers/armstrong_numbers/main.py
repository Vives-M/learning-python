def is_armstrong_number(number):
    """
    Fonction pour déterminer si un nombre donné est un nombre d'Armstrong.
    Un nombre d'Armstrong est un entier naturel qui est égal à la somme des cubes des chiffres qui le composent.
    Exemples :
    - 9 est un nombre d'Armstrong car 9 = 9^1 = 9
    - 10 n'est pas un nombre d'Armstrong car 10 != 1^2 + 0^2 = 1
    - 153 est un nombre d'Armstrong car 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    - 154 n'est pas un nombre d'Armstrong car 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
    """
    # Convertir le nombre en string
    number_in_string = str(number)
    # Récupérer le nombre de digits avec len()
    number_of_digits = len(number_in_string)
    # Si le nombre n'a qu'un digit, number élevé à la puissance du nombre de digits :
    number_power = number ** number_of_digits
    # On initialise à 0 la somme des digits élevés à la puissance  :
    sum_of_digits_power = 0
    print(list(number_in_string))
    # On itère sur la liste créée d'après la string du nombre :
    for i in list(number_in_string):
        # Chaque digit isolé du nombre est élevé à la puissance du nombre total de digits :
        digit_power = int(i)**number_of_digits
        # On ajoute le résultat du digit élevé à la puissance à la somme :
        sum_of_digits_power += digit_power
    print(sum_of_digits_power)
    # Si le number n'a qu'un digit :
    if number == number_power:
        return True
    # Si le number est égal à la somme de ses digits élevés à la puissance du total des digits :
    elif number == sum_of_digits_power:
        return True
    return False
