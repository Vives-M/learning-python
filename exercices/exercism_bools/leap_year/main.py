"""
Fonction pour savoir si une année est bisextile selon le calendrier gregorien.
Pour comprendre comment fonctionne le système des années bisextiles : https://www.youtube.com/watch?v=xX96xng7sAE
Rappel : année bissextile :
    - divisible par 4 et pas par 100
    - divisible par 400
"""

def leap_year(year):
    """
    :param year: int - l'année que vous souhaitez tester
    :return: bool - True si l'année testée est bisextile
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    return False
