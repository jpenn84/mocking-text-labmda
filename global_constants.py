# request payload keys
JSON_KEY_INPUT_TEXT = "inputText"
JSON_KEY_OUTPUT_UPPERCASE = "outputUpperCase"
JSON_KEY_OUTPUT_LOWERCASE = "outputLowerCase"

# response payload keys
STATUS_CODE_KEY = "statusCode"
IS_BASE64_ENCODED_KEY = "isBase64Encoded"
HEADERS_KEY = "headers"
CONTENT_TYPE_HEADER_KEY = "Content-Type"
CONTENT_TYPE_APPLICATION_JSON = "application/json"
ACAO_HEADER_KEY = "Access-Control-Allow-Origin"
BODY_KEY = "body"

# ACAO env var
ACAO_ENV_VAR = "MOCKING_TEXT_LAMBDA_ACAO"
ACAO_ENV_VAR_NOT_SET_ERROR_MESSAGE = ACAO_HEADER_KEY + "header is not set on the server"
