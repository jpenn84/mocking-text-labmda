import unittest
from convert_text import convert_text, lambda_handler

input_text = "Money can't buy happiness."
expected_output_start_upper_case = "MoNeY CaN'T BuY HaPpInEsS."
expected_output_start_lower_case = "mOnEy cAn't bUy hApPiNeSs."
expected_output_lambda = "{\"convertedText\": \"" + expected_output_start_upper_case + "\"}"
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

    # If trimmed AFTER conversion, the case will be opposite due whitespace being indexed
    def test_string_trim_odd_number_of_spaces(self):
        output_text = convert_text("   " + input_text + "   ", True)
        self.assertEqual(output_text, expected_output_start_upper_case)

    def test_string_trim_even_number_of_spaces(self):
        output_text = convert_text("    " + input_text + "    ", True)
        self.assertEqual(output_text, expected_output_start_upper_case)

    def test_string_trim_newline(self):
        output_text = convert_text("\n" + input_text + "\n", True)
        self.assertEqual(output_text, expected_output_start_upper_case)

    def test_string_trim_tab(self):
        output_text = convert_text("\t" + input_text + "\t", True)
        self.assertEqual(output_text, expected_output_start_upper_case)

    def test_lambda_handler(self):
        event = {
            "inputText": input_text,
            "startUpperCase": True
        }
        self.assertEqual(expected_output_lambda, lambda_handler(event, None))


if __name__ == '__main__':
    unittest.main()
