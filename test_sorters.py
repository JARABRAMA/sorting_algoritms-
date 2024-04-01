from unittest import TestCase

from sorters import Sorters


class Test(TestCase):
    x: list[int] = [3, 9, 8, 2, 1, 6, 4, 5, 7]
    orderedList: int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_selection_sort(self):
        print(Sorters.selection_sort(self.x))
        self.assertEqual(Sorters.selection_sort(self.x), self.orderedList)

    def test_insertion_sort(self):
        print(Sorters.insertion_sort(self.x))
        self.assertEqual(Sorters.selection_sort(self.x), self.orderedList)

