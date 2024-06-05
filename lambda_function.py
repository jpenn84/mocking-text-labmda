import json
import os
from global_constants import *
from convert_text import convert_text


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

    json_output = {
       JSON_KEY_OUTPUT_UPPERCASE: convert_text(body[JSON_KEY_INPUT_TEXT], True),
       JSON_KEY_OUTPUT_LOWERCASE: convert_text(body[JSON_KEY_INPUT_TEXT], False)
    }

    return {
        STATUS_CODE_KEY: 200,
        IS_BASE64_ENCODED_KEY: False,
        HEADERS_KEY: {
            CONTENT_TYPE_HEADER_KEY: CONTENT_TYPE_APPLICATION_JSON,
            ACAO_HEADER_KEY: os.environ.get(ACAO_ENV_VAR)
        },
        BODY_KEY: json.dumps(json_output)
    }
