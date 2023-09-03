import functools


def sum_digits(num): # O(n) Time, O(n) Space
    # fill in
    if num  < 10:
        return num
    num_list = [int(i)  for i in  str(num)]
    
    total = sum(num_list)
    result = sum_digits(total)
    return result


















import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert sum_digits(1) == 1
        print("PASSED: `sum_digits(1)` should return `1`")

    def test_2(self):
        assert sum_digits(49) == 4
        print("PASSED: `sum_digits(49)` should return `4`")

    def test_3(self):
        assert sum_digits(439230) == 3
        print("PASSED: `sum_digits(439230)` should return `3`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")