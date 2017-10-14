import unittest
from devide_numbers import divide_numbers
#Test Cases

class DivideTestCases(unittest.TestCase):
    # Divide two numbers
    def test_divide_two_numbers(self):
        result = divide_numbers(4,2)
        self.assertEqual(result,2)

    #Divide by Zero
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(4,0)

    # Divide two strings
    def test_divide_two_strings(self):
    
        with self.assertRaises(TypeError):
            divide_numbers('4','0')

    #Divide two arrays
    def test_divide_two_arrays(self):
        
        with self.assertRaises(TypeError):
            divide_numbers([1],[2])

if __name__ == "__main__":
     unittest.main()   
#  