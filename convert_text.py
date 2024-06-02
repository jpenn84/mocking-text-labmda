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
