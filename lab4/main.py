from Matrix import Matrix
from Stack import Stack
from Queue import Queue

def main_for_ex1():
    stiva1 = Stack()
    stiva1.push(1)
    stiva1.push(3)
    stiva1.push(8)
    last_el = stiva1.peek()
    print(last_el)
    stiva1.print_values()
    al = stiva1.pop()
    stiva1.print_values()


def main_for_ex2():
    coada1 = Queue()
    coada1.push(1)
    coada1.push(3)
    coada1.push(8)
    first_el = coada1.peek()
    print(first_el)
    coada1.print_values()
    al = coada1.pop()
    coada1.print_values()


def main_for_ex3():
    matrix = Matrix(2, 3)

    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    matrix.print_matrix()

    transposed = matrix.transpose()
    transposed.print_matrix()

    other_matrix = Matrix(3, 2)
    other_matrix.set(0, 0, 1)
    other_matrix.set(0, 1, 2)
    other_matrix.set(1, 0, 3)
    other_matrix.set(1, 1, 4)
    other_matrix.set(2, 0, 5)
    other_matrix.set(2, 1, 6)

    result = matrix.multiply(other_matrix)
    result.print_matrix()

    matrix.apply(lambda x: x * 2)
    matrix.print_matrix()


#main_for_ex1()
#main_for_ex2()
main_for_ex3()