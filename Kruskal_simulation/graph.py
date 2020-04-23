from collections import defaultdict
import random


class Graph:

    V=0
    graph=[]
    def __init__(self , vert):
        self.V = vert
        self.graph=[]
    def addEdge(self,u,v,w):

        self.graph.append([u,v,w])

    def printGraph(self):
        print("Vertices : " + str(self.V))
        print(self.graph)

    def edge_No(self):
        return len(self.graph)
    def find(self,parent,i):

        if(parent[i]==i):

            return i

        return self.find(parent, parent[i])

    def union(self,parent,rank,x,y):

        xroot=self.find(parent,x)

        yroot=self.find(parent,y)

        if(rank[xroot] < rank[yroot]):
            parent[xroot] = yroot

        elif(rank[xroot] > rank[yroot]):

            parent[yroot] = xroot

        else:

            parent[yroot] = xroot

            rank[xroot] += 1

    def KruskalMST(self):

        result = []

        i=0

        e=0

        self.graph = sorted(self.graph,key=lambda item:item[2])

        parent,rank = [],[]

        for node in range(self.V):

            parent.append(node)

            rank.append(0)

        while(e < self.V-1):

            u,v,w = self.graph[i]

            i+=1

            x = self.find(parent, u)

            y = self.find(parent, v)

            if(x != y):

                e+=1

                result.append([u,v,w])

                self.union(parent, rank, x, y)

        return  result

    def printMST(self):
        result = self.KruskalMST()
        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))

    def MST_weight(self):
        result = self.KruskalMST()
        sum = 0
        for u, v, weight in result:
            sum+=weight
        return ("Weight of MST " + str(sum))

n=100
m=1500
for i in range(m):
    u = random.randint(0,99)
    v=  random.randint(0,99)
    w = random.randint(-1000 , 10000)
    print(str(u)+" " ,end="")
    print(str(v) + " ", end="")
    print(w)