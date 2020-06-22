import networkx as nx
import matplotlib.pyplot as plt
import logging
from logging import handlers
import sys

# 日志输出 log4j对中文过敏
class Logger(object):
    # 日志级别关系映射
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    def __init__(self, filename="D:/PythonProjects/learnpytorch/log/test2.log", level="info", when="D", backupCount=3,
                 fmt="%(asctime)s - %(pathname)s[line:%(lineno)d] - %"
                     "(levelname)s: %(message)s"):
        # 设置日志输出格式
        format_str = logging.Formatter(fmt)
        # 设置日志在控制台输出
        streamHandler = logging.StreamHandler()
        # 设置控制台中输出日志格式
        streamHandler.setFormatter(format_str)
        # 设置日志输出到文件（指定间隔时间自动生成文件的处理器  --按日生成）
        # filename：日志文件名，interval：时间间隔，when：间隔的时间单位， backupCount：备份文件个数，若超过这个数就会自动删除
        fileHandler = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backupCount,
                                                        encoding="utf-8")
        # 设置日志文件中的输出格式
        fileHandler.setFormatter(format_str)
        # 设置日志输出文件
        self.logger = logging.getLogger(filename)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 将输出对象添加到logger中
        self.logger.addHandler(streamHandler)
        self.logger.addHandler(fileHandler)
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
log = Logger(level="debug").logger
# if count > 1 and min_length > 3:
log.info("filename:" + sys.argv[1])
log.debug("min_length:" + str(min_length))
log.warning("count:" + str(count))
log.error("λ:"+sys.argv[2])
print('count:{}'.format(count))


