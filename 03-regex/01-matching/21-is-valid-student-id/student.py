# Write your code
import re


def is_valid_student_id(string):
    return re.fullmatch("[s|r|R|S][0-9]{7}", string)
