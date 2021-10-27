import unittest

import mymodule

class TestMyModule(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mymodule.sumaNumeros(7,8),15)

    def test_rest(self):
        self.assertEqual(mymodule.restaNumeros(8,4),4)

if __name__=="__main__":
    unittest.main()