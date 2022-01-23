import unittest 
from cats_and_cheese import balanced_symbols, cost_prorating, water_jugs

class TestCatsAndCheese(unittest.TestCase):
    
    # Challenge 1
    def test_balanced_symbols(self):
        self.assertEqual(balanced_symbols("({[()[]]})"), True)
        self.assertEqual(balanced_symbols("/* abcd /* efgh */ ijkl */"), False)
        self.assertEqual(balanced_symbols("/*"), False)
        self.assertEqual(balanced_symbols(""), True)
        self.assertEqual(balanced_symbols(), True)

    def test_balanced_symbols_returns_a_bool(self):
        self.assertIsInstance(balanced_symbols("({[()[]]})"), bool)
    
    def test_balanced_symbols_type_error(self):
        self.assertRaises(TypeError, balanced_symbols, 1)

    # Challenge 2
    def test_cost_prorating(self):
        self.assertEqual(cost_prorating(10, [2, 5]), [3, 7])
        self.assertEqual(cost_prorating(10, [1, 0]), [10, 0])
        self.assertEqual(cost_prorating(123, [1, 2, 3, 4, 5, 6]), [6, 12, 18, 23, 29, 35])
        self.assertEqual(cost_prorating(5, [0, 0, 1]), [0, 0, 5])
    
    def test_cost_prorating_returns_a_list(self):
        self.assertIsInstance(cost_prorating(10, [2, 5]), list)
    
    def test_cost_prorating_type_error(self):
        self.assertRaises(TypeError, cost_prorating, 1.0, [1])
        self.assertRaises(TypeError, cost_prorating, 1, "hi")
        self.assertRaises(TypeError, cost_prorating, 1, [1.0])
    
    def test_cost_prorating_value_error(self):
        self.assertRaises(ValueError, cost_prorating, -1, [1])
        self.assertRaises(ValueError, cost_prorating, 1, [])
        self.assertRaises(ValueError, cost_prorating, 1, [-1])
        self.assertRaises(ValueError, cost_prorating, 1, [0])

    # Challenge 3
    def test_water_jugs(self):
        self.assertEqual(water_jugs(4, [3, 5]), '-1 -> 1 : (0, 5)\n1 -> 0 : (3, 2)\n0 -> -1 : (0, 2)\n1 -> 0 : (2, 0)\n-1 -> 1 : (2, 5)\n1 -> 0 : (3, 4)\n')
        self.assertEqual(water_jugs(15, [1, 2, 10, 20]), '-1 -> 3 : (0, 0, 0, 20)\n3 -> 0 : (1, 0, 0, 19)\n3 -> 1 : (1, 2, 0, 17)\n1 -> -1 : (1, 0, 0, 17)\n3 -> 1 : (1, 2, 0, 15)\n')
    
    def test_water_jugs_returns_a_str(self):
        self.assertIsInstance(water_jugs(4, [3, 5]), str)

    def test_water_jugs_type_error(self):
        self.assertRaises(TypeError, water_jugs, "hi", [1])
        self.assertRaises(TypeError, water_jugs, 1, 1)
        self.assertRaises(TypeError, water_jugs, 1, [1.0, "hi"])
    
    def test_water_jugs_value_error(self):
        self.assertRaises(ValueError, water_jugs, -1, [1])
        self.assertRaises(ValueError, water_jugs, 1, [])
        self.assertRaises(ValueError, water_jugs, 1, [-1])


if __name__ == "__main__":
    unittest.main()