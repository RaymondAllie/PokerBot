from card import Card

class Hand:
    cards : tuple
    def __init__(self, card1 : Card, card2 : Card):
        self.cards = (card1, card2)

