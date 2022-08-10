import unittest
from calculate_lbtt import calcultate_lbtt_previous_buyer

class TestLBTT_PreviousBuyer(unittest.TestCase):
    def test_band_one(self):
        self.assertEqual(calcultate_lbtt_previous_buyer(100000), 0)

    def test_band_two(self):
        self.assertEqual(calcultate_lbtt_previous_buyer(200000), 1100)

    def test_band_three(self):
        self.assertEqual(calcultate_lbtt_previous_buyer(300000), 4600)

    def test_band_four(self):
        self.assertEqual(calcultate_lbtt_previous_buyer(400000), 13350)

    def test_band_five(self):
        self.assertEqual(calcultate_lbtt_previous_buyer(800000),54350)



if __name__ =='__main__':
    unittest.main()