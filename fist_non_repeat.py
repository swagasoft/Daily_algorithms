
def first_non_repeat(s): # O(n) time, O(n) space.
    # fill this in
    freq = {}
    
    for chr in s:
        if freq.get(chr):
            freq[chr] += 1
        else:
            freq[chr] =  1
            
    for chr in s:
        if(freq[chr] == 1):
            return chr

    return ""


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert first_non_repeat("") == ""
        print("PASSED: first_non_repeat('') should return ''")

    def test_2(self):
        assert first_non_repeat("a") == "a"
        print("PASSED: first_non_repeat('a') should return 'a'")

    def test_3(self):
        assert first_non_repeat("oh my god dude where is my car") == "g"
        print(
            "PASSED: first_non_repeat('oh my god dude where is my car') should return 'g'"
        )

    def test_4(self):
        assert first_non_repeat("asdfsdafdasfjdfsafnnunlfdffvxcvsfansd") == "j"
        print(
            "PASSED: first_non_repeat('asdfsdafdasfjdfsafnnunlfdffvxcvsfansd') should return 'j'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")