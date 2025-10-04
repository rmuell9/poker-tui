class Card:
    suits = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
    ranks = {"Ace": "A", "Two": "2", "Three": "3", "Four": "4", "Five": "5", "Six": "6", "Seven": "7", "Eight":"8", "Nine": "9", "Ten":"10", "Jack":"J", "Queen": "Q", "King": "K"}
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.ranks[self.rank].isdigit():
            return int(self.ranks[self.rank])
        values = {"A": {"low": 1, "high": 14}, "J": 11, "Q": 12, "K":13}
        return values[self.ranks[self.rank]]

    def __eq__(self, other):
        return self.get_value() == other.get_value()

    def __repr__(self):
        return f"{self.rank} of {self.suit} {self.suits[self.suit]}"

