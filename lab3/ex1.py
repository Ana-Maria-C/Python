def a_and_b(a, b):
    result = set()
    # nu pot adauga elemente mutabile(list) intr un set, de asta convertim la tuple
    result.add(tuple(a.intersection(b)))
    result.add(tuple(a.union(b)))
    result.add(tuple(a.difference(b)))
    result.add(tuple(b.difference(a)))
    return result


def main():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    result_set = a_and_b(a, b)
    print(
        f"\n Intersectia dintre a si b este: {result_set.pop()}.\n Reuniunea dintre a si b este: {result_set.pop()}.\n Diferenta a-b este: {result_set.pop()}.\n Diferenta b-a este: {result_set.pop()} ")


main()
