import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import math
from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        self.dimensions = None
        self.graph = None

    def distance(self, point1, point2):
        distance_x = abs(point1[0]-point2[0])
        distance_y = abs(point1[1]-point2[1])
        return math.gcd(distance_x, distance_y)

    def centre_dimensions(self, dimensions):
        # Make dimensions mutable
        dimensions = list(dimensions)

        # So that the centre is centred
        if dimensions[0] % 2 == 0:
            dimensions[0] += 1
        if dimensions[1] % 2 == 0:
            dimensions[1] += 1

        return tuple(dimensions)

    @abstractmethod
    # The locus of points definition, i.e. whether a point at (x, y) lies in the set of points that make up the shape.
    def locus(self, x, y):
        return False

    def render(self, dimensions=None):
         # dimensions is a tuple (or list, if you must) with the format (width, height).
        if not dimensions:
            dimensions = (100, 100) # default value
        self.dimensions = self.centre_dimensions(dimensions)

        self.center_to_edge = (int(self.dimensions[0]/2), int(self.dimensions[1]/2)) # Again with the format (x_length, y_length)

        # center_to_edge is an object variable because it will be used in draw().
        self.graph = np.zeros([self.dimensions[1], self.dimensions[0]])

        for y in tqdm(range(-self.center_to_edge[1], self.center_to_edge[1]+1)):
            for x in range(-self.center_to_edge[0], self.center_to_edge[0]+1):
                if self.locus(x, y):
                    self.graph[y+self.center_to_edge[1]][x+self.center_to_edge[0]] = 1

        return self.graph

    def draw(self, dimensions=None):
        if not dimensions:
            if not self.graph: # if render() has not been called, since dimensions are only ever set in render()
                self.render() # render with defaults
            # else, just draw what has already been rendered.
        else: # if dimensions were specified
            if self.centre_dimensions(dimensions) != self.dimensions:
            # if the new dimensions are different from what has already been rendered,
            # or if dimensions have not been rendered (i.e self.dimensions == None)
                self.render(dimensions) # rerender with new dimensions.
            # else, there has been no change in dimensions, so draw what has already been rendered.

        fig, ax = plt.subplots()
        ax.imshow(self.graph, cmap='Blues', origin='lower',extent=(-self.center_to_edge[0]-0.5, self.center_to_edge[0]+0.5, -self.center_to_edge[1]-0.5, self.center_to_edge[1]+0.5))
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.tight_layout()
        plt.show()

class Circle(Shape):

    def __init__(self, radius=1, center=(0,0)): # I should probably get rid of the options argument here, as it does not need to be defined until the shape becomes a rendered shape, which only occurs when render() is called.
        self.radius = radius
        self.center = center
        super().__init__()

    def locus(self, x, y):
        return self.distance(self.center, (x,y)) == self.radius

class Ellipse(Shape):
    def __init__(self, focus1=(-1,0), focus2=(1,0), major_axis=4, dimensions=None):
        self.foci = (focus1, focus2)
        self.major_axis = major_axis
        self.dimensions = dimensions
        if not self.dimensions:
            super().__init__()

    def distance(self, point1, point2):
        return super().distance(point1, point2)
#
#
#
#
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
