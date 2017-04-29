import unittest
import random
from mock import patch

from ts import RandomDecision

CHOICES = [
    {'weight': 30, 'hi': 'hello'},
    {'weight': 23, 'hi': 'bye'}
]


class TestRandomDecision(unittest.TestCase):

    def test_accumulates_all_the_weights_at_the_beginning(self):
        rd = RandomDecision(choices=CHOICES)
        self.assertIsNotNone(rd.weights)

    @patch.object(random, 'randint', return_value=5)
    def test_picks_random_number_applies_to_choice(self, randint):
        rd = RandomDecision(choices=CHOICES)
        choice = rd.choice()
        self.assertEqual(choice['hi'], 'hello')
        self.assertEqual(randint.call_count, 1)

