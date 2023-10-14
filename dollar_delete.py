def is_dollar_delete_equal(arr):
    # fill in
    for idx, word in enumerate(arr): # O(m * n^2) Time, O(1) space
        helperFunction(word, idx, arr)
        
    first_word = arr[0]
    for word in arr:
        if first_word != word:
            return False
    return True



def helperFunction(word, idx, arr): #O(n ^2)time, O(1)space
    for i, chr in enumerate(word):
        if chr == '$':  
            new_word = word[i+ 1 :] #$abd n(n)
            arr[idx] = new_word
        else:
            pass





import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert is_dollar_delete_equal(["f$ec", "ec"]) == True
        print("PASSED: `['f$ec', 'ec']` should return `true`")

    def test_2(self):
        assert is_dollar_delete_equal(["a90$n$c$se", "a90n$cse"]) == False
        print("PASSED: `['a90$n$c$se', 'a90n$cse']` should return `false`")

    def test_3(self):
        assert is_dollar_delete_equal(["ab$$", "c$d$"]) == True
        print("PASSED: `['ab$$', 'c$d$']` should return `true`")

    def test_4(self):
        assert is_dollar_delete_equal(["b$$p", "$b$p"]) == True
        print("PASSED: `['b$$p', '$b$p']` should return `true`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")