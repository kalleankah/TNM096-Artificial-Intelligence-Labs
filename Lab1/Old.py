# # Generate tree of new boards from the possible moves
#         children = []
#         if blank_tile[1] > 0:
#             board = make_move(self.mat, blank_tile + [0, -1])
#             if never_visited(board):
#                 children.append(node(board, self.level+1))

#         if blank_tile[1] < 2:
#             board = make_move(self.mat, blank_tile + [0, 1])
#             if never_visited(board):
#                 children.append(node(board, self.level+1))
        
#         if blank_tile[0] > 0:
#             board = make_move(self.mat, blank_tile + [-1, 0])
#             if never_visited(board):
#                 children.append(node(board, self.level+1))

#         if blank_tile[0] < 2:
#             board = make_move(self.mat, blank_tile + [1, 0])
#             if never_visited(board):
#                 children.append(node(board, self.level+1))

# def genStartMatrix():
#     mat = np.arange(9)
#     np.random.shuffle(mat)
#     # mat = np.array([1,2,3,0,4,6,7,5,8])
#     mat = np.reshape(mat, (3,3))

#     return mat

# # Begin from goal board and make random moves to shuffle the board
# def shuffleBoard(mat,steps):
        
#     for step in range(steps):
#         # Get empty square coordinates
#         blankTile = np.argwhere(mat == 0)[0]
        
#         # Generate tree of new boards from the possible moves
#         moves = [blankTile + [0, -1], blankTile + [0, 1], blankTile + [-1, 0], blankTile + [1, 0]]
#         validMoves = []
        
#         for move in moves:
#             if(move[0] >= 0 and move[0] < 3 and move[1] >= 0 and move[1] < 3):
#                 validMoves.append(move)

#         mat = genNewBoard(mat, validMoves[randrange(0, len(validMoves))])

#     return mat