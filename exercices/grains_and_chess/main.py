def square(number):
    """
    Calcul du nombre de grains sur un carré donné.
    :param: int - numéro du carré sur lequel on souhaite connaître le nombre de grains
    :return: int - nombre de grains sur le carré demandé
    Exception : afficher un message d'erreur personnalisé quand le carré demandé n'existe pas : raise ValueError("Square must be between 1 and 64")
    """

    numbers = range(1,65)
    if number == 1:
        return 1
    elif number in numbers:
        return 2**(number-1)
    else:
        raise ValueError("Vous devez indiquer une case entre 1 et 64.")


def total():
    """
    Calcul du nombre total de grains sur l'échiquier.
    :return: int - nombre de grains total sur l'échiquier.
    """

    somme = 0
    for i in range(1,65):
        somme += square(i)
    return somme
