def calc_square_of_a_number(a, b):
    b = 2
    return a ** b


import unittest


class finding_a_square_of_a_number(unittest.TestCase):

    def test_the_numbers(self):
        result = calc_square_of_a_number(4, 2)
        self.assertEqual(result, 16)

if __name__ == "__main__":
    unittest.main()        
        



