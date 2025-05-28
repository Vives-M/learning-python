"""
Bob est un adolescent apathique. Quand quelqu'un lui parle, ses réponses sont limitées.
"""
def response(hey_bob):
    """
    Cette fonction définit les réponses de Bob.
    :param hey_bob: string - phrase adressée à Bob.
    :return: string - réponse de Bob à la phrase donnée.
    Réponses possibles :
    - "Sure." -> Réponse à une question. Par convention, les questions finissent avec un "?".
    - "Whoa, chill out!" -> Réponse si on lui CRIE DESSUS. La convention pour les cris est l'utilisation des MAJUSCULES.
    - "Calm down, I know what I'm doing!" -> Réponse si on lui crie une question.
    - "Fine. Be that way!" -> Réponse au silence. Par convention, le silence c'est si l'on envoie rien ou une suite d'espaces.
    - "Whatever." -> Réponse à quoi que soit d'autre.
    """
    if hey_bob.strip().endswith('?') and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith('?'):
        return "Sure."
    elif hey_bob.isupper() :
        return "Whoa, chill out!"
    elif hey_bob == "" or hey_bob.strip() == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
