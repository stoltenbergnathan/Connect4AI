from board import Board

class State():
    def __init__(self, board, player) -> None:
        self.state = [0, 0, 0, 0, 0, 0, 0]
        self.player = player
        self.setState(board)
    
    def getValueCol(self, col) -> list:
        return self.state[col]
    
    def setState(self, board: Board) -> None:
        for col in range(len(self.state)):
            row = board.getHeight(col)
            if row == None:
                row = 0
            self.state[col] = self.getOne(board.state, row, col, self.player)
    
    def winner(self):
        for value in self.state:
            if value == 4:
                return True
        return False
    
    def getOne(self, board, row, col, player):
        total = 0
        # Look right
        addition = 1
        while True:
            if col + addition > 6:
                break
            if board[row][col + addition] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        # Look left
        addition = 1
        while True:
            if col - addition < 0:
                break
            if board[row][col - addition] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        # Up Diagonal
        # Look right
        addition = 1
        while True:
            if col + addition > 6 or row - addition < 0:
                break
            if board[row - addition][col + addition] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        # Look left
        addition = 1
        while True:
            if col - addition < 0 or row - addition < 0:
                break
            if board[row - addition][col - addition] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        # Down Diagonal
        # Look right
        addition = 1
        while True:
            if col + addition > 6 or row + addition > 5:
                break
            if board[row + addition][col + addition] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        # Look left
        addition = 1
        while True:
            if col - addition < 0 or row + addition > 5:
                break
            if board[row - addition][col - addition] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        # Look down
        addition = 1
        while True:
            if row + addition > 5 or row == 0:
                break
            if board[row + addition][col] == player:
                total += 1
                if total >= 4:
                    return total
                addition += 1
            else:
                break
        return total