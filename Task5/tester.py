import unittest
import modules

class TestModules(unittest.TestCase):

    def test_factor(self):
        self.assertEqual(modules.factors(18), [1,2,3,6,9,18])
        self.assertEqual(modules.factors(15), [1,3,5,15])
        self.assertEqual(modules.factors(10), [1,2,5,10])
    def test_prime_true(self):
        self.assertTrue(modules.is_prime(5) is True)
        self.assertTrue(modules.is_prime(10) is False)
        self.assertTrue(modules.is_prime(3) is True)
    def test_vovels(self):
        self.assertEqual(modules.vowels("A Buttercups"),['A','u','e','u'])
        self.assertEqual(modules.vowels("For The Emperor"),['o','e','E','e','o'])
        self.assertEqual(modules.vowels("Battleship"),['a','e','i'])
    def test_len(self):
        self.assertEqual(len("A Random Text !"),15)
        self.assertEqual(len("For those we cherish, we die in glory!"),38)
        self.assertEqual(len("Knowledge is power, guard it well."),34)

if __name__ == '__main__':
    unittest.main()
