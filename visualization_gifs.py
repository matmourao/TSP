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
ani.save('./img/animation2_OPT.gif', writer='imagemagick', fps=1)

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

ani.save('./img/animation3_OPT.gif', writer='imagemagick', fps=1)

########## GIF 2-opt vs 3-opt ############

fig, ax = plt.subplots()

def update(frame):
    route = list_routes[frame]
    route3 = list_routes3[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.plot(city_list[route3, 0], city_list[route3, 1], 'C1', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.scatter(city_list[route3, 0], city_list[route3, 1], zorder=2)
    ax.legend(['2-opt', '3-opt'])
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(list_routes), repeat=False)

ani.save('./img/animation2vs3_OPT.gif', writer='imagemagick', fps=1)


#### Utilizando savings #####

rota_2, _ = savings(matrix)


_, l2 = two_opt(matrix, rota_2)

fig, ax = plt.subplots()


def update(frame):
    route = l2[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(l2), repeat=False)

ani.save('./img/animation2_OPT_savings.gif', writer='imagemagick', fps=1)

_, l3 = three_opt(matrix, rota_2)

fig, ax = plt.subplots()

def update(frame):
    route = l3[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(l3), repeat=False)

ani.save('./img/animation3_OPT_savings.gif', writer='imagemagick', fps=1)


# comparando 2-opt e 3-opt
fig, ax = plt.subplots()

def update(frame):
    route = l2[frame]
    route3 = l3[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.plot(city_list[route3, 0], city_list[route3, 1], 'C1', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.scatter(city_list[route3, 0], city_list[route3, 1], zorder=2)
    ax.legend(['2-opt', '3-opt'])
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(l2), repeat=False)

ani.save('./img/animation2vs3_OPT_savings.gif', writer='imagemagick', fps=1)

### cheapest edge ###

rota_3, _ = cheapest_edge(matrix)

# 2-opt
_, l2_chped = two_opt(matrix, rota_3)

fig, ax = plt.subplots()

def update(frame):
    route = l2_chped[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(l2_chped), repeat=False)

ani.save('./img/animation2_OPT_cheapest_edge.gif', writer='imagemagick', fps=1)

# 3-opt
_, l3_chped = three_opt(matrix, rota_3)

fig, ax = plt.subplots()

def update(frame):
    route = l3_chped[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(l3_chped), repeat=False)

ani.save('./img/animation3_OPT_cheapest_edge.gif', writer='imagemagick', fps=1)

# comparando 2-opt e 3-opt
fig, ax = plt.subplots()

def update(frame):
    route = l2_chped[frame]
    route3 = l3_chped[frame]
    ax.clear()
    ax.imshow(image)  
    ax.plot(city_list[route, 0], city_list[route, 1], 'C0', zorder=1)
    ax.plot(city_list[route3, 0], city_list[route3, 1], 'C1', zorder=1)
    ax.scatter(city_list[route, 0], city_list[route, 1], zorder=2)
    ax.scatter(city_list[route3, 0], city_list[route3, 1], zorder=2)
    ax.legend(['2-opt', '3-opt'])
    ax.set_title(f'Route {frame}')

ani = FuncAnimation(fig, update, frames=len(l2_chped), repeat=False)

ani.save('./img/animation2vs3_OPT_cheapest_edge.gif', writer='imagemagick', fps=1)


