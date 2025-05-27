def classify(number):
    """ Un nombre est parfait lorsqu'il est égal la somme de ses diviseurs propres,
    c'est-à-dire tous ses diviseurs à l'exception de lui-même.

    :param number: int a positive integer
    :return: str the classification of the input integer

    Un nombre est parfait lorsqu'il est égal à sa somme aliquote. Par exemple :

        6 est un nombre parfait car 1 + 2 + 3 = 6
        28 est un nombre parfait car 1 + 2 + 4 + 7 + 14 = 28
    Abondant
    Un nombre est abondant lorsqu'il est inférieur à sa somme aliquote. Par exemple :

        12 est un nombre abondant car 1 + 2 + 3 + 4 + 6 = 16
        24 est un nombre abondant car 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36
    Déficient
    Un nombre est déficitaire lorsqu'il est supérieur à sa somme aliquote. Par exemple :

        8 est un nombre déficitaire car 1 + 2 + 4 = 7
        Les nombres premiers sont déficitaires


    """
    numbers = range(1,number)
    somme = 0
    if number >= 1:
        for n in numbers:
            if number % n == 0:
                somme += n
        print(somme)
        if number == somme:
            return "perfect"
        elif number > somme:
            return "deficient"
        return "abundant"
    # if a number to be classified is less than 1.
    raise ValueError("Classification is only possible for positive integers.")
