"""Functions used in preparing Guido's gorgeous lasagna.
https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#Todo: define the 'EXPECTED_BAKE_TIME' constant below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#Todo: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """Calculer le temps de cuisson restant.

    :param elapsed_bake_time: int - temps de cuisson déjà écoulé.
    :return: int - tems de cuisson restant calculé d'après 'EXPECTED_BAKE_TIME'.

    Fonction prenant comme argument le temps de cuisson réel des lasagnes au four et
    renvoyant le temps de cuisson restant en minutes, en fonction de « EXPECTED_BAKE_TIME »."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time



#Todo: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    """ Calculer le temps de préparation (en minutes).

    :param number_of_layers: int - le nombre de couches de lasagnes.
    :return: int - temps total de préparation (en minutes)"""
    return number_of_layers * PREPARATION_TIME


#Todo: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculer le temps de cuisine écoulé.

    :param number_of_layers: int - le nombre de couches de lasagnes.
    :param elapsed_bake_time: int - temps de cuisson déjà écoulé.
    :return: int - temps total écoulé (en minutes) : préparation et cuisson.

    Cette fonction prend deux entiers représentant le nombre de couches de lasagnes
    et le temps de cuisson déjà passé et calcule le nombre total de minutes écoulées
    pour la cuisson des lasagnes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


# Todo: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
