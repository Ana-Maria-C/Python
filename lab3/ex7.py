def a_and_b(a, b):
    result = list()
    # nu pot adauga elemente mutabile(list) intr un set, de asta convertim la tuple
    result.append(tuple(a.intersection(b)))
    result.append(tuple(a.union(b)))
    result.append(tuple(a.difference(b)))
    result.append(tuple(b.difference(a)))
    return result


def print_function(set_a, set_b, result):
    result_list = list(result)
    print(f"{set_a} & {set_b} : {result_list[0]}")
    print(f"{set_a} | {set_b} : {result_list[1]}")
    print(f"{set_a} - {set_b} : {result_list[2]}")
    print(f"{set_b} - {set_a} : {result_list[3]}")


def multi_set(*sets):
    sets_list = list(sets)
    for i in range(0, len(sets_list) - 1):
        for j in range(i + 1, len(sets_list)):
            result = a_and_b(sets_list[i], sets_list[j])
            print_function(sets_list[i], sets_list[j], result)


def main():
    sets = [{1, 2}, {2, 3}]
    multi_set(*sets)


main()
