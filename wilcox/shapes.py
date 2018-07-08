import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math
from abc import ABC, abstractmethod

class Shape(ABC):

    def distance(self, point1, point2):
        distance_x = abs(point1[0]-point2[0])
        distance_y = abs(point1[1]-point2[1])
        return math.gcd(distance_x, distance_y)

    @abstractmethod
    def render(self, dimensions):
        pass

    def draw(self, dimensions=None):
        if dimensions and dimensions != self.dimensions:
            self.render(dimensions)
        fig, ax = plt.subplots()
        ax.imshow(self.graph, cmap='Blues', origin='lower',extent=(-self.center_to_edge[0]-0.5, self.center_to_edge[0]+0.5, -self.center_to_edge[1]-0.5, self.center_to_edge[1]+0.5))
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.tight_layout()
        plt.show()

class Circle(Shape):

    def __init__(self, radius=1, center=(0,0), dimensions=None): # Surely there is a better variable name than "center_to_edge."
        self.radius = radius
        self.center = center
        self.dimensions = dimensions

    def distance(self, point1, point2):
        return super().distance(point1, point2)

    def render(self, dimensions):
        # dimensions is a tuple (or list, if you must) with the format (width, height).
        self.dimensions = list(dimensions)
        # So that the centre is centred:
        if self.dimensions[0] % 2 == 0:
            self.dimensions[0] += 1
        if self.dimensions[1] % 2 == 0:
            self.dimensions[1] += 1
        self.dimensions=tuple(self.dimensions)

        self.center_to_edge = (int(dimensions[0]/2), int(dimensions[1]/2)) # Again with the format (x_distance, y_distance)

        self.graph = np.zeros([self.dimensions[1], self.dimensions[0]])
        for y in tqdm(range(-self.center_to_edge[1], self.center_to_edge[1]+1)):
            for x in range(-self.center_to_edge[0], self.center_to_edge[0]+1):
                if self.distance(self.center, (x,y)) == self.radius:
                    self.graph[y+self.center_to_edge[1]][x+self.center_to_edge[0]] = 1

        # return graph

# def draw(graph,x_center_to_edge=x_distance, y_center_to_edge=y_distance):
#     fig, ax = plt.subplots()
#     ax.imshow(graph, cmap='Blues', origin='lower',extent=(-x_center_to_edge-0.5, x_center_to_edge+0.5, -y_center_to_edge-0.5, y_center_to_edge+0.5))
#     ax.xaxis.set_visible(False)
#     ax.yaxis.set_visible(False)
#     plt.tight_layout()
#     plt.show()
#
# def circle(radius=1, center=(0,0), x_center_to_edge=x_distance, y_center_to_edge=y_distance):
#     length_x = 2*x_center_to_edge + 1
#     length_y = 2*y_center_to_edge + 1
#     graph = np.zeros([length_y, length_x])
#     for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
#         for x in range(-x_center_to_edge, x_center_to_edge+1):
#             if distance(center, (x,y)) == radius:
#                 graph[y+y_center_to_edge][x+x_center_to_edge] = 1
#     draw(graph)
#
# # circle()
#
# def ellipse(focus1=(-1,0), focus2=(1,0), total_distance=2, x_center_to_edge=x_distance, y_center_to_edge=y_distance):
#     # total_distance is 2a, in the locus of points definition of a conic section.
#     length_x = 2*x_center_to_edge + 1
#     length_y = 2*y_center_to_edge + 1
#     graph = np.zeros([length_y, length_x])
#     for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
#         for x in range(-x_center_to_edge, x_center_to_edge+1):
#             if distance(focus1, (x,y)) + distance(focus2, (x,y)) == total_distance:
#                 graph[y+y_center_to_edge][x+x_center_to_edge] = 1
#     draw(graph)
#
# # ellipse((-10,0), (5,20), 2)
#
# def parabola(focus=(0,0), directrix=0, x_center_to_edge=x_distance, y_center_to_edge=y_distance):
#     length_x = 2*x_center_to_edge + 1
#     length_y = 2*y_center_to_edge + 1
#     graph = np.zeros([length_y, length_x])
#     for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
#         for x in range(-x_center_to_edge, x_center_to_edge+1):
#             if distance(focus, (x,y)) == abs(y-directrix):
#                 graph[y+y_center_to_edge][x+x_center_to_edge] = 1
#     draw(graph)
#
# # parabola((0,0), 0)
#
# def hyperbola(focus1=(-1,0), focus2=(1,0), total_distance=2, x_center_to_edge=x_distance, y_center_to_edge=y_distance):
#     length_x = 2*x_center_to_edge + 1
#     length_y = 2*y_center_to_edge + 1
#     graph = np.zeros([length_y, length_x])
#     for y in tqdm(range(-y_center_to_edge, y_center_to_edge+1)):
#         for x in range(-x_center_to_edge, x_center_to_edge+1):
#             if abs(distance(focus1, (x,y)) - distance(focus2, (x,y))) == total_distance:
#                 graph[y+y_center_to_edge][x+x_center_to_edge] = 1
#     draw(graph)
#
# # hyperbola(total_distance=20)
#
# # circle()
# # ellipse()
# # parabola()
# # hyperbola()
