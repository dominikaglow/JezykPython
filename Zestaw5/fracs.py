import unittest

def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a)

def add_frac(frac1, frac2):
    res =[]
    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    gcdNum = gcd(licz, mian)
    res = [int(licz/gcdNum), int(mian/gcdNum)]
    return res

def sub_frac(frac1, frac2):
    res = []
    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    gcdNum = abs(gcd(licz, mian))
    res = [int(licz / gcdNum), int(mian / gcdNum)]
    return res

def mul_frac(frac1, frac2):
    res = []
    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[0]
    gcdNum = abs(gcd(licz, mian))
    res = [int(licz / gcdNum), int(mian / gcdNum)]
    return res

def div_frac(frac1, frac2):
    res = []
    mian = frac1[1] * frac2[0]
    licz = frac1[0] * frac2[1]
    gcdNum = abs(gcd(licz, mian))
    res = [int(licz / gcdNum), int(mian / gcdNum)]
    return res

def is_positive(frac):
    if frac[0] >= 0:
        return True
    else:
        return False

def is_zero(frac):
    gcdNum = abs(gcd(frac[0], frac[1]))
    frac[0] = int(frac[0] / gcdNum)
    frac[1] = int(frac[1] / gcdNum)
    if frac[0] == 0:
        return True
    else:
        return False

def frac2float(frac):
    res = frac[0] / frac[1]
    res = round(res, 2)
    return res

def cmp_frac(frac1, frac2):
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

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [14, 8]), [-5, 4])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([5, 15]), 0.33)

    def tearDown(self):
        super(TestFractions, self).tearDown()

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy