def power_of_three(num):
    # fill in
    
    if ( num % 3 == 0):
        return True
    else:
        return False














import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert power_of_three(9) == True
        print("PASSED: `power_of_three(9)` should be `True`")

    def test_2(self):
        assert power_of_three(7) == False
        print("PASSED: `power_of_three(7)` should be `False`")

    def test_3(self):
        assert power_of_three(729) == True
        print("PASSED: `power_of_three(729)` should be `True`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
