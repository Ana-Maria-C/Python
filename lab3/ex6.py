def unique_or_duplicate(my_list):
    duplicate_set = set()
    unique_set = set()
    for elem in my_list:
        if elem in unique_set:
            duplicate_set.add(elem)
            unique_set.discard(elem)
        else:
            unique_set.add(elem)
    return len(duplicate_set), len(unique_set)


def main():
    my_list = [1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8, 9]
    result = unique_or_duplicate(my_list)
    print(f"Numarul de elemnete duplicate este: {result[0]}, iar numarul de elemente unice este {result[1]}")


main()
