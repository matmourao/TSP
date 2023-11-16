from randgraph import *
import numpy as np
import itertools

def opt(M):
    # retorna o comprimento do
    # menor ciclo hamiltoniano
    # da matriz de adjacencias M

    n = len(M)
    perm = list(itertools.permutations(range(n)))
    # guarda todas as permutações dos vertices em p

    ciclos = []
    # lista com os pesos das arestas de cada permutação
    for p in perm:
        ciclo = []
        for i in range(len(p)-1):
            ciclo.append(M[p[i]][p[i+1]])
        ciclo.append(M[p[len(p)-1]][p[0]])
        ciclos.append(ciclo)

    # soma o peso de todas as arestas de cada ciclo
    ciclos = list(sum(x) for x in ciclos)
    
    # retorna o menor deles
    return min(ciclos)

def nearest_neighbor(matrix):
    n = len(matrix)
    
    # inicializa o ciclo com um vértice "aleatório" e o peso
    cycle = [0]
    weight = 0
    
    while len(cycle) < n:
        current_vertex = cycle[-1] # último elemento adicionado ao ciclo
        min_distance = max(matrix[current_vertex]) + 1

        # encontra o vizinho mais próximo
        for neighbor in range(n):
            if neighbor not in cycle:
                distance = matrix[current_vertex][neighbor]
                if distance < min_distance:
                    min_distance = distance
                    nearest_neighbor = neighbor
        
        # adiciona o vizinho mais próximo ao ciclo e contabiliza o peso
        cycle.append(nearest_neighbor)
        weight += min_distance
    
    # adiciona a aresta final para formar um ciclo e contabiliza o peso
    cycle.append(cycle[0])
    weight += matrix[0][cycle[-2]]
    
    return cycle, weight

def savings(matrix):
    n = len(matrix)

    # constroi a matriz de economias
    S = np.zeros((n,n))
    for i in range(1, n):
        for j in range(i+1,n):
            S[i,j] = matrix[i][0] + matrix[0][j] - matrix[i][j]
    
    # calcula o primeiro ciclo
    idx = np.unravel_index(np.argmax(S, axis=None), S.shape)
    cycle = list(idx) # ignora o vertice 0 por enquanto
    S[idx] = 0

    # constroi o resto do ciclo (sem o 0 ainda)
    while(len(cycle) < n-1):
        idx = np.unravel_index(np.argmax(S, axis=None), S.shape)
        if cycle[0] in idx:
            aux = list(idx)
            aux.remove(cycle[0])
            cycle = aux + cycle
        elif cycle[-1] in  idx:
            aux = list(idx)
            aux.remove(cycle[-1])
            cycle = cycle + aux
        else:
            S[idx] = 0  

    # fecha o ciclo e calcula seu peso total
    cycle = [0] + cycle + [0]
    weight = 0
    for i in range(len(cycle)-1):
        weight += matrix[cycle[i]][cycle[i+1]]

    return cycle, weight
