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

    input_text = input_text.strip()

    output_text = str()

    # Boolean to toggle for every letter
    next_char_upper = start_upper_case

    for index in range(len(input_text)):
        if input_text[index].isspace():
            output_text = output_text + input_text[index]
            continue
        if next_char_upper:
            output_text = output_text + input_text[index].upper()
        else:
            output_text = output_text + input_text[index].lower()
        next_char_upper = not next_char_upper

    return output_text
