def reverse_string(str1): #O(n) Time and O(1)  space
    # fill this in
    str_list = list(str1)
    start = 0
    end =  len(str_list) - 1
    
    
    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1


    return "".join(str_list)














import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert reverse_string("njnschnjkdasn j32 uida") == "adiu 23j nsadkjnhcsnjn"
        print(
            "PASSED: reverse_string('njnschnjkdasn j32 uida') should return 'adiu 23j nsadkjnhcsnjn'"
        )

    def test_2(self):
        assert reverse_string("timbuktu12") == "21utkubmit"
        print("PASSED: reverse_string('timbuktu12') should return '21utkubmit'")

    def test_3(self):
        assert reverse_string("") == ""
        print("PASSED: reverse_string('') should return ''")

    def test_4(self):
        assert reverse_string("reverseastring") == "gnirtsaesrever"
        print("PASSED: reverse_string('reverseastring') should return 'gnirtsaesrever'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 4/4 tests passed!")
