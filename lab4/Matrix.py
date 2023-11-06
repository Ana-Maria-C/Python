class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[0] * m for _ in range(n)]

    def get(self, i, j):    # obtin elementul de pe linia i si coloana j
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.matrix[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)    #creem o noua matrice cu m linii si n coloane
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.matrix[j][i] = self.matrix[i][j]
        return transposed

    def multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            return None
        # daca A(n*m) * B(m*p) = C(n*p)
        result = Matrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
        return result

    def apply(self, lambda_function):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = lambda_function(self.matrix[i][j])

    def print_matrix(self):
        for i in range(self.rows):
            print(self.matrix[i])
        print()