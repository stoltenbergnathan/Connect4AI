from random import choice, randint, random
from board import Board
import numpy as np

COL = 7
ROW = 6

EMPTY = 0
P1 = 1
P2 = 2

MAX = 1
MIN = 0

class MinMax():
  def __init__(self, strategy, player) -> None:
    self.board = None
    self.player = player
    if strategy:
      self.strat = MAX
    else:
      self.strat = MIN
    return
  
  # returns a list of all possible column moves
  def possibleMoves(self):
    moves = []
    for col in range(COL):
      if self.board[ROW - 1][col]:
        moves.append(col)

    return moves
  
  # returns the total reward for this board state
  def getReward(self, board):
    reward = 0

    middleArray = [int(i) for i in list(board[:, COL//2])]
    middleCount = middleArray.count(self.player)
    reward += middleCount * 2

    for row in range(ROW):
      rows = [int(i) for i in list(board[row, :])]
      for col in range(COL - 3):
        section = rows[col:col + 4]
        reward += self.getStrat(section)
    
    for col in range(COL):
      cols = [int(i) for i in list(board[:, col])]
      for row in range(ROW - 3):
        section = cols[row:row + 4]
        reward += self.getStrat(section)
    
    for row in range(ROW):
      for col in range(COL - 3):
        section = [board[row + i][col + i] for i in range(4)]
        reward += self.getStrat(section)

    for col in range(COL):
      for row in range(ROW - 3):
        section = [board[row + 3 - i][col + i] for i in range(4)]
        reward += self.getStrat(section)
    
    return reward
  
  # pick best move possible
  def pickMove(self):
    moves = self.possibleMoves()
    
    rewardBest = -np.Infinity
    colBest = 0

    row = 0
    for col in moves:
      board = Board(self.board)
      board.placeTile(self.player, col)
      reward = self.getReward(board)
      if reward > rewardBest:
        rewardBest = reward
        colBest = col
    
    return colBest

  # scores the current board section and returns a reward value based on that
  def getStrat(self, section):
    score = 0
    opponent = P1
    if self.player == P1:
      opponent = P2
    if section.count(self.player) == 4:
      score += 50
    if section.count(self.player) == 3 and section.count(EMPTY) == 1:
      score += 10
    if section.count(self.player) == 2 and section.count(EMPTY) == 2:
      score += 3
    if section.count(opponent) == 3 and section.count(EMPTY) == 1:
      score -= 6
    return score
      
  # function on enter, copies the board and begins the minMax algorithm
  def play(self, board):
    self.board = board
    col, val = self.minMax(self.board, 4, -np.Infinity, np.Infinity) # 0-6
    return col
    
  def minMax(self, board, depth, a, b):
    validMoves = self.possibleMoves()
    
    opponent = P1
    if self.player == P1:
      opponent = P2
      
    if board.isWinner(self.player):
      return(None, 1000000)
    elif board.isWinner(opponent):
      return(None, -1000000)
    elif self.board.full():
      return(None, 0)
      
    if self.strat == MAX:
      score = -np.Infinity
      col = random.choice(validMoves)
      for c in validMoves:
        tempBoard = board.copy()
        self.board.placeTile(self.player, c)
        newScore = self.minMax(tempBoard, depth-1, a, b)[1]
        if newScore > score:
          score = newScore
          col = c
        b = max(b, score)
        if a >= b:
          break
        return col, score
    else:
      score = np.Infinity
      col = random.choice(validMoves)
      for c in validMoves:
        tempBoard = board.copy()
        self.board.placeTile(self.player, c)
        newScore = self.minMax(tempBoard, depth-1, a, b)[1]
        if newScore < score:
          score = newScore
          col = c
        b = min(b, score)
        if a >= b:
          break
        return col, score      

        