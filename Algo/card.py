suits = {
    "H" : "Hearts",
    "D" : "Diamonds",
    "S" : "Spades",
    "C" : "Clubs"
}
values = { a + 2 : a + 2 for a in range(9)}
values["11"] = "Jack"
values["12"] = "Queen"
values["13"] = "King"
values["14"] = "Ace"

cardIDs = {}

for suit in suits.keys():
    for value in values.keys():
        cardIDs[suit + str(value)] = str(values[value]) + " of " + suits[suit]


class Card:
    cardIDs = cardIDs
    value : int # 2 - 14
    name : str # card name
    id: str # e.g H2 (2 of Hearts)
    def __init__(self, id):
        self.id = id
        self.name = cardIDs[id]
        self.value = id[1:]
    
    def toString(self):
        return self.name
