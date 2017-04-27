import unittest

from src.car import logic

class TestCarLogic(unittest.TestCase):

    def test_calculate_speed_adds_to_current(self):
        speed = logic.calculate_speed(2, 4, -1)
        self.assertEqual(speed, 5)

    def test_sets_upper_bound(self):
        speed = logic.calculate_speed(5, 10, 0)
        self.assertEqual(speed, 10)

    def test_sets_lower_bound(self):
        speed = logic.calculate_speed(5, 0, -10)
        self.assertEqual(speed, 0)


