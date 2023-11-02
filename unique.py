def uniques(arr): # O(n) time, O(n) space
    # fill in
    store = {}
    result = []
    
    for num in arr:
        if store.get(num) == num:
            pass
        else:
            result.append(num)
            store[num] = num
    
    return result











import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert uniques(
            [8, 8, 15, 6, 19, 7, 12, 6, 6, 3, 13, 9, 15, 14, 1, 13, 4, 11, 16]
        ) == [8, 15, 6, 19, 7, 12, 3, 13, 9, 14, 1, 4, 11, 16]
        print(
            "PASSED: uniques([8,8,15,6,19,7,12,6,6,3,13,9,15,14,1,13,4,11,16]) should return [8,15,6,19,7,12,3,13,9,14,1,4,11,16]"
        )

    def test_2(self):
        assert uniques([12, 7, 2, 20, 20, 2, 15, 20, 2, 10, 12, 1]) == [
            12,
            7,
            2,
            20,
            15,
            10,
            1,
        ]
        print(
            "PASSED: uniques([12,7,2,20,20,2,15,20,2,10,12,1]) should return [12,7,2,20,15,10,1]"
        )

    def test_3(self):
        assert uniques(
            [6, 12, 5, 1, 4, 18, 10, 17, 10, 0, 1, 7, 6, 18, 11, 2, 15, 19]
        ) == [6, 12, 5, 1, 4, 18, 10, 17, 0, 7, 11, 2, 15, 19]
        print(
            "PASSED: uniques([6,12,5,1,4,18,10,17,10,0,1,7,6,18,11,2,15,19]) should return [6,12,5,1,4,18,10,17,0,7,11,2,15,19]"
        )

    def test_4(self):
        assert uniques(
            [9, 0, 11, 16, 19, 14, 7, 18, 10, 6, 0, 17, 12, 9, 12, 18, 0, 14, 17]
        ) == [9, 0, 11, 16, 19, 14, 7, 18, 10, 6, 17, 12]
        print(
            "PASSED: uniques([9,0,11,16,19,14,7,18,10,6,0,17,12,9,12,18,0,14,17]) should return [9,0,11,16,19,14,7,18,10,6,17,12]"
        )

    def test_5(self):
        assert uniques([5, 10, 3, 17, 9, 12, 19, 4, 16, 19, 7, 9, 7, 8, 10]) == [
            5,
            10,
            3,
            17,
            9,
            12,
            19,
            4,
            16,
            7,
            8,
        ]
        print(
            "PASSED: uniques([5,10,3,17,9,12,19,4,16,19,7,9,7,8,10]) should return [5,10,3,17,9,12,19,4,16,7,8]"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 5/5 tests passed!")