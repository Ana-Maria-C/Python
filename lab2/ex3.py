def a_int_b(a, b):
    result = []
    for e in a:
        if e in b:
            result.append(e)
    return result


def a_reu_b(a, b):
    result = []
    for e in a:
        result.append(e)
    for e in b:
        if e not in result:
            result.append(e)
    return result


def a_min_b(a, b):
    result = []
    for e in a:
        if e not in b:
            result.append(e)
    return result


def b_min_a(a, b):
    result = []
    for e in b:
        if e not in a:
            result.append(e)
    return result


def main():
    a = input("Introduceti lista pentru a: ")
    b = input("Introduceti lista pentru b: ")
    elemA = a.split()
    elemB = b.split()
    print(f"Reuniunea dintre a si b este: {a_reu_b(elemA, elemB)}")
    print(f"Intersectia dintre a si b este: {a_int_b(elemA, elemB)}")
    print(f"Diferenta a-b este: {a_min_b(elemA, elemB)}")
    print(f"Diferenta b-a este: {b_min_a(elemA, elemB)}")


if __name__ == "__main__":
    main()
