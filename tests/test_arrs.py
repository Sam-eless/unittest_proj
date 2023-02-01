from utils import arrs
import unittest


class TestGet(unittest.TestCase):
    def test_get(self):
        self.assertEqual((arrs.get([1, 2, 3], 1, "test")), 2)
        self.assertEqual((arrs.get([], -1, "test")), "test")

    def test_slice(self):
        self.assertTrue(arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3])
        self.assertTrue(arrs.my_slice([1, 2, 3], 1) == [2, 3])
        self.assertTrue(arrs.my_slice([], 3) == [])
        self.assertTrue(arrs.my_slice([1, 2, 3], -1) == [3])
        self.assertTrue(arrs.my_slice([1, 2, 3], -4) == [1, 2, 3])
