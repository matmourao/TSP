from randgraph import urandgraph
from algor import opt
import time

def inef(n,m):
    # mede o tempo levado para 
    # rodar o algoritmo ótimo
    # num grafo aleatorio de n vertices
    # com os pesos distribuidos por unif(0,m)

    M = urandgraph(n,m)
    start = time.time()
    opt(M)
    end = time.time()
    return(end - start)

for i in range(6,13):

    print("Para ", i ," vértices, o algoritmo demora ", inef(i,100), " segundos.")
