def missing_in_unsorted(arr, lowerBound, upperBound):
    # fill in
    total =  cal_total_sum(lowerBound, upperBound)
    tempt_total = 0
    
    for num  in arr:
        tempt_total += num

    return total - tempt_total
    
def cal_total_sum(low, upper) -> int:
    total = 0
    while low <= upper:
        total += low
        low += 1
    return total



import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert missing_in_unsorted([2, 5, 1, 4, 9, 6, 3, 7], 1, 9) == 8
        print(
            "PASSED: `missing_in_unsorted([ 2, 5, 1, 4, 9, 6, 3, 7 ], 1, 9)` should return `8`"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 1/1 tests passed!")
