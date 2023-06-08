# Write your code here
def double_dict_values(dictionary):
    rsult = {}
    for k, v in dictionary.items():
        v2 = v * 2
        rsult[k] = v2
    return rsult
