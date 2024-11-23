import unittest
from solution import strict


@strict
def fbool(a: bool):
    return a


@strict
def fint(a: int):
    return a


@strict
def ffloat(a: float):
    return a


@strict
def fstr(a: str):
    return a


@strict
def empty():
    return 1


@strict
def func(a: int, b: str, c: float, d: bool):
    return 1


class CheckStrict(unittest.TestCase):
    def test_bool(self):
        self.assertRaises(TypeError, fbool, 1)
        self.assertEqual(fbool(True), True)

    def test_int(self):
        self.assertRaises(TypeError, fint, "123")
        self.assertEqual(fint(1), 1)

    def test_float(self):
        self.assertRaises(TypeError, ffloat, "123")
        self.assertEqual(ffloat(1.5), 1.5)

    def test_str(self):
        self.assertRaises(TypeError, fstr, 3333)
        self.assertEqual(fstr("123"), "123")

    def test_empty(self):
        self.assertEqual(empty(), 1)

    def test_many_args(self):
        self.assertRaises(TypeError, func, 1, "333", 1.0, 1)
        self.assertEqual(func(1, "1", 1.0, True), 1)

    def test_named_pass(self):
        self.assertRaises(TypeError, func, c="555", b="333", d=True, a=1)
        self.assertEqual(func(c=1.0, d=True, b="1", a=1), 1)

    def test_args_and_kwargs(self):
        self.assertRaises(TypeError, func, 1, "333", d=True, c="555")
        self.assertEqual(func(1, "1", c=1.0, d=True), 1)


if __name__ == "__main__":
    unittest.main()
