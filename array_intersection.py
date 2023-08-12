def intersection(nums1, nums2): # O(n + m) time, O(n * m)  space
    # fill this in
    result = []
    
    for num in nums1:
        for num2 in nums2:
            if num == num2:
                result.append(num)

    return result












import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert intersection([6, 0, 12, 10, 16], [3, 15, 18, 20, 15]) == []
        print(
            "PASSED: `intersection([6,0,12,10,16],[3,15,18,20,15])` should return `[]`"
        )

    def test_2(self):
        assert intersection([1, 5, 2, 12, 6], [13, 10, 9, 5, 8]) == [5]
        print("PASSED: `intersection([1,5,2,12,6],[13,10,9,5,8])` should return `[5]`")

    def test_3(self):
        assert intersection([3], [15]) == []
        print("PASSED: `intersection([3],[15])` should return `[]`")

    def test_4(self):
        assert intersection([2, 16, 8, 9], [14, 15, 2, 20]) == [2]
        print("PASSED: `intersection([2,16,8,9],[14,15,2,20])` should return `[2]`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
