# Implémente la fonction principale qui lance un jeu de blackjack depuis le terminal. Il devrait fonctionner comme suit :
# Souhaitez-vous une nouvelle carte ? "o" ou "oui" pour piocher
# > oui
# Votre score est de 6, la banque a 17.
# Souhaitez-vous une nouvelle carte ? "o" ou "oui" pour piocher
# > oui
# Votre score est de 16, la banque a 17.
# Souhaitez-vous une nouvelle carte ? "o" ou "oui" pour piocher
# > oui
# Votre score est de 19, la banque a 17.
# Souhaitez-vous une nouvelle carte ? "o" ou "oui" pour piocher
# > non
# Félicitations, vous avez plus de points que la banque, WINNER !

from black_jack import score_pioche_banque, pioche_carte_joueur
from croupier import etat_de_jeu, message_fin_de_jeu

score_banque = score_pioche_banque()
score_joueur = 0
veut_piocher = True

while veut_piocher:
    choix_joueur = input("Souhaitez-vous une nouvelle carte ? 'o' ou 'oui' pour piocher : ")
    if choix_joueur == 'oui' or choix_joueur == 'o':
        score_joueur += pioche_carte_joueur()
        etat_de_jeu(score_banque, score_joueur)
    elif choix_joueur == 'non' or choix_joueur == 'n':
        veut_piocher = False
    else:
        print("Je n'ai pas compris votre réponse...")

message_fin_de_jeu(score_banque, score_joueur)
