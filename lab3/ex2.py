def contor(sir):
    my_dict = {}  # creez un dictionar in care voi pune toate elementele ca si cheie si numarul lor de apartitii ca si
    # valoarea corespunzatoare fiecarei cheie
    for i in range(len(sir)):
        if sir[i] in my_dict:
            my_dict[sir[i]] += 1
        else:
            my_dict[sir[i]] = 1
    return my_dict


def main():
    result = contor("Ana has apples.")
    print(f"Numarul de aparitii a fiecarui caracter: \n {result}")


main()
