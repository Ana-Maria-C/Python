def first_n_fibbo(n):
    t1 = 0
    t2 = 1
    sir = [t1, t2]
    for i in range(0, n - 2):
        t3 = t1 + t2
        sir.append(t3)
        t1 = t2
        t2 = t3
    return sir


def main():
    n = int(input("Introduceti numarul: "))
    result = first_n_fibbo(n)
    print(f"Primii {n} termeni din sirul fibbonaci este: {result}")


if __name__ == "__main__":
    main()
