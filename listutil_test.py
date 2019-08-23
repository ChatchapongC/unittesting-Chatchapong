import unittest
from listutil import unique


class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertEqual(['a'],unique(['a']))

    def test_empty_list(self):
        self.assertEqual([],unique([]))

    def test_same_item_list(self):
        self.assertEqual(['a','b','c'],unique(['a','b','a','c','b']))

    def test_nested_list(self):
        lst = [1, 'a', [1,'a'], [1,'a'], 'b', 2, 1]
        self.assertEqual([1, 'a', [1, 'a'], 'b', 2],unique(lst))

    def test_not_a_list_item(self):
        with self.assertRaises(TypeError):
            lst = unique(1)
