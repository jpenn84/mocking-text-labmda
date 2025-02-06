import json
import os
import unittest
from global_constants import *
from convert_text import convert_text
from lambda_function import lambda_handler

INPUT_TEXT = "Money can't buy happiness."
EXPECTED_OUTPUT_START_UPPER_CASE = "MoNeY cAn'T bUy HaPpInEsS."
EXPECTED_OUTPUT_START_LOWER_CASE = "mOnEy CaN't BuY hApPiNeSs."
EXPECTED_OUTPUT_LAMBDA_200 = (
    "{\"outputUpperCase\": \"" + EXPECTED_OUTPUT_START_UPPER_CASE + "\", \"outputLowerCase\": \"" + EXPECTED_OUTPUT_START_LOWER_CASE + "\"}"
    )
CONVERSION_ERROR_MESSAGE = "Conversion error:"
LAMBDA_ERROR_MESSAGE = "Lambda error:"


def unset_acao_header():
    del os.environ[ACAO_ENV_VAR]


def set_acao_header():
    os.environ[ACAO_ENV_VAR] = "*"


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

    def test_string_with_non_alpha(self):
        output_text = convert_text("Hello! Goodbye!", True)
        self.assertEqual("HeLlO! gOoDbYe!", output_text, CONVERSION_ERROR_MESSAGE)

    def test_lambda_handler_200(self):
        set_acao_header()
        body = {JSON_KEY_INPUT_TEXT: INPUT_TEXT}
        event = {BODY_KEY: json.dumps(body)}
        resp = lambda_handler(event, None)
        self.assertEqual(EXPECTED_OUTPUT_LAMBDA_200, resp[BODY_KEY], LAMBDA_ERROR_MESSAGE)
        self.assertEqual(200, resp[STATUS_CODE_KEY], LAMBDA_ERROR_MESSAGE)

    def test_missing_acao_header(self):
        unset_acao_header()
        body = {JSON_KEY_INPUT_TEXT: INPUT_TEXT}
        event = {BODY_KEY: json.dumps(body)}
        resp = lambda_handler(event, None)
        self.assertEqual(ACAO_ENV_VAR_NOT_SET_ERROR_MESSAGE, resp[BODY_KEY], LAMBDA_ERROR_MESSAGE)
        self.assertEqual(500, resp[STATUS_CODE_KEY], LAMBDA_ERROR_MESSAGE)


if __name__ == '__main__':
    unittest.main()
