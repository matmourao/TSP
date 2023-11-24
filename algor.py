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
    S = np.triu(S) + np.tril(S.T, 1)

    # calcula o primeiro ciclo
    idx = np.unravel_index(np.argmax(S, axis=None), S.shape)
    cycle = list(idx) # ignora o vertice 0 por enquanto
    S[idx] = np.NINF
    S[(idx[1], idx[0])] = np.NINF
    
    # constroi o resto do ciclo (sem o 0 ainda)
    while(len(cycle) < n-1):
        # acha a aresta de maior economia a ser inserida
        max = np.NINF
        for i in [x for x in range(1,n) if x not in cycle]:
            for j in [cycle[0], cycle[-1]]:
                if S[i][j] > max:
                    idx = (i,j)
                    max = S[idx]
            
        # adiciona a aresta no ciclo
        if cycle[0] in idx:
            aux = list(idx)
            aux.remove(cycle[0])
            cycle = aux + cycle
        elif cycle[-1] in  idx:
            aux = list(idx)
            aux.remove(cycle[-1])
            cycle = cycle + aux
        
        S[idx] = np.NINF
        S[(idx[1], idx[0])] = np.NINF
   
    # fecha o ciclo e calcula seu peso total
    cycle = [0] + cycle + [0]
    weight = 0
    for i in range(len(cycle)-1):
        weight += matrix[cycle[i]][cycle[i+1]]

    return cycle, weight

def cheapest_edge(matrix):
    n = len(matrix)

    # controi o primeiro ciclo
    S = np.zeros((n,n))
    for i in range(1, n):
        for j in range(i+1,n):
            S[i,j] = matrix[i][0] + matrix[0][j] - matrix[i][j]
    idx = np.unravel_index(np.argmax(S, axis=None), S.shape)
    cycle = [0] + list(idx) # sem o ultimo vertice por enquanto

    # define o conjunto V dos vertices fora do ciclo
    V = [x for x in range(1,n) if x not in idx]

    # constroi o resto do ciclo
    while(len(V) > 0):

        # acha o vertice mais barato a ser inserido
        min = np.inf
        for t in range(len(cycle)-1):
            i = cycle[t]
            j = cycle[t+1]
            for k in V:
                cost = matrix[i][k] + matrix[k][j] - matrix[i][j]
                if cost < min:
                    min = cost
                    vertex = k
                    idx = t
        
        # insere as respectivas arestas no ciclo
        cycle.insert(idx+1, vertex)

        # remove o vertice de V
        V.remove(vertex)

    # fecha o ciclo e calcula seu peso total
    cycle = cycle + [0]
    weight = 0
    for i in range(len(cycle)-1):
        weight += matrix[cycle[i]][cycle[i+1]]

    return cycle, weight