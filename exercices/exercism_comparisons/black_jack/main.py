numeric_cards = [list(range(2,11)), '2', '3', '4', '5', '6', '7', '8', '9', '10']
face_cards = ["J", "Q", "K"]
ace_card = ["A"]
cards =  numeric_cards + face_cards + ace_card

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in numeric_cards:
        # print(f"{card} : It is a real card and it brings {card} points !")
        return int(card)
    elif card == "A":
        # print(f"{card} : It is a real card and it brings {1} point !")
        return 1
    elif card in face_cards:
        # print(f"{card} : It is a real card and it brings {10} points !")
        return 10
    raise ValueError("This is not a real card !")

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    """
    if card_one in cards and card_two in cards:
        value_of_card_one = value_of_card(card_one)
        value_of_card_two = value_of_card(card_two)
        if value_of_card_one == value_of_card_two:
            return card_one, card_two
        elif value_of_card_one > value_of_card_two:
            return card_one
        return card_two
    raise ValueError("This is not a real card !")

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    """
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        return 1
    elif (value_of_card_one + value_of_card_two) <= 10:
        return 11
    return 1


# print(value_of_card('2'))
# print(higher_card("J", "10"))
