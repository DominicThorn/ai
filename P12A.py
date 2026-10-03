import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

deck = [rank + " of " + suit for suit in suits for rank in cards]

print("Original Deck: ")
print(deck)

random.shuffle(deck)

print("\nShuffled Deck:")
print(deck)