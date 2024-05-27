import json

JSON_KEY_INPUT_TEXT = "inputText"
JSON_KEY_START_UPPER_CASE = "startUpperCase"
JSON_KEY_CONVERTED_TEXT = "convertedText"


def lambda_handler(event, context):
    body = json.loads(event['body'])
    json_output = {JSON_KEY_CONVERTED_TEXT: convert_text(body[JSON_KEY_INPUT_TEXT], body[JSON_KEY_START_UPPER_CASE])}
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": '*'
        },
        "body": json.dumps(json_output)
    }


def convert_text(input_text, start_upper_case=None):
    if start_upper_case is None:
        start_upper_case = True

    # remove leading and trailing whitespace chars
    input_text = input_text.strip()

    output_text = str()
    for index in range(len(input_text)):

        # If either: (character index is even and start upper case) or (character is odd and start lower case)
        # Then make it upper case
        if (not index % 2 and start_upper_case) or (index % 2 and not start_upper_case):
            output_text = output_text + input_text[index].upper()

        # Else, make it lower case
        else:
            output_text = output_text + input_text[index].lower()

    return output_text
