import json
import unittest
from convert_text import convert_text, lambda_handler, JSON_KEY_INPUT_TEXT, JSON_KEY_START_UPPER_CASE

INPUT_TEXT = "Money can't buy happiness."
EXPECTED_OUTPUT_START_UPPER_CASE = "MoNeY cAn't BuY hApPiNeSs."
EXPECTED_OUTPUT_START_LOWER_CASE = "mOnEy CaN'T bUy HaPpInEsS."
EXPECTED_OUTPUT_LAMBDA_200 = "{\"convertedText\": \"MoNeY cAn't BuY hApPiNeSs.\"}"
CONVERSION_ERROR_MESSAGE = "Conversion error:"
LAMBDA_ERROR_MESSAGE = "Lambda error:"


class TestConversion(unittest.TestCase):
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
        body = {
            JSON_KEY_INPUT_TEXT: INPUT_TEXT,
            JSON_KEY_START_UPPER_CASE: True
        }
        event = {"body": json.dumps(body)}
        resp = lambda_handler(event, None)
        self.assertEqual(EXPECTED_OUTPUT_LAMBDA_200, resp['body'], LAMBDA_ERROR_MESSAGE)
        self.assertEqual(200, resp['statusCode'], LAMBDA_ERROR_MESSAGE)


if __name__ == '__main__':
    unittest.main()
