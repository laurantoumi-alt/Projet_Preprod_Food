import unittest
from food import Food


class TestFood(unittest.TestCase):
    """ class test food """

    def test_get_name(self):
        """ test_get_name """
        print('test_get_name')
        food_one = Food()
        food_two = Food()

        food_two.set_name('coconut')

        self.assertEqual(food_one.get_name(), None)
        self.assertEqual(food_two.get_name(), 'coconut')

    def test_is_fat(self):
        """ test_is_fat """
        print('test_is_fat')

        # Aliment gras (beurre ~81g de graisses/100g)
        butter = Food()
        butter.set_name('butter')
        butter.set_fat(81.0)
        self.assertTrue(butter.is_fat())

        # Aliment pas gras (pomme ~0.2g de graisses/100g)
        apple = Food()
        apple.set_name('apple')
        apple.set_fat(0.2)
        self.assertFalse(apple.is_fat())

        # Exactement au seuil (20g) — pas considéré comme gras
        neutral = Food()
        neutral.set_name('neutral')
        neutral.set_fat(20.0)
        self.assertFalse(neutral.is_fat())


if __name__ == '__main__':
    unittest.main()
