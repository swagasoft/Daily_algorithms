import re


def reverse_only_alpha(s): #O(n) time,  O(n) Space
    # fill in
    
    chr_list = [c for c in s if c.isalpha()]
    reversed_chr = reverse_array(chr_list)
    result = []
    char_index = 0
    
    for c in s:
        if c.isalpha():
            result.append(reversed_chr[char_index])
            char_index += 1
        else:
            result.append(c)
    
    return "".join(result)


def reverse_array(arr):
    return arr[::-1]











import unittest



class Test(unittest.TestCase):
    def test_1(self):
        assert callable(reverse_only_alpha) == True
        print("PASSED: Expect reverse_only_alpha is a function")

    def test_2(self):
        assert reverse_only_alpha("sea!$hells3") == "sll!$ehaes3"
        print(
            "PASSED: Expect reverse_only_alpha('sea!$hells3') to return 'sll!$ehaes3'"
        )

    def test_3(self):
        assert reverse_only_alpha("1kas90jda3") == "1adj90sak3"
        print("PASSED: Expect reverse_only_alpha('1kas90jda3') to return '1adj90sak3'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")