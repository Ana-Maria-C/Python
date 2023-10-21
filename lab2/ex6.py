def x_times(x, *args):
    my_dict = {}  # creez un dictionar in care voi pune toate elementele ca si cheie si numarul lor de apartitii ca si
    # valoarea corespunzatoare fiecarei cheie
    for my_list in args:
        for i in my_list:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
    new_list = []  # creez o noua lista ce va contine doar elemntele ce apar de x ori in listele de intrare
    for i in my_dict.keys():
        if my_dict[i] == x:
            new_list.append(i)
    return new_list


def main():
    list1 = [3, 6, 8, 9]
    list2 = [3, 5, 8, 2]
    list3 = [1, 0, 6]
    x = 2
    result = x_times(x, list1, list2, list3)
    print(f"Elementele ce apar de exact {x} ori in liste sunt: {result}")


if __name__ == "__main__":
    main()