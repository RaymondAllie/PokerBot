from card import Card
from hand import Hand

class Board:
    boardCards = []
    def __init__(self):
        self.boardCards = []
    
    def add(self, card : Card):
        self.boardCards.append(card)

    def printBoard(self):
        for card in self.boardCards:
            print(card.toString())
