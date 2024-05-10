import unittest
from convert_text import convert_text

input_text = "Money can't buy happiness."
expected_output_start_upper_case = "MoNeY CaN'T BuY HaPpInEsS."
expected_output_start_lower_case = "mOnEy cAn't bUy hApPiNeSs."
error_message = "Conversion error:"

class TestCalculations(unittest.TestCase):
    def test_default(self):
        output_text = convert_text(input_text)
        self.assertEqual(output_text, expected_output_start_upper_case)

    def test_upper(self):
        output_text = convert_text(input_text, True)
        self.assertEqual(output_text, expected_output_start_upper_case)

    def test_lower(self):
        output_text = convert_text(input_text, False)
        self.assertEqual(output_text, expected_output_start_lower_case)

if __name__ == '__main__':
    unittest.main()
