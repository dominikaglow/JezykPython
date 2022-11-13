import unittest

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def negDenom(frac):
    frac[0] = - frac[0]
    frac[1] = abs(frac[1])
    return frac

def add_frac(frac1, frac2):
    res = []

    if frac1[1] < 0:
        frac1 = negDenom(frac1)
    if frac2[1] < 0:
        frac2 = negDenom(frac2)

    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    gcdNum = gcd(licz, mian)
    res = [licz//gcdNum, mian//gcdNum]
    return res

def sub_frac(frac1, frac2):
    res = []

    if frac1[1] < 0:
        frac1 = negDenom(frac1)
    if frac2[1] < 0:
        frac2 = negDenom(frac2)

    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    gcdNum = abs(gcd(licz, mian))
    res = [licz//gcdNum, mian//gcdNum]
    return res

def mul_frac(frac1, frac2):
    res = []

    if frac1[1] < 0:
        frac1 = negDenom(frac1)
    if frac2[1] < 0:
        frac2 = negDenom(frac2)

    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[0]
    gcdNum = abs(gcd(licz, mian))
    res = [licz//gcdNum, mian//gcdNum]
    return res


def div_frac(frac1, frac2):
    res = []

    if frac1[1] < 0:
        frac1 = negDenom(frac1)
    if frac2[1] < 0:
        frac2 = negDenom(frac2)

    mian = frac1[1] * frac2[0]
    licz = frac1[0] * frac2[1]
    gcdNum = abs(gcd(licz, mian))
    res = [licz//gcdNum, mian//gcdNum]

    if res[0] < 0 and res[1] < 0:
        res[0] = abs(res[0])
        res[1] = abs(res[1])
    return res

def is_positive(frac):
    if frac[0] >= 0:
        return True
    else:
        return False

def is_zero(frac):
    gcdNum = abs(gcd(frac[0], frac[1]))
    frac[0] = frac[0]//gcdNum
    frac[1] = frac[1]//gcdNum

    if frac[0] == 0:
        return True
    else:
        return False

def frac2float(frac):
    res = round((frac[0] / frac[1]), 2)
    return res

def cmp_frac(frac1, frac2):
    if frac1[1] < 0:
        frac1 = negDenom(frac1)
    if frac2[1] < 0:
        frac2 = negDenom(frac2)

    f1 = frac2float(frac1)
    f2 = frac2float(frac2)

    if f1 > f2:
        return 1
    elif f1 == f2:
        return 0
    else:
        return -1


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 35], [51, 11]), [1796, 385])
        self.assertEqual(add_frac([-1, -35], [51, -11]), [1774, -385])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [14, 8]), [-5, 4])
        self.assertEqual(sub_frac([1, 2], [0, 8]), [1, 2])
        self.assertEqual(sub_frac([17, 2], [1, 3]), [49, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([1, 2], [1, -3]), [-1, 6])
        self.assertEqual(mul_frac([-1, 12], [1, -3]), [1, 36])
        self.assertEqual(div_frac([-1, 21], [1, -3]), [1, 7])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([-1, 21], [1, -3]), [1, 7])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([0, 2]), True)
        self.assertEqual(is_positive([1, 2]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([0, -10]), True)
        self.assertEqual(is_zero([1, -10]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 7], [1, 7]), 0)
        self.assertEqual(cmp_frac([2, 5], [8, 5]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([5, 15]), 0.33)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy