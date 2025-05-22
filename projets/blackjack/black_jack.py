# Implémente la fonction score_pioche_banque qui retourne un nombre aléatoire entre 16 et 21
import random
def score_pioche_banque():
    liste_scores_possibles_banque = range(1,22)
    return random.choice(liste_scores_possibles_banque)
print("Score banque : ", score_pioche_banque())

# Implémente la fonction pioche_carte_joueur qui retourne un nombre aléatoire entre 1 et 11
def pioche_carte_joueur():
    liste_scores_possibles_joueur = range(1,12)
    return random.choice(liste_scores_possibles_joueur)
print("Score joueur : ", pioche_carte_joueur())
