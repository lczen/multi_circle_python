import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from Logger import Logger
filename = "D:/PythonProjects/learnpytorch/vertices.txt"
f = open(filename)
lines = f.readlines()
vertices = []
edges = []
edges_list = []
arcs = []
arcs_list = []
u = []
v = []
x = []
y = []
for line in lines:
    if ':' in str(line):
        edge = str(line).replace("\n", "").split(":")
        edges.append((edge[0],edge[1]))
        edges_list.append(edge[0]+":"+edge[1])
        vertex_zero = edge[0].split("_")[0]
        vertex_two = edge[0].split("_")[1]
        vertex_three = edge[1].split("_")[0]
        vertex_four = edge[1].split("_")[1]
        u.append([int(vertex_zero), int(vertex_three)])
        v.append([int(vertex_two), int(vertex_four)])
    elif '+' in str(line):
        arc = str(line).replace("\n", "").split("+")
        arcs.append((arc[0], arc[1]))
        arcs_list.append(arc[0] + ":" + arc[1])
        vertex_zero = arc[0].split("_")[0]
        vertex_two = arc[0].split("_")[1]
        vertex_three = arc[1].split("_")[0]
        vertex_four = arc[1].split("_")[1]
        x.append([int(vertex_zero), int(vertex_three)])
        y.append([int(vertex_two), int(vertex_four)])
    else:
        vertices.append(str(line).replace("\n", ""))
for i in range(len(u)):
    plt.plot(u[i], v[i], color='b')
    plt.scatter(u[i], v[i], color='y')
for i in range(len(x)):
    plt.plot(x[i], y[i], color='r')
    plt.scatter(x[i], y[i], color='y')
plt.show()
