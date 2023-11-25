from randgraph import *
from opt_algorithms import *

def u_compare(n, m, k):
    # compara os algoritmos com
    # k grafos aleatorios de n vertices
    # com pesos distrbuidos por unif(0,m)
    # retorna uma lista com quantos %
    # cada algoritmo esta longe do menor caminho
    # ordem: 
    # nearest neighbor
    # cheapest edge
    # savings

    results = []
    for i in range(k):
        M = urandgraph(n,m)
        weights = [nearest_neighbor(M)[1],
                   cheapest_edge(M)[1],
                   savings(M)[1]]
        mini = opt(M)
        percents = [100*x/mini - 100 for x in weights]
        results.append(percents)

    final_result = []
    for i in range(3):
        percent = 0
        for r in results:
            percent += r[i]

        percent = percent/k
        final_result.append(percent)
    
    return final_result

def u_measure_opt2(n, m, k):
    # mede a porcentagem de melhora do opt2 dado as rotas de cada algoritmo
    # calcula a media da melhora para k grafos de n vertices
    # com pesos distribuidos por unif(0,m)
    # retorna uma lista com a média da porcentagem de melhora dos algoritmos 
    # ordem:
    # nearest neighbor
    # cheapest edge
    # savings
    
    results = []
    for i in range(k):
        M = urandgraph(n, m)
        routes = [nearest_neighbor(M)[0],
                   cheapest_edge(M)[0],
                   savings(M)[0]]
        weights = [cost(x,M) for x in routes]
        improved = [two_opt(M, x)[0] for x in routes]
    
        measures = [100*(weights[x] - cost(improved[x],M))/weights[x] for x in range(3)]
        results.append(measures)
    
    final_result = []
    for i in range(3):
        percent = 0
        for r in results:
            percent += r[i]
        
        percent = percent/k
        final_result.append(percent)
    
    return final_result

def u_measure_opt3(n, m, k):
    # faz a mesma coisa com o opt3
    
    results = []
    for i in range(k):
        M = urandgraph(n, m)
        routes = [nearest_neighbor(M)[0],
                   cheapest_edge(M)[0],
                   savings(M)[0]]
        weights = [cost(x,M) for x in routes]
        improved = [three_opt(M, x)[0] for x in routes]
    
        measures = [100*(weights[x] - cost(improved[x],M))/weights[x] for x in range(3)]
        results.append(measures)
    
    final_result = []
    for i in range(3):
        percent = 0
        for r in results:
            percent += r[i]
        
        percent = percent/k
        final_result.append(percent)
    
    return final_result


algoritmos = ["Vizinho mais próximo: ", "Aresta mais barata: ", "Clark e Wright: "]

compare = u_compare(10, 100, 1000) 
for i in range(3):
    print(algoritmos[i], "{:.2f}".format(compare[i]), "% distante da solução ótima em média")

print("="*80)
print("2-OPT: ")
measure_2 = u_measure_opt2(20,100,1000)
for i in range(3):
    print(algoritmos[i], "melhorado em ", "{:.2f}".format(measure_2[i]), "% em média")

print("="*80)
print("3-OPT: ")
measure_3 = u_measure_opt3(20,100,1000)
for i in range(3):
    print(algoritmos[i], "melhorado em ", "{:.2f}".format(measure_3[i]), "% em média")













