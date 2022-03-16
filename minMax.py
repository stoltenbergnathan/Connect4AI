from random import choice, randint, random
from board import Board
import numpy as np

COL = 7
ROW = 6

EMPTY = 0
P1 = 1
P2 = 2

MAX = True
MIN = False

DEPTH = 6
INF = np.Infinity

class MinMax():
  def __init__(self, strategy, player) -> None:
    self.board = Board(None)
    self.player = player
    if strategy:
      self.strat = MAX
    else:
      self.strat = MIN
    return
  
  # returns a list of all possible column moves
  def possibleMoves(self, board):
    moves = []
    for col in range(COL):
      if board.state[0][col] == 0:
        moves.append(col)

    return moves
  
  # returns the total reward for this board state
  def getReward(self, board):
    reward = 0

    middleArray = [int(i) for i in list(board.state[:, COL//2])]
    middleCount = middleArray.count(self.player)
    reward += middleCount * 3

    for row in range(ROW):
      rows = [int(i) for i in list(board.state[row, :])]
      for col in range(COL - 3):
        section = rows[col:col + 4]
        reward += self.getStrat(section)
    
    for col in range(COL):
      cols = [int(i) for i in list(board.state[:, col])]
      for row in range(ROW - 3):
        section = cols[row:row + 4]
        reward += self.getStrat(section)
    
    for row in range(ROW - 3):
      for col in range(COL - 3):
        section = [board.state[row + i][col + i] for i in range(4)]
        reward += self.getStrat(section)

    for col in range(COL - 3):
      for row in range(ROW - 3):
        section = [board.state[row + 3 - i][col + i] for i in range(4)]
        reward += self.getStrat(section)
    
    return reward

  # scores the current board section and returns a reward value based on that
  def getStrat(self, section):
    score = 0

    opponent = P1
    if self.player == P1:
      opponent = P2

    if section.count(self.player) == 4:
      score += 100
    elif section.count(self.player) == 3 and section.count(EMPTY) == 1:
      score += 9
    elif section.count(self.player) == 2 and section.count(EMPTY) == 2:
      score += 5

    if section.count(opponent) == 3 and section.count(EMPTY) == 1:
      score -= 7
      
    return score
      
  # function on enter, copies the board and begins the minMax algorithm
  def play(self, board):
    self.board = Board(board.state)
    col, val = self.minMax(self.board, DEPTH, -INF, INF, self.strat) # 0-6
    return col
    
  def minMax(self, board, depth, a, b, maxOpp):
    validMoves = self.possibleMoves(board)
    
    opponent = P1
    if self.player == P1:
      opponent = P2

    if depth == 0:
      return (None, self.getReward(board))
      
    if maxOpp:
      score = -INF
      col = choice(validMoves)
      for c in validMoves:
        tempBoard = Board(board.state)
        tempBoard.placeTile(self.player, c)
        column, newScore = self.minMax(tempBoard, depth-1, a, b, False)
        if newScore > score:
          score = newScore
          col = c
        a = max(a, score)
        if a >= b:
          break
      return col, score
    else:
      score = INF
      col = choice(validMoves)
      for c in validMoves:
        tempBoard = Board(board.state)
        tempBoard.placeTile(opponent, c)
        column, newScore = self.minMax(tempBoard, depth-1, a, b, True)
        if newScore < score:
          score = newScore
          col = c
        b = min(b, score)
        if a >= b:
          break
      return col, score      

        