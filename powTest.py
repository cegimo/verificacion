import unittest
from main import Power


class TestPower(unittest.TestCase):

    def setUp(self):
        pass

    def test_power_calculation(self):
        self.assertEqual(Power.powerFunction(1, 1), 1)

    def test_fails_integers_and_caracters(self):
        self.assertRaises(TypeError, lambda: Power.powerFunction(2, 'a'))

    def test_input_just_ints(self):
        self.assertRaises(Exception, lambda: Power.powerFunction("hola", "pepito"))

    def test_fails_with_one_int(self):
        self.assertRaises(Exception, lambda: Power.powerFunction(1))

    def test_works_with_more_than_2_elements(self):
        try:
            Power.powerFunction(2 , 4, 3)
        except Exception:
            self.fail("powerFunction raised Exception unexpectedly!")

    def test_if_base_grater_than_ten(self):
        self.assertRaises(TypeError, lambda: Power.powerFunction(12, 2))

    def test_if_exponent_grater_than_four(self):
        self.assertRaises(TypeError, lambda: Power.powerFunction(2, 10))

    def test_if_base_grater_than_ten_and_exponent_grater_than_four(self):
        self.assertRaises(TypeError, lambda: Power.powerFunction(12, 8))

    def test_if_base_is_negative(self):
        self.assertRaises(TypeError, lambda: Power.powerfunction(-4, 2))

    def test_if_exponent_is_negative(self):
        self.assertRaises(TypeError, lambda: Power.powerfunction(2, -3))

    def test_if_base_and_exponent_are_negative(self):
        self.assertRaises(TypeError, lambda: Power.powerfunction(-3, -2))

if __name__ == '__main__':
    unittest.main()




