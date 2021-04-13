import numpy as np
from random import randrange
import heapq
import time

goalMatrix = np.reshape(np.array([1,2,3,4,5,6,7,8,0]), (3,3))
goalMatrixIndices = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]]

unvisited = []
visiteddict = {}

easy = np.reshape(np.array([4, 1, 3, 7, 2, 6, 0, 5, 8]), (3,3))     ##### easy with 6 moves
medium = np.reshape(np.array([7, 2, 4, 5, 0, 6, 8, 3, 1]), (3,3))     ##### medium 20 moves
hard1 = np.reshape(np.array([6, 4, 7, 8, 5, 0, 3, 2, 1]), (3,3))     ##### difficult 31 moves
hard2 = np.reshape(np.array([8, 6, 7, 2, 5, 4, 3, 0, 1]), (3,3))     ##### difficult 31 moves

class node:
    def __init__(self, mat, level):
        self.mat = mat
        self.hval = h2(self.mat)
        self.level = level
        self.fval = self.hval + self.level
        self.unique = self.mat[2][2] + self.mat[2][1]*10 + self.mat[2][0]*100 + self.mat[1][2]*1000 + self.mat[1][1]*10000 + self.mat[1][0]*100000 + self.mat[0][2]*1000000 + self.mat[0][1]*10000000 + self.mat[0][0]*100000000
    
    # Returns an array of coordinates of the movable squares
    def get_moves(self):
        
        # Get empty square coordinates
        blank_tile = np.argwhere(self.mat == 0)[0]
        
        # Generate tree of new boards from the possible moves
        moves = [blank_tile + [0, -1], blank_tile + [0, 1], blank_tile + [-1, 0], blank_tile + [1, 0]]
        children = []

        for move in moves:
            if(legal_move(move)):
                board = make_move(self.mat, move)
                child = node(board, self.level+1)
                if(never_visited(child)):
                    children.append(child)

        return children
    
    def __lt__(self, other):
        return (self.fval < other.fval)

def legal_move(move):
    return (move[0] >= 0 and move[0] < 3 and move[1] >= 0 and move[1] < 3)

# Traversing the list backwards is more efficient
def never_visited(node):
    if node.unique in visiteddict:
        return False
    return True

def make_move(mat,move):
    temp = mat.copy()
    blank_tile = np.argwhere(temp == 0)[0]
    temp[blank_tile[0]][blank_tile[1]] = temp[move[0]][move[1]]
    temp[move[0]][move[1]] = 0
    return temp

# h1: Count number of misplaced tiles
def h1(curr_mat):
    distance = 0

    for row in range(3):
        for col in range(3):
            if curr_mat[row][col] != goalMatrix[row][col] and curr_mat[row][col] != 0:
                distance += 1

    #distance = np.sum(curr_mat != goalMatrix)

    return distance

# h2: Calculate manhattan distance to solution
def h2(curr_mat):
    
    distance = 0
    for row in range(3):
        for col in range(3):
            if curr_mat[row][col] != 0:
                i = curr_mat[row][col]
                goalpos = goalMatrixIndices[i]
                distance += abs(row - goalpos[0]) +  abs(col - goalpos[1])
    return distance

# Main function
# Prepare initial state
startMatrix = hard2
initailBoard = node(startMatrix, 0)
heapq.heappush(unvisited, initailBoard)

print("Start matrix: ")
print(startMatrix)


#Loop
tic = time.time()
while(True):
    current = heapq.heappop(unvisited)

    # print("Distance to solution:", current.hval)
    
    # Check if solution is found
    if(current.hval == 0):
        print("Solution found in", current.level, "moves and", time.time() - tic, "seconds.")
        break
    
    # Generate new boards
    for newBoard in current.get_moves():
        heapq.heappush(unvisited, newBoard)

    #Move current node from unvisited to visited list
    visiteddict[current.unique] = current