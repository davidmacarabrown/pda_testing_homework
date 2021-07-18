import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card_1 = Card("spades", 1)
        self.card_2 = Card("clubs", 9)
        self.card_3 = Card("diamonds", 10)

    def test_check_for_ace__true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_1))

    def test_check_for_ace__false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_2))

    def test_highest_card__one(self):
        highest_card = self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(9, highest_card.value)

    def test_highest_card__two(self):
        highest_card = self.card_game.highest_card(self.card_2, self.card_3)
        self.assertEqual(10, highest_card.value)

    def test_cards_total__one(self):
        cards = [self.card_1, self.card_2]
        total = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 10", total)

    def test_cards_total__two(self):
        cards = [self.card_2, self.card_3]
        total = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 19", total)




        