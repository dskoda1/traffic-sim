import unittest

from src.car import logic

class TestCarLogic(unittest.TestCase):

    def test_calculate_speed_adds_to_current(self):
        """adds forward and backward to current."""
        speed = logic.calculate_speed(2, 4, -1)
        self.assertEqual(speed, 5)

    def test_sets_upper_bound(self):
        """adds forward and backward to current."""
        speed = logic.calculate_speed('hello', 4, -1)
        self.assertEqual(speed, 5)


