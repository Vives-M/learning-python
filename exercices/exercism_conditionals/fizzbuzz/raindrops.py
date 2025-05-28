def convert(number):
    """
    Cette fonction convertit un nombre en son de pluie correspondant. Règles du jeu :
    Si le nombre donné (number) est :
    - divisible par 3, ajoute "Pling" au résultat
    - divisible par 5, ajoute "Plang" au résultat
    - divisible par 7, ajoute "Plong" au résultat
    - non divisible par 3, 5 ou 7, le résultat devra être le nombre donné converti en string.

    :param number: int - nombre à tester pour avoir le bon son
    :result: string - le son correspondant
    """
    pling = "Pling"
    plang = "Plang"
    plong = "Plong"

    
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return pling + plang + plong
    elif number % 3 == 0 and number % 5 == 0:
        return pling + plang
    elif number % 5 == 0 and number % 7 == 0:
        return plang + plong
    elif number % 3 == 0 and number % 7 == 0:
        return pling + plong
    elif number % 3 == 0:
        number = pling
        return number
    elif number % 5 == 0 :
        number = plang
        return number
    elif number % 7 == 0:
        number = plong
        return number
    return str(number)
