import sys
from board import Board

gameBoard = Board()

# Change both player imputs to Agents
def getPlayer1Input() -> int:
    return int(input("Enter move (1): "))

def getPlayer2Input() -> int:
    return int(input("Enter move (2): "))

def winnerMessage(winner):
    print(f"{winner} won!")

if __name__ == "__main__":
    gameBoard.display()

    while True:
        player1move = getPlayer1Input()
        if gameBoard.placeTile(1, player1move) == [-1, -1]:
            sys.exit(1)
        if gameBoard.isWinner(1):
            winnerMessage("red")
            break
        gameBoard.display()

        player2move = getPlayer2Input()
        if gameBoard.placeTile(2, player2move) == [-1, -1]:
            sys.exit(1)
        if gameBoard.isWinner(2):
            winnerMessage("yellow")
            break
        gameBoard.display()
    
    gameBoard.display()
