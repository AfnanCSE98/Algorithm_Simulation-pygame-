import random

import pygame
from graph import Graph
#reading from file and creating the graph
array=[]
with open('input.txt') as f:
    vertices = [int(x) for x in next(f).split()]
    array = [[int(x) for x in line.split()] for line in f]
    no_of_edges = len(array)
N=vertices[0]
g = Graph(N)
for e in array:
    g.addEdge(e[0] , e[1] , e[2])
g.KruskalMST()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location

pygame.init()

# Set the HEIGHT and WIDTH of the screen
screen_w=800
screen_h=650

WINDOW_SIZE = [screen_w , screen_h]


screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Kruskal's MST")


# Used to manage how fast the screen updates
clock = pygame.time.Clock()
screen.fill(WHITE)

list1 = random.sample(range(70 , screen_h-70) , N)
list2 = random.sample(range(70 , screen_h-70) , N)

font = pygame.font.Font('freesansbold.ttf', 12)
#drawing nodes
def drawNode():
    for r in range(N):
        pygame.draw.circle(screen, BLACK, (list1[r], list2[r]), 8, 0)
        text = font.render(str(r), True, RED)
        textRect = text.get_rect()
        textRect.center = (list1[r], list2[r])
        screen.blit(text , textRect)

def writeMST(str,x,y):
    text = font.render(str, True, BLACK)
    textRect = text.get_rect()
    textRect.center = (x , y)
    screen.blit(text, textRect)

#drawing the edges
def drawEdges():
    for i in range(g.edge_No()):
        u = g.graph[i][0]
        v = g.graph[i][1]
        pygame.draw.line(screen, GREEN, (list1[u], list2[u]), (list1[v], list2[v]), 1)

def removeEdgesAfterMSTDrawn():
    result = g.KruskalMST()
    for i in range(g.edge_No()):
        u = g.graph[i][0]
        v = g.graph[i][1]
        w = g.graph[i][2]
        if(result.__contains__([u,v,w]) == False):
            pygame.draw.line(screen, WHITE, (list1[u], list2[u]), (list1[v], list2[v]), 1)

def drawMST():
    j=0
    while(j < len(mst)):
        u = mst[j][0]
        v = mst[j][1]
        pygame.draw.line(screen, (0, 0, 255), (list1[u], list2[u]), (list1[v], list2[v]), 4)
        j = j+1
        drawNode()


drawEdges()
drawNode()
mst = g.KruskalMST()
g.printMST()
g.MST_weight()
writeMST("Edges    Weight" , screen_w-100 , 30)


# -------- Main Program Loop -----------
done = False
i=0
low_h=45

while not done:

    for event in pygame.event.get() :  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    if(i<len(mst)):
        u = mst[i][0]
        v = mst[i][1]
        w = mst[i][2]
        pygame.draw.line(screen, (0, 0, 255), (list1[u], list2[u]), (list1[v], list2[v]), 4)
        drawNode()

        writeMST(str(u)+" -> " + str(v) + "      : " + str(w)  ,  screen_w-130 , low_h)

    i = i + 1
    low_h+=15
    if(i==len(mst)):
        removeEdgesAfterMSTDrawn()
        drawMST()#draw mst again to make sure no overlapping of color
        drawNode()
        writeMST(g.MST_weight() , screen_w-(screen_w/2) , 20)

    clock.tick(0.7)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()