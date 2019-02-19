from array import *

filetxt = open("peas.txt","r")
peas = list(filetxt.read())
filetxt.close()
filetxt = open("mouse.txt","r")
mouse = list(filetxt.read())
filetxt.close()

#makes an array with every character seperated 
map = [peas, mouse]

# graph of peas x mouse array of ints 
graph = [[int for i in range(len(peas))] for j in range(len(mouse))]

#initializes the graph with the initial base cases with 0, -1, -2, ...
for i in range(len(mouse)):
    graph[i][0] = -i
for i in range(len(peas)):
    graph[0][i] = -i


#start at 1,1 and recurse down the graph
#if matching then diagonal +1
#check up, left and diagonally for max, then -1 it


#grading, run back through the graph optimally
#if diagonal and matching, matches +1, score +1
#if diagonal but not matching, mismatches+gap +1, score -1
#if left or up are max, mismatchesgap +1, score -1

#print it out