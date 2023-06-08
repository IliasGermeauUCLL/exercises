# Write your code here
def odd_keys_dict(dictionary):
    dictionary1 = {}
    for k, v in dictionary.items():
        if k % 2 != 0:
            dictionary1[k] = v
    return dictionary1
