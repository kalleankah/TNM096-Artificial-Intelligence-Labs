import numpy as np
from random import randrange
import heapq
import time

goalMatrix = np.array([1,2,3,4,5,6,7,8,0])
goalMatrix = np.reshape(goalMatrix, (3,3))

unvisited = []
visited = []

easy = np.array([4, 1, 3, 7, 2, 6, 0, 5, 8])     ##### easy with 6 moves
medium = np.array([7, 2, 4, 5, 0, 6, 8, 3, 1])     ##### medium 20 moves
hard1 = np.array([6, 4, 7, 8, 5, 0, 3, 2, 1])     ##### difficult 31 moves
hard2 = np.array([8, 6, 7, 2, 5, 4, 3, 0, 1])     ##### difficult 31 moves

class node:
    def __init__(self, mat, level):
        self.mat = mat
        self.hval = h1(self.mat)
        self.level = level
        self.fval = self.hval + self.level
    
    # Returns an array of coordinates of the movable squares
    def getPossibleMoves(self):
        # Get empty square coordinates
        blankTile = np.argwhere(self.mat == 0)[0]
        
        # Generate tree of new boards from the possible moves
        moves = [blankTile + [0, -1], blankTile + [0, 1], blankTile + [-1, 0], blankTile + [1, 0]]
        children = []

        for move in moves:
            if(legalMove(move)):
                board = makeMove(self.mat, move)
                if(neverVisited(board)):
                    child = node(board, self.level+1)
                    children.append(child)

        return children
    
    def __lt__(self, other):
        return (self.fval < other.fval)

def legalMove(move):
    return (move[0] >= 0 and move[0] < 3 and move[1] >= 0 and move[1] < 3)

def neverVisited(board):
    for thing in visited:
        if(np.array_equal(board,thing.mat)):
            return False
    return True

def makeMove(mat,move):
    temp = mat.copy()
    blankTile = np.argwhere(temp == 0)[0]
    temp[blankTile[0]][blankTile[1]] = temp[move[0]][move[1]]
    temp[move[0]][move[1]] = 0
    return temp


# h1: Count number of misplaced tiles
def h1(currMat):
    distance = np.sum(currMat != goalMatrix)

    return distance

# h2: Calculate manhattan distance to solution
def h2(currMat):
    distance = 0

    for i in range(9):
        currpos = np.argwhere(currMat == i)[0]
        goalpos = np.argwhere(goalMatrix == i)[0]

        distance += abs(currpos[0] - goalpos[0]) +  abs(currpos[1] - goalpos[1])
    return distance

# Main function
# Prepare initial state
startMatrix = np.reshape(medium, (3,3))
board = node(startMatrix, 0)
heapq.heappush(unvisited, board)

print("Start matrix: ")
print(startMatrix)

loops = 0
#Loop
tic = time.time()
while(True):
    current = heapq.heappop(unvisited)

    # print("Distance to solution: ", current.hval)
    
    # Check if solution is found
    if(current.hval == 0):
        print("Solution found in", current.level, "moves and", time.time() - tic, "seconds.")
        print(current.mat)
        break
    
    # Generate new boards
    for newBoard in current.getPossibleMoves():
        heapq.heappush(unvisited, newBoard)

    #Move current node from unvisited to visited list
    visited.append(current)

    #Sort unvisited list by lowest fval
    #unvisited.sort(key = lambda node: node.fval, reverse = False)

    # print("current mat: ")
    # print(current.mat)
    # print("current fval: ", current.fval)
    # print("visited mat: ")
    # print(visited[loops].mat)
    # print("visited fval: ", visited[loops].fval)

    # print("unvisited mat: ")
    # print(unvisited[loops].mat)
    # print("unvisited fval: ", unvisited[loops].fval)

    # loops = loops+1
