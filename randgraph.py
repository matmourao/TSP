import random as rand

def urandgraph(n, m):
    # retorna a matriz de adjacencias
    # do grafo completo de n vertices
    # com pesos aleatorios
    # distribuidos por uma uniforme de 0 a m

    matriz = M = [[0 for i in range(5)] for j in range(5)]
    # inicializa a matriz de adjacencias

    for i in range(n):
        for j in range(i+1,n):
            matriz[i][j] = m*rand.random()
            matriz[j][i] = matriz[i][j]

    return matriz

