#!/usr/bin/python3
""" text indentation function"""


def text_indentation(text):
    """ print text

    Args:
       text (string): the text to print.
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = 0
    while t < len(text) and text[t] == ' ':
        t += 1

    while t < len(text):
        print(text[t], end="")
        if text[t] == "\n" or text[t] in ".?:":
            if text[t] in ".?:":
                print("\n")
            t += 1
            while t < len(text) and text[t] == ' ':
                t += 1
            continue
        t += 1
