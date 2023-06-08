# Write your code here
import re


def two_or_more(string):
    return re.fullmatch("abc(abc)+", string)
