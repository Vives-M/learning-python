numeric_cards = [list(range(2,11)), '2', '3', '4', '5', '6', '7', '8', '9', '10']
face_cards = ["J", "Q", "K"]
ace_card = ["A"]
cards =  numeric_cards + face_cards + ace_card

def value_of_card(card):
    if card in numeric_cards:
        print(f"{card} : It is a real card and it brings {card} points !")
        return int(card)
    elif card == "A":
        print(f"{card} : It is a real card and it brings {1} point !")
        return 1
    elif card in face_cards:
        print(f"{card} : It is a real card and it brings {10} points !")
        return 10
    else:
        print(f"{card} : This is not a real card !")


print(value_of_card('2'))
