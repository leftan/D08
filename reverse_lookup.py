d = {1: 'blue', 2: 'blue', 3: 'red'}

def reverse_lookup(dict_lookup, value):
    result = []
    print(list(dict_lookup.items()))

    for key, val in dict_lookup.items():
        # print(key)
        # print(val)
        if val == value:
            result.append(key)
    return result


print(reverse_lookup(d, 'blue'))
# print(reverse_lookup(d, 'red'))