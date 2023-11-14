from randgraph import *
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