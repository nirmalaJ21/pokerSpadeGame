import unittest
import Poker_Spade_Game


class TestCardGame(unittest.TestCase):
    #Test cases for checking staright sequence
    def test_check_straight(self):
        self.assertEqual(Poker_Spade_Game.check_straight('S10', 'S9', 'S8'), 10)
    def test_check_straight1(self):
        self.assertEqual(Poker_Spade_Game.check_straight('S9', 'S10', 'SJ'), 11)
    def test_check_straight2(self):
        self.assertEqual(Poker_Spade_Game.check_straight('S6', 'S7', 'S8'), 8)
    def test_check_straight3(self):
        self.assertEqual(Poker_Spade_Game.check_straight('SA', 'SK', 'SQ'), 14)
    #Test cases to check 3 of same kind if yes return value else 0
    def test_check_3ofa_kind(self):
        self.assertEqual(Poker_Spade_Game.check_3ofa_kind('S4', 'S4', 'S4'), 4)
    def test_check_3ofa_kind1(self):
        self.assertEqual(Poker_Spade_Game.check_3ofa_kind('S10', 'SJ', 'SJ'), 0)
    def test_check_3ofa_kind2(self):
        self.assertEqual(Poker_Spade_Game.check_3ofa_kind('S9', 'S9', 'SA'), 0)
    def test_check_3ofa_kind3(self):
        self.assertEqual(Poker_Spade_Game.check_3ofa_kind('SA', 'SA', 'SA'), 14)
    #Test cases for checking royal flush
    def test_check_royal_flush(self):
        self.assertEqual(Poker_Spade_Game.check_royal_flush('S10', 'SJ', 'SQ'), 0)
    def test_check_royal_flush1(self):
        self.assertEqual(Poker_Spade_Game.check_royal_flush('SA', 'SK', 'SQ'), 0)
    def test_check_royal_flush2(self):
        self.assertEqual(Poker_Spade_Game.check_royal_flush('SA', 'SK', 'SQ'), 14)

    #test cases for play cards
    def test_play_cards(self):
        self.assertEqual(Poker_Spade_Game.play_cards('SA', 'SK', 'SQ', 'SJ', 'S10', 'S9'), 1)
    def test_check_royal_flush2(self):
         self.assertEqual(Poker_Spade_Game.play_cards('S2', 'S3', 'S4', 'S5', 'S6', 'S7'), -1)
    def test_check_royal_flush2(self):
        self.assertEqual(Poker_Spade_Game.play_cards('S10', 'SJ', 'S9', 'SK', 'SJ', 'S10'), -1)
    def test_check_royal_flush2(self):
        self.assertEqual(Poker_Spade_Game.play_cards('SA', 'S10', 'S9', 'SK', 'SJ', 'SQ'), 0)


if __name__ == '__main__':
    unittest.main()

