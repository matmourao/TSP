import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import image as mpimg
from opt_algorithms import *
from algor import *


image = mpimg.imread("./img/map.png")


#         location    x    y
city_list=np.array([[30,  172],  # London
                    [127, 777],  # Barcelona
                    [136, 339],  # Paris
                    [216, 211],  # Brussels
                    [241, 112],  # Amsterdam
                    [416, 552],  # Milan
                    [448,  34],  # Hamburg
                    [513, 389],  # Munich
                    [587, 104],  # Berlin
                    [631, 262],  # Prague
                    [690, 528],  # Zagreb
                    [710, 382],  # Vienna
                    [820, 422],  # Budapest
                    [545, 743],  # Rome
                    [901, 126]]) # Warsaw

# Matriz de adjacência
n = len(city_list)
matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        matrix[i][j] = np.linalg.norm(city_list[i] - city_list[j])

# Usando um dos algoritmos de eurísticas conwtrutivas para ter uma rota
route, _ = nearest_neighbor(matrix)

########## GIF 2-opt ############

# Aplicando o algoritmo 2-opt para melhorar a rota
_, list_routes = two_opt(matrix, route)

# Configurando a figura para a animação
fig, ax = plt.subplots()

def update(frame):
    route = list_routes[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.set_title(f'Route {frame}')

# Criando a animação
ani = FuncAnimation(fig, update, frames=len(list_routes), repeat=False)

# Salvando a animação
ani.save('animation2_OPT.gif', writer='imagemagick', fps=1)

########## GIF 3-opt ############

_, list_routes3 = three_opt(matrix, route)


fig, ax = plt.subplots()

def update(frame):
    route = list_routes3[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(list_routes3), repeat=False)

ani.save('animation3_OPT.gif', writer='imagemagick', fps=1)