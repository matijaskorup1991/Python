import unittest


# def multiply(a, b):
#     return a * b

# def multiply(a, b):
#     return a + b


def divisible_by(a, b):
    return a % b == 0


class TestMultiply(unittest.TestCase):
    # def test_multiply(self):
    #     test_x = 5
    #     text_y = 10
    #     self.assertEqual(multiply(test_x, text_y), 50, "should be 50")

    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 2))
        self.assertFalse(divisible_by(10, 3))


if __name__ == '__main__':
    unittest.main()
