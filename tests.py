import unittest
from convert_text import convert_text, lambda_handler, JSON_KEY_INPUT_TEXT, JSON_KEY_START_UPPER_CASE

INPUT_TEXT = "Money can't buy happiness."
EXPECTED_OUTPUT_START_UPPER_CASE = "MoNeY CaN'T BuY HaPpInEsS."
EXPECTED_OUTPUT_START_LOWER_CASE = "mOnEy cAn't bUy hApPiNeSs."
EXPECTED_OUTPUT_LAMBDA_200 = {'body': '{"convertedText": "MoNeY CaN\'T BuY HaPpInEsS."}', 'status code': 200}
CONVERSION_ERROR_MESSAGE = "Conversion error:"
LAMBDA_ERROR_MESSAGE = "Lambda error:"


class TestCalculations(unittest.TestCase):
    def test_default(self):
        output_text = convert_text(INPUT_TEXT)
        self.assertEqual(EXPECTED_OUTPUT_START_UPPER_CASE, output_text), CONVERSION_ERROR_MESSAGE

    def test_upper(self):
        output_text = convert_text(INPUT_TEXT, True)
        self.assertEqual(EXPECTED_OUTPUT_START_UPPER_CASE, output_text, CONVERSION_ERROR_MESSAGE)

    def test_lower(self):
        output_text = convert_text(INPUT_TEXT, False)
        self.assertEqual(EXPECTED_OUTPUT_START_LOWER_CASE, output_text, CONVERSION_ERROR_MESSAGE)

    # If trimmed AFTER conversion, the case will be opposite due whitespace being indexed
    def test_string_trim_odd_number_of_spaces(self):
        output_text = convert_text("   " + INPUT_TEXT + "   ", True)
        self.assertEqual(EXPECTED_OUTPUT_START_UPPER_CASE, output_text, CONVERSION_ERROR_MESSAGE)

    def test_string_trim_even_number_of_spaces(self):
        output_text = convert_text("    " + INPUT_TEXT + "    ", True)
        self.assertEqual(EXPECTED_OUTPUT_START_UPPER_CASE, output_text, CONVERSION_ERROR_MESSAGE)

    def test_string_trim_newline(self):
        output_text = convert_text("\n" + INPUT_TEXT + "\n", True)
        self.assertEqual(EXPECTED_OUTPUT_START_UPPER_CASE, output_text, CONVERSION_ERROR_MESSAGE)

    def test_string_trim_tab(self):
        output_text = convert_text("\t" + INPUT_TEXT + "\t", True)
        self.assertEqual(EXPECTED_OUTPUT_START_UPPER_CASE, output_text, CONVERSION_ERROR_MESSAGE)

    def test_lambda_handler_200(self):
        event = {
            JSON_KEY_INPUT_TEXT: INPUT_TEXT,
            JSON_KEY_START_UPPER_CASE: True
        }
        self.assertEqual(EXPECTED_OUTPUT_LAMBDA_200, lambda_handler(event, None), LAMBDA_ERROR_MESSAGE)


if __name__ == '__main__':
    unittest.main()
