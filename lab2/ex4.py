def sing(notes, moves, start_move):
    melody = []
    l = len(notes)
    melody.append(notes[start_move % l])
    for move in moves:
        index = (start_move + move) % l
        start_move = index
        melody.append(notes[index])
    return melody


def main():
    result = sing(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    print(f"Sirul obtinut este {result}")


if __name__ == "__main__":
    main()
