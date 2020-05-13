n = int(input())
mat = [[0] * n for i in range(n)]
count = 1
m = 0  # коэф для верхних внутренних  сторон

# Значение центрального элемента матрицы
mat[n // 2][n // 2] = n * n


for v in range(n // 2):

    # Заполнение верхней горизонтальной матрицы
    for i in range(n - m):
        mat[v][i + v] = count
        count += 1

    # Заполнение правой вертикальной матрицы
    for i in range(v + 1, n - v):
        mat[i][-v - 1] = count
        count += 1

    # Заполнение нижней горизонтальной матрицы
    for i in range(v + 1, n - v):
        mat[-v - 1][-i - 1] = count
        count += 1

    # Заполнение левой вертикальной матрицы
    for i in range(v + 1, n - (v + 1)):
        mat[-i - 1][v] = count
        count += 1

    m += 2

# Вывод результата на экран
for i in mat:
    print(*i)
