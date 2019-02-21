#from array import *
import sys

filetxt = open("peas.txt","r")
peas = list(filetxt.read())
filetxt.close()
filetxt = open("mouse.txt","r")
mouse = list(filetxt.read())
filetxt.close()

#marks the beginning of the string, and aligns the text for 
#the algorigm to look nicer
peas.insert(0,"$")
mouse.insert(0,"$")

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
for y in range(1,len(mouse)):
    for x in range(1,len(peas)):
        if proteins[0][x] == proteins[1][y]:    #if matching
            graph[y][x] = graph[y-1][x-1] + 1
        else:                                   #if not matching, check they arent outside range, on last one 
            graph[y][x] = max(graph[y-1][x-1],      #diagonal
                                graph[y][x-1],      #left
                                graph[y-1][x]) -1   #up
            

#print(graph[len(mouse)][len(peas)]) #test TODO work in progress, check ends of graph

class bio:
    #variables for keeping the score
    matching = 0
    gap = 0
    mismatch = 0
    

    #coordinate of the traversing index through the graph
    traverseX = len(peas)-1
    traverseY = len(mouse)-1

    #resuting string that shows alignment, saved in reverse
    peas_string = "" #x axis
    mouse_string = "" #y axis

    def display_results(self):
        print(self.peas_string[::-1])
        print(self.mouse_string[::-1])

        print("\nMatching: %s \nMismatches: %s \nGaps: %s" % 
                        (self.matching, self.mismatch, self.gap))



#where all the scoring will be stored for simplcity of this program
bio = bio()


#backtracking through the graph, picking the greatest number every time using recursion
#TODO make it so that you have functions that will access the graph instead
#of having things like [x-1] to make things more readable
#will revisit once I have more time and not everything due on the same night.
def find_lower(x = bio.traverseX , y = bio.traverseY):

    if y-1 < 0 and x-1 < 0:     #check if youre going out of bounds manually
        return None             #once you reach the corner, youre at the base case

    else:                       #need to check if youre at the edge since array when negative
        if y-1 < 0 and x-1 >= 0: #checks if youre are the top edge, vertical gap
            bio.peas_string += proteins[0][x]
            bio.gap += 1
            return find_lower(x-1,y)

        elif y-1 >= 0 and x-1 < 0: #checks if youre at the left edge, horozintal gap
            bio.mouse_string += proteins[1][y]
            bio.gap +=1
            return find_lower(x,y-1)

        else:                   #then youre in the middle of the graph
            upper = graph[y-1][x]
            left = graph[y][x-1]
            diagonal = graph[y-1][x-1]
            ans = max(upper, left, diagonal)

            #checks if youre matching in the middle of the graph
            if ans == diagonal and proteins[0][x] == proteins[1][y]:
                bio.matching += 1
                bio.mouse_string += proteins[1][y]
                bio.peas_string += proteins[0][x]
                #print("match was found! it was: " + proteins[0][x-1] + " and " + proteins[1][y-1])
                #print("which is index: x=%d and y=%d" % (x-1,y-1))
                return find_lower(x-1,y-1)

            #checks if they are mismatching in the middle of the graph
            elif ans == diagonal and proteins[0][x] != proteins[1][y]:
                bio.mismatch += 1
                bio.mouse_string += proteins[1][y]
                bio.peas_string += proteins[0][x]
                return find_lower(x-1,y-1)

            #checks if your left is biggest
            elif ans == left:
                bio.gap += 1
                bio.mouse_string += "-"
                bio.peas_string += proteins[0][x]
                return find_lower(x-1,y)

            #checks if upper is biggest
            elif ans == upper:
                bio.gap +=1
                bio.mouse_string += proteins[1][y]
                bio.peas_string += "-"
                return find_lower(x,y-1)

            else:
                print("you done fucked up you done fucked up you done fucked up you done fucked up ")
                return None #it will quit out if you fucked up


#final output of the results
find_lower()
bio.display_results()
score = bio.matching - (bio.mismatch + bio.gap)
print("Score: %s" % score)


