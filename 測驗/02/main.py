from Obj import *


def is_Flush(cards):
    # 確認是否同花色
    for card in cards[1:]:
        if not isinstance(card, type(cards[0])):
            return False
    return True


def is_StraightFlush(cards):
    return is_Straight(cards) and is_Flush(cards)


def is_FullHouse(cards):
    cards = [card.rank for card in cards]
    chker = 0
    for card in cards:
        chker += cards.count(card)
    if chker == 13:
        return True
    return False


def is_FourOfAKind(cards):
    cards = [card.rank for card in cards]
    for card in cards:
        if cards.count(card) == 4:
            return True
    return False



test_data = {
    'Straight': [
        Spades(Card.RANK['A']),
        Diamond(Card.RANK['5']),
        Spades(Card.RANK['3']),
        Club(Card.RANK['4']),
        Heart(Card.RANK['2'])
    ],

    'Flush': [
        Diamond(Card.RANK['8']),
        Diamond(Card.RANK['5']),
        Diamond(Card.RANK['3']),
        Diamond(Card.RANK['10']),
        Diamond(Card.RANK['2'])
    ],

    'StraightFlush': [
        Spades(Card.RANK['A']),
        Spades(Card.RANK['5']),
        Spades(Card.RANK['3']),
        Spades(Card.RANK['4']),
        Spades(Card.RANK['2'])
    ],

    'FourOfAKind': [
        Spades(Card.RANK['A']),
        Heart(Card.RANK['A']),
        Diamond(Card.RANK['A']),
        Club(Card.RANK['A']),
        Spades(Card.RANK['5']),
    ],

    'FullHouse': [
        Heart(Card.RANK['K']),
        Spades(Card.RANK['K']),
        Club(Card.RANK['K']),
        Club(Card.RANK['A']),
        Diamond(Card.RANK['A']),
    ],

    'Any': [
        Heart(Card.RANK['K']),
        Diamond(Card.RANK['A']),
        Spades(Card.RANK['5']),
        Diamond(Card.RANK['10']),
        Club(Card.RANK['4']),
    ]
}

# for k, v in test_data.items():
#     if is_StraightFlush(v):
#         print(k + ' is straight flush.')
#     elif is_FourOfAKind(v):
#         print(k + ' is four of a kind.')
#     elif is_FullHouse(v):
#         print(k + ' is full house.')
#     elif is_Flush(v):
#         print(k + ' is flush.')
#     elif is_Straight(v):
#         print(k + ' is straight.')
#     else:
#         print(k + ' is any unmatched')



def check_deck(cards):
    if is_StraightFlush(cards):
        return 5
    elif is_FourOfAKind(cards):
        return 4
    elif is_FullHouse(cards):
        return 3
    elif is_Flush(cards):
        return 2
    elif is_Straight(cards):
        return 1
    else:
        return 0

def find_better(cards1, cards2):
    if check_deck(cards1) > check_deck(cards2):
        print('winner : cards1')
    elif check_deck(cards1) < check_deck(cards2):
        print('winner : cards2')
    else:
        print('draw')


# for k, v in test_data.items():
#     print('{} = {}'.format(k, check_bigger(v)))


find_better(test_data['Straight'], test_data['FullHouse'])
find_better(test_data['FourOfAKind'], test_data['Any'])
find_better(test_data['Straight'], test_data['StraightFlush'])
find_better(test_data['FullHouse'], test_data['Flush'])
find_better(test_data['FourOfAKind'], test_data['StraightFlush'])
find_better(test_data['FullHouse'], test_data['FourOfAKind'])
