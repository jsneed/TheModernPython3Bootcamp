import unittest
from deck import Card 
from deck import Deck 

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_print_deck(self):
        self.assertEqual(self.deck.__repr__(), 'Deck of 52 cards')

    def test_count(self):
        """checks that an accurate count is returned"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.deal_card()
        self.assertEqual(self.deck.count(), 51)

    def test_shuffle(self):
        """checks that shuffle works as expected"""
        self.deck.shuffle()
        self.assertEqual(self.deck.count(), 52)
        self.deck.deal_card()
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_shuffle_random(self):
        """checks that shuffle works as expectedand gives a random first card"""
        self.deck.shuffle()
        card = self.deck.deal_card()
        self.assertNotEqual(Card("Hearts", "A"), card)

    def test_deal_card(self):
        """Check that only one card is dealt and it has a value and suit as expected"""
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

        card = self.deck.deal_card()
        self.assertEqual(self.deck.count(), 51)
        self.assertIn(card.suit, suits)
        self.assertIn(card.value, values)

        card = self.deck.deal_card()
        self.assertEqual(self.deck.count(), 50)
        self.assertIn(card.suit, suits)
        self.assertIn(card.value, values)

    def test_deal_hand(self):
        """check that the size of the hand dealt is as expected"""
        hand = self.deck.deal_hand(5)
        self.assertEqual(len(hand), 5)
        self.assertEqual(self.deck.count(), 47)
        for card in hand:
            self.assertIsInstance(card, Card)

        hand = self.deck.deal_hand(7)
        self.assertEqual(len(hand), 7)
        self.assertEqual(self.deck.count(), 40)

    def test_insufficient_cards(self):
        hand = self.deck.deal_hand(50)
        hand = self.deck.deal_hand(4)
        self.assertEqual(len(hand), 2)
        with self.assertRaises(ValueError):
            self.deck.deal_hand(1)




if __name__ == "__main__":
    unittest.main()

