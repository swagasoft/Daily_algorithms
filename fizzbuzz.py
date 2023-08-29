def fizz_buzz(n): # O(n) time, O(n) space
  #write your code here
  
  result = []
  
  for num in range(1, n + 1):
    if ( num % 3 == 0 and num % 5 == 0):
        result.append('fizzbuzz')
    elif(num % 3 ==  0):
        result.append('fizz')
    elif  (num % 5 == 0):
        result.append('buzz')
    else:
        result.append(str(num))


  return "".join(result)










import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert fizz_buzz(0) == ""
        print("PASSED: Expect fizz_buzz(0) to equal ''")

    def test_2(self):
        assert fizz_buzz(1) == "1"
        print("PASSED: Expect fizz_buzz(1) to equal '1'")

    def test_3(self):
        assert fizz_buzz(15) == "12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz"
        print(
            "PASSED: Expect fizz_buzz(15) to equal '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
