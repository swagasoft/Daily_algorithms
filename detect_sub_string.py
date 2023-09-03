def detectSubstring(txt, subStr): #O(n) Time, O(n) space
    # fill in
    txt_list = list(txt) # O(n) time
    sub_str_list = list(subStr) 
    scope = False
    counter = 0
    result = -1
    
    for idx, str in enumerate(txt_list):
        first_sub = sub_str_list[0]
        if str == first_sub:
            scope = True
            result = idx
            
        if scope == True:
            if str == sub_str_list[counter]:
                counter += 1
            else:
                scope = False
                result= - 1
                counter = 0
            if counter == len(sub_str_list) - 1:
                return result
    
    
    return result








import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert detectSubstring("thepigflewwow", "flew") == 6
        print("PASSED: `detectSubstring('thepigflewwow', 'flew')` should return `6`")

    def test_2(self):
        assert detectSubstring("twocanplay", "two") == 0
        print("PASSED: `detectSubstring('twocanplay', 'two')` should return `0`")

    def test_3(self):
        assert detectSubstring("wherearemyshorts", "pork") == -1
        print(
            "PASSED: `detectSubstring('wherearemyshorts', 'pork')` should return `-1`"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")