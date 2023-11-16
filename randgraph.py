import random as rand

def urandgraph(n, m):
    # retorna a matriz de adjacencias
    # do grafo completo de n vertices
    # com pesos aleatorios
    # distribuidos por uma uniforme de 0 a m

    matrix = [[0 for i in range(n)] for j in range(n)]
    # inicializa a matriz de adjacencias

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j] = m*rand.random()
            matrix[j][i] = matrix[i][j]

    return matrix

