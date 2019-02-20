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

#algorithm using loops
for y in range(len(mouse)):
    for x in range(len(peas)):
        if proteins[0][x] == proteins[1][y]:    #if matching
            graph[y+1][x+1] = graph[y][x] + 1
        else:                                   #if not matching
            graph[y+1][x+1] = max(graph[y][x],      #diagonal
                                graph[y+1][x],      #left
                                graph[y][x+1]) -1   #up
            

#print(graph[len(mouse)][len(peas)]) #test TODO work in progress, check ends of graph

class bio:
    #variables for keeping the score
    matching = 0
    gap = 0
    mismatch = 0
    score = matching + gap + mismatch

    #coordinate of the traversing index through the graph
    traverseX = len(peas)
    traverseY = len(mouse)

    #resuting string that shows alignment, saved in reverse
    peas_string = "" #x axis
    mouse_string = "" #y axis

    def display_results(self):
        print(self.peas_string)
        print(self.mouse_string)

        print("\nMatching: %s \nMismatches: %s \nGaps: %s \nScore: %s" % 
                        (self.matching, self.mismatch, self.gap, self.score))



#where all the scoring will be stored for simplcity of this program
bio = bio()



#backtracking through the graph, picking the greatest number every time
def find_lower(x = bio.traverseX , y = bio.traverseY):

    if y-1 < 0 and x-1 < 0:     #check if youre going out of bounds manually
        return None             #once you reach the corner, youre at the base case

    else:
        if y-1 < 0 and x-1 > 0: #checks if youre are the top edge, vertical gap
            bio.peas_string += proteins[0][x]
            return find_lower(x-1,y)
            
        elif y-1 > 0 and x-1 < 0: #checks if youre at the left edge, horozintal gap
            bio.mouse_string += proteins[1][y]
            return find_lower(x,y-1)
        else:
            None


#print(graph[0][0])  

#start at 1,1 and recurse down the graph
#if matching then diagonal +1
#check up, left and diagonally for max, then -1 it


#grading, run back through the graph optimally
#if diagonal and matching, matches +1, score +1
#if diagonal but not matching, mismatches+gap +1, score -1
#if left or up are max, mismatchesgap +1, score -1

#print it out