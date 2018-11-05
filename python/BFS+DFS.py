import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

# def vis(g):


def BFS(s, g):
    q = [] #create a queue to implememnt the BFS
    searched = []
    q.append(s)
    while q!=[]:
        x = q[0]
        q = q[1:] #pop the queue
        if not x in searched:
            searched.append(x)
            print "Now Reach: ", x
            for i in g[x]:
                q.append(i)
        

def DFS(searched, s, g): 
    searched.append(s)
    print "Now Reach: ", s
    for x in g[s]:
        if x not in searched:
            searched.append(x)
            DFS(searched, x, g)
    




graph = [ [1, 2], [0, 3, 4], [0, 5], [1], [1], [2, 6], [5]]
source = 0
searched = []

DFS(searched, source, graph)

