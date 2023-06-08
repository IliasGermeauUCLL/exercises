import re


def one_or_more(string):
    return re.fullmatch("(abc)+", string)
