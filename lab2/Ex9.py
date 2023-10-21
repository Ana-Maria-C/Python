def find_wrong_seats(matrix):
    my_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(0, i):
                if matrix[i][j] <= matrix[k][j]:
                    if (i,j) not in my_list:
                        my_list.append((i, j))
    return my_list


def main():
    matrix = [[1, 2, 3, 2, 1, 1],

              [2, 4, 4, 3, 7, 2],

              [5, 5, 2, 5, 6, 4],

              [6, 6, 7, 6, 7, 5]]
    result = find_wrong_seats(matrix)
    print(f"Locurile care nu au vizibilitate la scena sunt:{result}")


main()
