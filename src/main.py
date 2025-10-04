from card import Card

test = Card("Hearts", "Five")
print(test)
print(test.get_value())
test2 = Card("Spades", "Ace")
print(test2)
print(test2.get_value())
test3 = Card("Diamonds", "Jack")
print(test3)
print(test3.get_value())
test4 = Card("Hearts", "Jack")
print(test4 == test3)
print(test4 == test)
