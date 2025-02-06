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
        # do not change non-alpha characters
        if not input_text[index].isalpha():
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
