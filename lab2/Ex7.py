def is_palindrom(number):
    ok = True
    sir = str(number)
    n = len(sir)
    for i in range(0, n // 2):
        if sir[i] != sir[-i - 1]:
            ok = False
            break
    return ok


def find_tuple(my_list):
    max_palindrom = 0
    numbers_of_palindrom = 0
    for i in my_list:
        if is_palindrom(i):
            numbers_of_palindrom += 1
            if i > max_palindrom:
                max_palindrom = i
    return numbers_of_palindrom, max_palindrom


def main():
    my_list = [333, 121, 3345, 1212, -131]
    result = find_tuple(my_list)
    print(f"Numarul de numere palindrom este {result[0]}, iar cel mai mare dintre acestea este {result[1]}.")


main()
