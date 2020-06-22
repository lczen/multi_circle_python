import networkx as nx
import matplotlib.pyplot as plt
import logging
from logging import handlers
import sys
filename = "D:/PythonProjects/learnpytorch/vertices.txt"
f = open(filename)
lines = f.readlines()
vertices = []
edges = []
edges_list = []
for line in lines:
    if ':' in str(line):
        edge = str(line).replace("\n", "").split(":")
        edges.append((edge[0],edge[1]))
        edges_list.append(edge[0]+":"+edge[1])
    else:
        vertices.append(str(line).replace("\n", ""))

# print('vertices:'+','.join(str(i) for i in vertices))
# print('edges:'+','.join(str(i) for i in edges))
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
count = 0
min_length = 1000
for c in nx.connected_components(G):
#这里统计一下，每个连通部分的，边的数量。如果差距不是很大，那么把该边写入日志。得从java传参数过来
    count_min = 0
    count =count + 1
    nodeSet = G.subgraph(c).nodes()
    edgeSet = list(G.subgraph(c).edges())
    i_str = str(count)
    filename = 'D:/PythonProjects/learnpytorch/vertex_edge/'+i_str + '.txt'
    f = open(filename, 'w')
    for node in nodeSet:
        f.write(node+"\n")
    for subedge in edgeSet:
        #因为边的方向会发生改变，这里处理一下。改正边的方向
        if subedge[0]+':'+subedge[1] not in edges_list and subedge[1]+':'+subedge[0] in edges_list:
            f.write(subedge[1]+':'+subedge[0] + "\n")
        else:
            f.write(subedge[0] + ':' + subedge[1] + "\n")
        count_min+=1
    if min_length > count_min:
        min_length = count_min
    f.close()
#print('count:{}'.format(count))


