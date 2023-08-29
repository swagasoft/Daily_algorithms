
def is_palindrome(s): # O(n) time, O(n) space
    # fill in
    s = s.lower()
    str_list = list(s.replace(" ", ""))
    start = 0
    end = len(str_list) - 1
    
    while( start < end):
        elel1 =  str_list[start]
        elel2 =  str_list[end]
        
        if elel1 != elel2:
            return False
        else:
            start += 1
            end -= 1

    
    return True









import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert is_palindrome("A Santa Lived As a Devil At NASA") == True
        print(
            "PASSED: assert is_palindrome('A Santa Lived As a Devil At NASA') == True"
        )

    def test_2(self):
        assert is_palindrome("gold") == False
        print("PASSED: assert is_palindrome('gold') == False")

    def test_3(self):
        assert is_palindrome("a") == True
        print("PASSED: assert is_palindrome('a') == True")

    def test_4(self):
        assert is_palindrome("racecar") == True
        print("PASSED: assert is_palindrome('racecar') == True")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
