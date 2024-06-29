#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import Get_Fahrenheit
from src.question_d.question_d import reverse_string


class Test_Config(unittest.TestCase):

    #def test_question_a_config(self):
        #self.assertEqual(True, test_config())

    def test_question_b_MPH(self):
        self.assertEqual(get_miles_per_hour(32, 60), 19.883872)

    def test_moon_landing(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
        self.assertEqual(reverse_string("Hello"), "olleH")

    def test_Hot_Cold(self):
       self.assertEqual(Get_Fahrenheit(0), 32)
       self.assertEqual(Get_Fahrenheit(5), 41)
       self.assertEqual(Get_Fahrenheit(10), 50)
