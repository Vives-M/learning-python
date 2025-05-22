# Implémente la fonction etat_du_jeu qui crée le message indiquant les scores de la banque et du joueur
def etat_de_jeu(score_banque, score_joueur):
    return print(f"Votre score est de {score_joueur}, la banque a {score_banque}.")


# Implémente la fonction message_fin_du_jeu qui sera appelée à la fin du jeu, qui contient le résultat (victoire, défaite ou push)
def message_fin_de_jeu(score_banque, score_joueur):
    if score_joueur > 21:
        return print("Vous avez dépassé 21, LOSER !")
    elif score_joueur == 21:
        return print("Félicitations ! VICTOIRE par BLACKJACK !")
    elif score_joueur > score_banque:
        return print("Félicitations, vous avez plus de points que la banque, WINNER !")
    elif score_joueur < score_banque:
        return print("Vous avez moins de points que la banque, LOSER !")
    else:
        return print("C'est un push ! Vous pouvez repartir avec votre argent.")
