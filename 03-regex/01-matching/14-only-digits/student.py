# Write your code here
import re


def only_digits(string):
    return re.fullmatch("[1|2|3|4|5|6|7|8|9|0]*", string)
