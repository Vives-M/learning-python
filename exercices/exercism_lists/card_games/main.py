"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    numbers = [number]
    next_numbers = [number +1, number +2]
    return numbers + next_numbers


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds_1.extend(rounds_2)
    return rounds_1


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return float(sum(hand) / len(hand))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_and_last_numbers_average = (hand[0] + hand[-1]) / 2
    middle_card_index = len(hand) // 2
    middle_card = hand[middle_card_index]

    return first_and_last_numbers_average == card_average(hand) or middle_card == card_average(hand)



def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    # odd_indexes = []
    # even_indexes = []
    # for number in hand :
    #     if number % 2 == 0 :
    #         even_indexes.append(number)
    #     else :
    #         odd_indexes.append(number)
    # sum_odd_indexes = sum(odd_indexes)
    # sum_even_indexes = sum(even_indexes)
    # if len(odd_indexes):
    #     average_odd_indexes = sum_odd_indexes / len(odd_indexes)
    # else:
    #     average_odd_indexes = 0
    # if len(even_indexes):
    #     average_even_indexes = sum_even_indexes / len(even_indexes)
    # else:
    #     average_even_indexes = 0

    # return average_even_indexes == average_odd_indexes or average_even_indexes == 0 or average_odd_indexes == 0

    odd_indexes = hand[0::2]
    even_indexes = hand[1::2]

    return card_average(odd_indexes) == card_average(even_indexes)

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
