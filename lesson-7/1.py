class Matrix:
    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result

    def __str__(self):
        return 'Матрица:\n' + '\n'.join('\t'.join(map(str, line)) for line in self.matrix)


matrix1 = [
    [1, 2],
    [3, 4],
    [5, 6],
]

matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6],
]


a = Matrix(matrix1)
print(a)
b = Matrix(matrix2)
print(b)
c = Matrix(a + b)
print(c)
