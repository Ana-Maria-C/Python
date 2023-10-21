def is_prim(n):
    if n <= 3:
        return True
    else:
        for i in range(2, n // 2):
            if n % i == 0:
                return False
        return True


def main():
    sir = input("Intruduceti sirul de numere: ")
    numere = [int(x) for x in sir.split()]
    newsir = []
    l = len(numere)
    for i in range(0, l - 1):
        if is_prim(numere[i]):
            newsir.append(numere[i])
    print(f"Numerele prime din sirul introdus sunt: {newsir} ")


if __name__ == "__main__":
    main()
