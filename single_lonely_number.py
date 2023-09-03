def lonely_number(numbers):# time O(n) time, O(n) Space
    # fill in
    lonely_number = None
    store_frq = {}
    
    
    for num in numbers:
        if(store_frq.get(num) != None):
            store_frq[num] += 1
        else:
            store_frq[num] = 1
            
    for key in store_frq:
        element = store_frq[key]
        if(element == 1):
            lonely_number = key
            
    
    return lonely_number









import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert lonely_number([4, 4, 6, 1, 3, 1, 3]) == 6
        print("PASSED: `lonely_number([4, 4, 6, 1, 3, 1, 3])` should return `6`")

    def test_2(self):
        assert lonely_number([3, 3, 9]) == 9
        print("PASSED: `lonely_number([3, 3, 9])` should return `9`")

    def test_3(self):
        assert callable(lonely_number) == True
        print("PASSED: `lonely_number` is a function")

    def test_4(self):
        assert lonely_number([3, 3, 9]) == 9
        print("PASSED: `lonely_number([1])` should return `1`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")