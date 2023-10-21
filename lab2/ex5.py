def trans_matrix(matrix):
    new_matrix = matrix
    for i in range(len(matrix)):
        for j in range(i):
            new_matrix[i][j] = 0
    return new_matrix


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    new_matrix = trans_matrix(matrix)
    print(f"Matricea obtinuta este {new_matrix}")


if __name__ == "__main__":
    main()
