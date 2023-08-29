
def is_anagram(str1, str2): # O(n) time, O(n) space 
    ## fill this in
    str_lst1 = list(str1.lower())
    str_lst2 = list(str2.lower())
    
    str_lst1.sort()
    str_lst2.sort() 
    


    return str_lst1 == str_lst2














import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert is_anagram("Mary", "Army") == True
        print("PASSED: is_anagram('Mary', 'Army') should return False")

    def test_2(self):
        assert is_anagram("cinema", "iceman") == True
        print("PASSED: is_anagram('cinema', 'iceman') should return True")

    def test_3(self):
        assert is_anagram("jake", "jay") == False
        print("PASSED: is_anagram('jake', 'jay') should return False")
        
    def test_4(self):
        assert is_anagram("", "jay") == False
        print("PASSED: is_anagram('jake', 'jay') should return False")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
