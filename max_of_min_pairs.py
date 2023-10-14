def max_of_min_pairs(nums): # O(n) Time, O(1) space
    # fill in
    result = 0
    skip = False
    nums.sort()
    
    for idx in range(len(nums) - 1):
        if skip == True:
            skip = False
        else:
            result += nums[idx]
            skip =  True
        
    
    return result













import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert max_of_min_pairs([3, 4, 2, 5]) == 6
        print("PASSED: max_of_min_pairs([3, 4, 2, 5]) should return 6")

    def test_2(self):
        assert max_of_min_pairs([1, 3, 2, 6, 5, 4]) == 9
        print("PASSED: max_of_min_pairs([1, 3, 2, 6, 5, 4]) should return 9")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 2/2 tests passed!")