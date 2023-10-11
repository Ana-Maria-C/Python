def matrixTraversal(matrix):
    n=len(matrix)
    traversal=[]
    for i in range(0, n // 2):
        for j in range(i, n - i):
            traversal.append(matrix[i][j])
        for j in range(i + 1, n - i):
            traversal.append(matrix[j][n - i - 1])
        for j in range(n - i - 2, i - 1, -1):
            traversal.append(matrix[n - i - 1][j])
        for j in range(n - i - 2, i, -1):
            traversal.append(matrix[j][i])
    if(n%2==1):
        traversal.append(matrix[n//2][n//2])
    return traversal

def main():
    matrix=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    result=matrixTraversal(matrix)
    print(f"{result}")

main()