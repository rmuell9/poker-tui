class Hand():
    def __init__(self, cards = []):
        self.cards = cards

    def __repr__(self):
        return f"{self.cards[0]} and {self.cards[1]}"
