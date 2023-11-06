def compare_dicts(dict1, dict2):
    # compar cheile
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # compar valorile cheilor
    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        if type(value1) is dict and type(value2) is dict:
            return compare_dicts(value1, value2)
        elif type(value1) is list and type(value2) is list or type(value1) is set and type(value2) is set:
            return compare_lists(value1, value2)
        elif value1 != value2:
            return False

    return True


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    # parcurg listele simultan (folosesc 'item in' pentru a fi valabil si pentru set)
    for item1, item2 in zip(list1, list2):
        if type(item1) is dict and type(item2) is dict:
            return compare_dicts(item1, item2)
        elif type(item1) is list and type(item2) is list or type(item1) is set and type(item2) is set:
            return compare_lists(item1, item2)
        elif item1 != item2:
            return False
    return True


def main():
    dict1 = {'a': 1, 'b': {'c': [2, 3]}, 'd': [4, 5]}
    dict2 = {'a': 1, 'b': {'c': [2, 3]}, 'd': [4, 5]}
    result = compare_dicts(dict1, dict2)
    print(result)


main()
