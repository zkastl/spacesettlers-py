class AbstractGame:

    def isGameOver() -> bool: pass
    def getTurn() -> bool: pass
    def playAction(self, action: 'AbstractGameAction') -> None: pass
    def getWinner(self) -> int: pass
    def getBoard(self) -> 'AbstractGameBoard': pass
    def getPlayer1(self) -> 'AbstractGameAgent': pass
    def getPlayer2(self) -> 'AbstractGameAgent': pass
    def getCurrentPlayer(self) -> 'AbstractGameAgent': pass


class AbstractGameAction: pass

class AbstractGameAgent:
    def __init__(self):
        self.player = 1

class AbstractGameBoard: pass