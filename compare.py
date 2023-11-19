from randgraph import *
from opt_alorithms import *

def u_compare(n, m, k):
    # compara os algoritmos com
    # k grafos aleatorios de n vertices
    # com pesos distrbuidos por unif(0,m)
    # retorna uma lista com quantos %
    # cada algoritmo esta longe do menor caminho
    # ordem: 
    # nearest neighbor
    # cheapest edge
    # chritofides
    # savings

    results = []
    for i in range(k):
        M = urandgraph(n,m)
        weights = [nearest_neighbor(M)[1],
                   cheapest_edge(M)[1],
                   m*n, #christofides
                   savings(M)[1]]
        mini = min(weights)
        percents = [100*x/mini - 100 for x in weights]
        results.append(percents)

    final_result = []
    for i in range(4):
        percent = 0
        for r in results:
            percent += r[i]

        percent = percent/k
        final_result.append(percent)
    
    return final_result

def u_compare_opt(n, m, k):
    # faz a mesma coisa mas compara com o algoritmo otimo

    results = []
    for i in range(k):
        M = urandgraph(n,m)
        weights = [nearest_neighbor(M)[1],
                   cheapest_edge(M)[1],
                   m*n, #christofides
                   savings(M)[1]]
        mini = opt(M)
        percents = [100*x/mini - 100 for x in weights]
        results.append(percents)

    final_result = []
    for i in range(4):
        percent = 0
        for r in results:
            percent += r[i]

        percent = percent/k
        final_result.append(percent)
    
    return final_result


print(u_compare_opt(10,100,100))