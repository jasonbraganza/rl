from random import choice


class noMoreCards(Exception):
    pass


class cannotSetCard(Exception):
    pass


class CardDeck:
    def __init__(self):
        suits = "DCSH"
        faces = "A23456789JQK"
        self.cards = []
        for one_suit in suits:
            for one_face in faces:
                self.cards.append((one_suit, one_face))
        self.used_cards = []

    @property
    def card(self):
        if not self.cards:
            raise noMoreCards("you have no more cards")
        one_card = choice(self.cards)
        self.used_cards.append(one_card)
        self.cards.remove(one_card)
        return one_card


def main():
    myDeck = CardDeck()
    for i in range(53):
        print((myDeck.card))


if __name__ == "__main__":
    main()
