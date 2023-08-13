# 2048 Game

import copy
import random
import time

class game():
    #Initialize the game
    def __init__(self, startTilesAmount):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.moveCount = 0
        self.didChange = True
        self.isGameOver = False
        for i in range(startTilesAmount):
            self.add_random_tile()

    #Add a random tile to the board
    def add_random_tile(self):
        #Find a random empty tile
        empty_tiles = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty_tiles.append([i,j])
        if len(empty_tiles) == 0:
            return False
        random_tile = random.choice(empty_tiles)
        #Add a 2 or 4 to the tile
        if random.random() < 0.9:
            self.board[random_tile[0]][random_tile[1]] = 2
        else:
            self.board[random_tile[0]][random_tile[1]] = 4
        return True

    #Check if the game is over
    def is_game_over(self):
        #Check if there are any empty tiles
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
        #Check if there are any adjacent tiles with the same value
        for i in range(4):
            for j in range(4):
                if i < 3 and self.board[i][j] == self.board[i+1][j]:
                    return False
                if j < 3 and self.board[i][j] == self.board[i][j+1]:
                    return False
        return True

    #Move the tiles up
    def move_up(self):
        boardBefore = copy.deepcopy(self.board)

        #Move the tiles
        for i in range(1, 4):
            for j in range(4):
                if self.board[i][j] != 0:
                    k = i
                    while k > 0 and self.board[k - 1][j] == 0:
                        self.board[k - 1][j] = self.board[k][j]
                        self.board[k][j] = 0
                        k -= 1
        for j in range(4):
            for i in range(3):
                if self.board[i][j] == self.board[i + 1][j]:
                    self.board[i][j] *= 2
                    self.board[i + 1][j] = 0
                    self.score += self.board[i][j]
        for i in range(1, 4):
            for j in range(4):
                if self.board[i][j] != 0:
                    k = i
                    while k > 0 and self.board[k - 1][j] == 0:
                        self.board[k - 1][j] = self.board[k][j]
                        self.board[k][j] = 0
                        k -= 1
        
        if (boardBefore == self.board):
            self.didChange = False
        else:
            self.didChange = True
            self.moveCount += 1

    #Move the tiles down
    def move_down(self):
        boardBefore = copy.deepcopy(self.board)

        #Move the tiles
        for i in range(2, -1, -1):
            for j in range(4):
                if self.board[i][j] != 0:
                    k = i
                    while k < 3 and self.board[k + 1][j] == 0:
                        self.board[k + 1][j] = self.board[k][j]
                        self.board[k][j] = 0
                        k += 1
        for j in range(4):
            for i in range(2, -1, -1):
                if self.board[i][j] == self.board[i + 1][j]:
                    self.board[i + 1][j] *= 2
                    self.board[i][j] = 0
                    self.score += self.board[i + 1][j]
        for i in range(2, -1, -1):
            for j in range(4):
                if self.board[i][j] != 0:
                    k = i
                    while k < 3 and self.board[k + 1][j] == 0:
                        self.board[k + 1][j] = self.board[k][j]
                        self.board[k][j] = 0
                        k += 1

        if (boardBefore == self.board):
            self.didChange = False
        else:
            self.didChange = True
            self.moveCount += 1

    #Move the tiles left
    def move_left(self):
        boardBefore = copy.deepcopy(self.board)
        
        #Move the tiles
        for j in range(1, 4):
            for i in range(4):
                if self.board[i][j] != 0:
                    k = j
                    while k > 0 and self.board[i][k - 1] == 0:
                        self.board[i][k - 1] = self.board[i][k]
                        self.board[i][k] = 0
                        k -= 1
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j + 1]:
                    self.board[i][j] *= 2
                    self.board[i][j + 1] = 0
                    self.score += self.board[i][j]
        for j in range(1, 4):
            for i in range(4):
                if self.board[i][j] != 0:
                    k = j
                    while k > 0 and self.board[i][k - 1] == 0:
                        self.board[i][k - 1] = self.board[i][k]
                        self.board[i][k] = 0
                        k -= 1

        if (boardBefore == self.board):
            self.didChange = False
        else:
            self.didChange = True
            self.moveCount += 1

    #Move the tiles right
    def move_right(self):
        boardBefore = copy.deepcopy(self.board)
        
        #Move the tiles
        for j in range(2, -1, -1):
            for i in range(4):
                if self.board[i][j] != 0:
                    k = j
                    while k < 3 and self.board[i][k + 1] == 0:
                        self.board[i][k + 1] = self.board[i][k]
                        self.board[i][k] = 0
                        k += 1
        for i in range(4):
            for j in range(2, -1, -1):
                if self.board[i][j] == self.board[i][j + 1]:
                    self.board[i][j + 1] *= 2
                    self.board[i][j] = 0
                    self.score += self.board[i][j + 1]
        for j in range(2, -1, -1):
            for i in range(4):
                if self.board[i][j] != 0:
                    k = j
                    while k < 3 and self.board[i][k + 1] == 0:
                        self.board[i][k + 1] = self.board[i][k]
                        self.board[i][k] = 0
                        k += 1
        
        if (boardBefore == self.board):
            self.didChange = False
        else:
            self.didChange = True
            self.moveCount += 1

    def update(self):
        addResult = False
        if (self.didChange):
            addResult = self.add_random_tile()
        if (not addResult and self.is_game_over()):
            self.isGameOver = True
        self.didChange = True

    
    def getCheckVars(self):
            return {"didChange":self.didChange,"isGameOver":self.isGameOver}

    def getScore(self):
        return self.score

    def getBoard(self):
        return self.board

    def getMoveCount(self):
        return self.moveCount

