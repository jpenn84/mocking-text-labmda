import json


def lambda_handler(event, context):
    # TODO: #6 Setup lambda / expand this stub
    json_output = {"convertedText": convert_text(None)}
    return json.dumps(json_output)

def convert_text(input_text, start_upper_case = None):
    if start_upper_case == None:
        start_upper_case = True

    #remove leading and trailing whitespace chars
    input_text = input_text.strip();

    outputText = ""
    for index in range(len(input_text)):

        # If either: (character index is even and start upper case) or (character is odd and start lower case)
        if ((not index % 2 and start_upper_case) or (index % 2 and not start_upper_case)):
            outputText = outputText + input_text[index].upper()
        
        # Else, by defalt, either: (character index is even and start lower case) or (character is odd and start upper case)
        else:
            outputText = outputText + input_text[index].lower()
    
    return outputText
