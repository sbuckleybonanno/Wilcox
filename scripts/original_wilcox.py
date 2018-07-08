""" The original script written over a single night.
    The basic mathematical operations necessary to plot
    in this geometry were first made to work here, and
    have continued almost unchanged from this original
    incarnation                                         """

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math

x_distance = 250
y_distance = 250

# def distance(point1, point2): # Surely this can be optimized.
#     distance_x = abs(point1[0]-point2[0])
#     distance_y = abs(point1[1]-point2[1])
#     distance = 0
#     i = max(distance_x, distance_y)
#     while i > 0:
#         if distance_x % i == 0 and distance_y % i == 0:
#             distance_x -= distance_x / i
#             distance_y -= distance_y / i
#             distance += 1
#             i = max(distance_x, distance_y)
#         else:
#             i -= 1
#     return distance

def distance(point1, point2):
    distance_x = abs(point1[0]-point2[0])
    distance_y = abs(point1[1]-point2[1])
    return math.gcd(distance_x, distance_y)
    # distance = 0
    # i = min(distance_x, distance_y)
    # while i > 0:
    #     if distance_x % i == 0 and distance_y % i == 0:
    #         # print("i = " + str(i))
    #         # print("x = " + str(distance_x))
    #         # print("y = " + str(distance_y))
    #         # print("********")
    #
    #         # distance_x /=  i
    #         # distance_y /= i
    #         # distance += i
    #         # break
    #         return i
    #         # i = min(distance_x, distance_y)
    #     i -= 1
    # return distance

# print(distance((0,0), (1,8)))
# print(distance((0,0), (2,8)))
# print(distance((0,0), (3,8)))
# print(distance((0,0), (4,8)))
# print(distance((0,0), (5,8)))
# print(distance((0,0), (6,8)))
# print(distance((0,0), (7,8)))
# print(distance((0,0), (8,8)))


def draw(graph,x_center_to_edge=x_distance, y_center_to_edge=y_distance):
    fig, ax = plt.subplots()
    ax.imshow(graph, cmap='Blues', origin='lower',extent=(-x_center_to_edge-0.5, x_center_to_edge+0.5, -y_center_to_edge-0.5, y_center_to_edge+0.5))
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.tight_layout()
    plt.show()

def circle(radius=1, center=(0,0), x_center_to_edge=x_distance, y_center_to_edge=y_distance):
    length_x = 2*x_center_to_edge + 1
    length_y = 2*y_center_to_edge + 1
    graph = np.zeros([length_y, length_x])
    for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
        for x in range(-x_center_to_edge, x_center_to_edge+1):
            if distance(center, (x,y)) == radius:
                graph[y+y_center_to_edge][x+x_center_to_edge] = 1
    draw(graph)

# circle()

def ellipse(focus1=(-1,0), focus2=(1,0), total_distance=2, x_center_to_edge=x_distance, y_center_to_edge=y_distance):
    # total_distance is 2a, in the locus of points definition of a conic section.
    length_x = 2*x_center_to_edge + 1
    length_y = 2*y_center_to_edge + 1
    graph = np.zeros([length_y, length_x])
    for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
        for x in range(-x_center_to_edge, x_center_to_edge+1):
            if distance(focus1, (x,y)) + distance(focus2, (x,y)) == total_distance:
                graph[y+y_center_to_edge][x+x_center_to_edge] = 1
    draw(graph)

# ellipse((-10,0), (5,20), 2)

def parabola(focus=(0,0), directrix=0, x_center_to_edge=x_distance, y_center_to_edge=y_distance):
    length_x = 2*x_center_to_edge + 1
    length_y = 2*y_center_to_edge + 1
    graph = np.zeros([length_y, length_x])
    for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
        for x in range(-x_center_to_edge, x_center_to_edge+1):
            if distance(focus, (x,y)) == abs(y-directrix):
                graph[y+y_center_to_edge][x+x_center_to_edge] = 1
    draw(graph)

# parabola((0,0), 0)

def hyperbola(focus1=(-1,0), focus2=(1,0), total_distance=2, x_center_to_edge=x_distance, y_center_to_edge=y_distance):
    length_x = 2*x_center_to_edge + 1
    length_y = 2*y_center_to_edge + 1
    graph = np.zeros([length_y, length_x])
    for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
        for x in range(-x_center_to_edge, x_center_to_edge+1):
            if abs(distance(focus1, (x,y)) - distance(focus2, (x,y))) == total_distance:
                graph[y+y_center_to_edge][x+x_center_to_edge] = 1
    draw(graph)

# hyperbola(total_distance=20)

circle()
# ellipse()
# parabola()
# hyperbola()
