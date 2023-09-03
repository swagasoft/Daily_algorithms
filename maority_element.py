###
# @param {number[]} nums
# @return {number}
###
from math import floor


def majority_element(nums):# O(n) Time, O(n) Space
    # fill in
    store = {}
    topFreq = 0
    result_key = None
    
    for num in nums:
        if (store.get(num) != None):
            store[num] += 1
        else:
            store[num] = 1
            
    #check item with highest freq
    for key in store:
        val  =  store[key]
        if val >  topFreq:
            topFreq = val
            result_key = key
            
            
    return result_key


# print(majorityElement([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1]))







import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert callable(majority_element) == True
        print("PASSED: 'majority_element' is a function")

    def test_2(self):
        assert majority_element([1, 4, 2, 4, 4, 3, 4]) == 4
        print("PASSED: 'majority_element([1, 4, 2, 4, 4, 3, 4])' should return '4'")

    def test_3(self):
        assert majority_element([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1]) == 1
        print(
            "PASSED: 'majority_element([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1])' should return '1'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")