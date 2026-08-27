import unittest
from datrax import textsmith


class TestTextsmith(unittest.TestCase):

    def test_flipstr(self):
        self.assertEqual(textsmith.flipstr("abc"), "cba")
        self.assertEqual(textsmith.flipstr(""), "")

    def test_loudify(self):
        self.assertEqual(textsmith.loudify("abcXYZ"), "ABCXYZ")
        self.assertEqual(textsmith.loudify("123"), "123")

    def test_softify(self):
        self.assertEqual(textsmith.softify("ABCxyz"), "abcxyz")
        self.assertEqual(textsmith.softify("HELLO123"), "hello123")

    def test_vowcount(self):
        self.assertEqual(textsmith.vowcount("aeiouAEIOU"), 10)
        self.assertEqual(textsmith.vowcount("xyz"), 0)

    def test_conscount(self):
        self.assertEqual(textsmith.conscount("abcXYZ"), 5)
        self.assertEqual(textsmith.conscount("aeiou"), 0)

    def test_ispali(self):
        self.assertTrue(textsmith.ispali("madam"))
        self.assertFalse(textsmith.ispali("hello"))
        self.assertTrue(textsmith.ispali(""))

    def test_wordcount(self):
        self.assertEqual(textsmith.wordcount("hello world"), 2)
        self.assertEqual(textsmith.wordcount("   spaced   out  "), 2)
        self.assertEqual(textsmith.wordcount(""), 0)

    def test_charfreq(self):
        self.assertEqual(textsmith.charfreq("aab"), {"a": 2, "b": 1})
        self.assertEqual(textsmith.charfreq(""), {})

    def test_trimspace(self):
        self.assertEqual(textsmith.trimspace("   hello  "), "hello")
        self.assertEqual(textsmith.trimspace(""), "")

    def test_swapstr(self):
        self.assertEqual(textsmith.swapstr("AbC"), "aBc")
        self.assertEqual(textsmith.swapstr("123"), "123")

    def test_findstr(self):
        self.assertEqual(textsmith.findstr("hello", "lo"), 3)
        self.assertEqual(textsmith.findstr("hello", "world"), -1)
        self.assertEqual(textsmith.findstr("abc", ""), 0)

    def test_splitstr(self):
        self.assertEqual(textsmith.splitstr("a b  c"), ["a", "b", "c"])
        self.assertEqual(textsmith.splitstr(""), [])

    def test_joinstr(self):
        self.assertEqual(textsmith.joinstr(["a", "b", "c"]), "a b c")
        self.assertEqual(textsmith.joinstr([], ","), "")
        self.assertEqual(textsmith.joinstr(["a", "b"], "-"), "a-b")

    def test_capfirst(self):
        self.assertEqual(textsmith.capfirst("hello"), "Hello")
        self.assertEqual(textsmith.capfirst("Hello"), "Hello")
        self.assertEqual(textsmith.capfirst(""), "")

    def test_titlefy(self):
        self.assertEqual(textsmith.titlefy("hello world"), "Hello World")
        self.assertEqual(textsmith.titlefy("HELLO WORLD"), "HELLO WORLD")
        self.assertEqual(textsmith.titlefy(""), "")


if __name__ == '__main__':
    unittest.main()
