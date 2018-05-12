from unittest import TestCase

from main import binarySearch


class TestBinarySearch(TestCase):
    def test_binarySearchFindsElementsInListWithEvenSize(self):
        size = 10
        for i in range(size):
            what = i
            where = range(size)

            foundIdx = binarySearch(where=where, what=what)

            self.assertEqual(foundIdx, where.index(what))

    def test_binarySearchFindsElementsInListWithOddSize(self):
        size = 9
        for i in range(size):
            what = i
            where = range(size)

            foundIdx = binarySearch(where=where, what=what)

            self.assertEqual(foundIdx, where.index(what))

    def test_binarySearchFindsElementsInListWithSizeOfOne(self):
        what = 1
        where = [1]

        foundIdx = binarySearch(where=where, what=what)

        self.assertEqual(foundIdx, where.index(what))

    def test_binarySearchReturnsNoneIfElementIsNotFound(self):
        what = 2
        where = [1]

        foundIdx = binarySearch(where=where, what=what)

        self.assertIsNone(foundIdx)
