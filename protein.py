#from array import *

filetxt = open("peas.txt","r")
peas = list(filetxt.read())
filetxt.close()
filetxt = open("mouse.txt","r")
mouse = list(filetxt.read())
filetxt.close()

#makes an array with every character seperated 
proteins = [peas, mouse]

# graph of peas x mouse array of ints , added + 1 for the extra added columnn
graph = [[-9999 for i in range(len(peas)+1)] for j in range(len(mouse)+1)]

#initializes the graph with the initial base cases with 0, -1, -2, ...
for i in range(len(mouse)):
    graph[i][0] = -i
for i in range(len(peas)):
    graph[0][i] = -i

#algorithm
for y in range(len(mouse)):
    for x in range(len(peas)):
        if proteins[0][x] == proteins[1][y]:    #if matching
            graph[y+1][x+1] = graph[y][x] + 1
        else:                                   #if not matching
            graph[y+1][x+1] = max(graph[y][x],      #diagonal
                                graph[y+1][x],      #left
                                graph[y][x+1]) -1   #up
            


print(graph[2][40]) #test TODO work in progress, check ends of graph


#start at 1,1 and recurse down the graph
#if matching then diagonal +1
#check up, left and diagonally for max, then -1 it


#grading, run back through the graph optimally
#if diagonal and matching, matches +1, score +1
#if diagonal but not matching, mismatches+gap +1, score -1
#if left or up are max, mismatchesgap +1, score -1

#print it out