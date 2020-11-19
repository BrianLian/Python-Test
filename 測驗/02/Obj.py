class Card:
    RANK = {
        'A':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
        'J':11,
        'Q':12,
        'K':13,
    }

    def __init__(self, card_rank):
        self.rank = card_rank



class Spades(Card):
    pass

class Heart(Card):
    pass

class Diamond(Card):
    pass

class Club(Card):
    pass


def is_Straight(cards):
    cards = [card.rank for card in cards]
    # 確認是否為連號
    sorted_cards = sorted(cards)

    # 判斷是否重複(順子不會重複)
    chker = 0
    for card in cards:
        chker += cards.count(card)

    if not chker is 5 \
    or not (sorted_cards[0] == 1 \
    and sorted_cards[1] == 10 and sorted_cards[2] == 11 \
    and sorted_cards[3] == 12 and sorted_cards[4] == 13)\
    and not ((max(sorted_cards) - min(sorted_cards)) == (len(sorted_cards) -1)):
        return False
    return True