import unittest
import modules

class TestModules(unittest.TestCase):

    def test_factor(self):
        self.assertEqual(modules.factors(10), [2,5])
        self.assertEqual(modules.factors(15), [3,5])
        self.assertEqual(modules.factors(6), [2,3])
    def test_prime_true(self):
        self.assertTrue(modules.is_prime(5) is True)
        self.assertTrue(modules.is_prime(137) is True)
        self.assertTrue(modules.is_prime(3) is True)
    def test_prime_false(self):
        self.assertFalse(modules.is_prime(10) is True)
        self.assertFalse(modules.is_prime(2022) is True)
        self.assertFalse(modules.is_prime(7) is True)
    def test_vovels(self):
        self.assertEqual(modules.vowels("A Buttercups"),['A','u','e','u'])
        self.assertEqual(modules.vowels("For The Emperor"),['o','e','E','e','o'])
        self.assertEqual(modules.vowels("Battleship"),['a','e','i'])
    def test_len(self):
        self.assertEqual(len("A Random Text !"),15)
        self.assertEqual(len("For those we cherish, we die in glory!"),20)
        self.assertEqual(len("Knowledge is power, guard it well."),33)

if __name__ == '__main__':
    unittest.main()
