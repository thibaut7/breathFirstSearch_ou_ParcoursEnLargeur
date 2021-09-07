# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:44:45 2021

@author: thibaut
Breath-first Search
"""
from collections import defaultdict
class Graph:
    
    def  __init__(self):
        self.graph = defaultdict(list)
        
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    
    
    def breathFirstSearch(self, s):
         visited = [False]*(len(self.graph) )
         l = ["inf"]*(len(self.graph) )
         
         queue = []
         queue.append(s) 
         visited[s] = True
         l[s] = 0
         while queue:
             
             s = queue.pop(0)
             print(s  ,  l[s], " ")
             for i in self.graph[s]:
                 if visited[i] == False:
                     queue.append(i)
                     visited[i] = True
                     l[i] = l[s] + 1
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.breathFirstSearch(2)