def my_function(my_dict):
    keys = set()  # vom pune cheile parcurse
    result = set()  # vom pune valorile corespunzatoare cheilor
    current_key = next(iter(my_dict.keys()))
    while current_key not in keys:
        keys.add(current_key)
        result.add(my_dict[current_key])
        current_key = my_dict[current_key]
    return result


def main():
    dict = ({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
    result = my_function(dict)
    print(result)


main()
