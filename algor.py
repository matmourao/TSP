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
