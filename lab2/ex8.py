def function(x=1, sir="", flag=True):
    new_sir_true = []
    new_sir_false = []
    for subsir in sir:
        for ch in subsir:
            ascii_value = ord(ch)
            if ascii_value % x == 0:
                # print(ascii)
                if ch not in new_sir_true:
                    new_sir_true.append(ch)
            elif ch not in new_sir_false:
                new_sir_false.append(ch)
    if flag:
        return new_sir_true
    else:
        return new_sir_false


def main():
    result = function(2, ["test", "hello", "lab002"], False)
    print(f"Caracterele ce respecta conditiile sunt: {result} ")


if __name__ == "__main__":
    main()
