def hex_name(text):
    """Generates an obscure name based on the class name hex value added to the length of the classes definition
       dictionary

    Args:
        **text (str)**: name of the class to be obscured

    Returns:
        An obscured name for a class
    """
    return f"_{hex(get_ascii_sum(text))}"


def get_ascii_sum(text):
    """Returns the sum of the ascii values of a string

    Args:
        **text (str)**: string of which to get the ascii value

    Returns:
        The sum of the ascii values of the string provided
    """
    sum = 0
    for c in text:
        sum += int(ord(c))
    return sum
