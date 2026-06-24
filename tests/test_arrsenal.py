import unittest
from Datrax import arrsenal


class TestArrsenal(unittest.TestCase):

    # sumup
    def test_sumup_normal(self):
        self.assertEqual(arrsenal.sumup([1, 2, 3]), 6)

    def test_sumup_empty(self):
        with self.assertRaises(ValueError):
            arrsenal.sumup([])

    # maxout
    def test_maxout_normal(self):
        self.assertEqual(arrsenal.maxout([1, 9, 3]), 9)

    def test_maxout_empty(self):
        with self.assertRaises(ValueError):
            arrsenal.maxout([])

    # minout
    def test_minout_normal(self):
        self.assertEqual(arrsenal.minout([1, 9, -3]), -3)

    def test_minout_empty(self):
        with self.assertRaises(ValueError):
            arrsenal.minout([])

    # fliparr
    def test_fliparr(self):
        self.assertEqual(arrsenal.fliparr([1, 2, 3]), [3, 2, 1])

    # uniqarr
    def test_uniqarr(self):
        self.assertEqual(arrsenal.uniqarr([1, 1, 2, 2, 3]), [1, 2, 3])

    # ascend
    def test_ascend(self):
        self.assertEqual(arrsenal.ascend([3, 1, 2]), [1, 2, 3])

    # descend
    def test_descend(self):
        self.assertEqual(arrsenal.descend([1, 3, 2]), [3, 2, 1])

    # locate
    def test_locate_found(self):
        self.assertEqual(arrsenal.locate([1, 2, 3], 2), 1)

    def test_locate_not_found(self):
        self.assertEqual(arrsenal.locate([1, 2, 3], 5), -1)

    # freq
    def test_freq(self):
        self.assertEqual(arrsenal.freq([1, 2, 2, 3], 2), 2)

    # mergearr
    def test_mergearr(self):
        self.assertEqual(arrsenal.mergearr([1, 2], [3, 4]), [1, 2, 3, 4])

    # cutarr
    def test_cutarr(self):
        self.assertEqual(arrsenal.cutarr([1, 2, 3, 4, 5], 1, 4), [2, 3, 4])

    def test_cutarr_with_step(self):
        self.assertEqual(arrsenal.cutarr([1, 2, 3, 4, 5], 0, 5, 2), [1, 3, 5])

    # rotarr
    def test_rotarr(self):
        self.assertEqual(arrsenal.rotarr([1, 2, 3, 4], 2), [3, 4, 1, 2])

    def test_rotarr_large_k(self):
        self.assertEqual(arrsenal.rotarr([1, 2, 3], 5), [2, 3, 1])

    # inject
    def test_inject_middle(self):
        self.assertEqual(arrsenal.inject([1, 2, 3], 1, 99), [1, 99, 2, 3])

    def test_inject_end(self):
        self.assertEqual(arrsenal.inject([1, 2, 3], 5, 99), [1, 2, 3, 99])

    # zapval
    def test_zapval(self):
        self.assertEqual(arrsenal.zapval([1, 2, 2, 3], 2), [1, 3])

    # zapindex
    def test_zapindex(self):
        self.assertEqual(arrsenal.zapindex([1, 2, 3], 1), [1, 3])


if __name__ == "__main__":
    unittest.main()
