import random

class Card:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    @classmethod
    def create_deck(cls):
        '''
        deck_list = []
        for suit in Card.suits:
            for value in Card.values:
                deck_list.append(Card(suit, value))
        '''

        deck_list = [Card(suit, value) for suit in Card.suits for value in Card.values]
        return deck_list

    def __init__(self):
        self.cards = Deck.create_deck()

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        dealt = []
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        elif num > len(self.cards):
            for i in range(0, len(self.cards)):
                dealt.append(self.cards.pop(0))
        else:
            for i in range(0, num):
                dealt.append(self.cards.pop(0))
        return dealt

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)
        return self.cards

    def deal_card(self):
        card = self._deal(1)[0]
        return card

    def deal_hand(self, num):
        hand = self._deal(num)
        return hand


'''
deck = Deck()
print(deck)
deck.shuffle()
print(deck.deal_card())
print(deck)
print(deck.deal_hand(5))
print(deck)
#deck.shuffle() #should cause error, can't shuffle less than full deck
hand = deck.deal_hand(47)
print(hand)
print(len(hand))
print(deck)
print(deck.deal_card()) #should cause error, no cards left
print(deck)
'''