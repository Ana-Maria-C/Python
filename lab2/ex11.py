def sorted_by_3_ch(list_of_tuples):
    list_of_tuples.sort(key=lambda i: i[1][2])
    return list_of_tuples


def main():
    list_of_tuples = [('abc', 'bcd'), ('abc', 'zza')]
    result = sorted_by_3_ch(list_of_tuples)
    print(f"Lista sortata este: {result}")


main()
