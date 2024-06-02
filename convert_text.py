import json
import os
from global_constants import *


def lambda_handler(event, context):
    if os.environ.get(ACAO_ENV_VAR) is None:
        print(ACAO_ENV_VAR_NOT_SET_ERROR_MESSAGE)
        return {
            STATUS_CODE_KEY: 500,
            IS_BASE64_ENCODED_KEY: False,
            HEADERS_KEY: {
                CONTENT_TYPE_HEADER_KEY: CONTENT_TYPE_APPLICATION_JSON,
                ACAO_HEADER_KEY: "*"
            },
            BODY_KEY: ACAO_ENV_VAR_NOT_SET_ERROR_MESSAGE
        }

    body = json.loads(event[BODY_KEY])
    json_output = {JSON_KEY_CONVERTED_TEXT: convert_text(body[JSON_KEY_INPUT_TEXT], body[JSON_KEY_START_UPPER_CASE])}
    return {
        STATUS_CODE_KEY: 200,
        IS_BASE64_ENCODED_KEY: False,
        HEADERS_KEY: {
            CONTENT_TYPE_HEADER_KEY: CONTENT_TYPE_APPLICATION_JSON,
            ACAO_HEADER_KEY: os.environ.get(ACAO_ENV_VAR)
        },
        BODY_KEY: json.dumps(json_output)
    }


def convert_text(input_text, start_upper_case=None):
    if start_upper_case is None:
        start_upper_case = True

    # remove leading and trailing whitespace chars
    input_text = input_text.strip()

    # string to construct output from converted input
    output_text = str()

    # boolean to toggle the expected case
    next_char_upper = start_upper_case

    for index in range(len(input_text)):
        # add whitespace to constructed string without toggling the expected case
        if input_text[index].isspace():
            output_text = output_text + input_text[index]
            continue

        # add char to constructed string based on the expected case
        if next_char_upper:
            output_text = output_text + input_text[index].upper()
        else:
            output_text = output_text + input_text[index].lower()

        # toggle the expected case
        next_char_upper = not next_char_upper

    return output_text
