import numpy as np
from randgraph import *
from algor import *

# função que calcula o custo do caminho
def cost(route, matrix):
    cost = 0
    for i in range(len(route)):
        cost += matrix[route[i-1]][route[i]] # soma o peso de cada aresta do caminho

    return cost



# função que aplica o algoritmo 2-opt dada a matriz de adjacencia e a rota a ser melhorada
def two_opt(matrix, route):
    list_routes = [route]
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i+1, len(route)): 
                new_route = route.copy() 
                new_route[i:j] = route[j-1:i-1:-1]  # Inverte a ordem dos elementos entre i e j
                new_cost = cost(new_route, matrix)  # Calcula o custo da nova rota
                
                if new_cost < cost(best_route, matrix):  # Se o custo da nova rota for menor, atualiza a rota
                    best_route = new_route
                    improved = True

        if improved:
            list_routes.append(best_route)
        route = best_route

    return best_route, list_routes
