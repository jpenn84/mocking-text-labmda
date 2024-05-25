import unittest
from convert_text import convert_text, lambda_handler, JSON_KEY_INPUT_TEXT, JSON_KEY_START_UPPER_CASE

input_text = "Money can't buy happiness."
expected_output_start_upper_case = "MoNeY CaN'T BuY HaPpInEsS."
expected_output_start_lower_case = "mOnEy cAn't bUy hApPiNeSs."
expected_output_lambda = "{\"convertedText\": \"" + expected_output_start_upper_case + "\"}"
conversion_error_message = "Conversion error:"
lambda_error_message = "Lambda error:"


class TestCalculations(unittest.TestCase):
    def test_default(self):
        output_text = convert_text(input_text)
        self.assertEqual(expected_output_start_upper_case, output_text), conversion_error_message

    def test_upper(self):
        output_text = convert_text(input_text, True)
        self.assertEqual(expected_output_start_upper_case, output_text, conversion_error_message)

    def test_lower(self):
        output_text = convert_text(input_text, False)
        self.assertEqual(expected_output_start_lower_case, output_text, conversion_error_message)

    # If trimmed AFTER conversion, the case will be opposite due whitespace being indexed
    def test_string_trim_odd_number_of_spaces(self):
        output_text = convert_text("   " + input_text + "   ", True)
        self.assertEqual(expected_output_start_upper_case, output_text, conversion_error_message)

    def test_string_trim_even_number_of_spaces(self):
        output_text = convert_text("    " + input_text + "    ", True)
        self.assertEqual(expected_output_start_upper_case, output_text, conversion_error_message)

    def test_string_trim_newline(self):
        output_text = convert_text("\n" + input_text + "\n", True)
        self.assertEqual(expected_output_start_upper_case, output_text, conversion_error_message)

    def test_string_trim_tab(self):
        output_text = convert_text("\t" + input_text + "\t", True)
        self.assertEqual(expected_output_start_upper_case, output_text, conversion_error_message)

    def test_lambda_handler(self):
        event = {
            JSON_KEY_INPUT_TEXT: input_text,
            JSON_KEY_START_UPPER_CASE: True
        }
        self.assertEqual(expected_output_lambda, lambda_handler(event, None), lambda_error_message)


if __name__ == '__main__':
    unittest.main()
