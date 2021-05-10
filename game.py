class Game:
    def __init__(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.playerX_turn = True
        self.playerO_turn = False
        self.stats = {"Tie": 0,
                      "X": 0,
                      "O": 0}
        self.cells = []
        self.move_has_made = False
        self.finished = False
        self.winner = "No winner"

    def move(self, row, col):
        if row in [0, 1, 2] and col in [0, 1, 2]:
            if not self.board[row][col]:
                if self.playerX_turn:
                    self.board[row][col] = "X"
                else:
                    self.board[row][col] = "O"
                self.playerX_turn, self.playerO_turn = self.playerO_turn, self.playerX_turn
                self.move_has_made = True

    def resetGame(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.playerX_turn = True
        self.playerO_turn = False
        self.move_has_made = False
        self.cells = []

    def checkWin(self):
        self.checkRows()
        if self.winner != "No winner":
            self.finished = True
            self.stats[self.winner] += 1
            return

        self.checkCols()
        if self.winner != "No winner":
            self.finished = True
            self.stats[self.winner] += 1
            return

        self.checkDiagonals()
        if self.winner != "No winner":
            self.finished = True
            self.stats[self.winner] += 1
            return

        if self.isFull():
            self.winner = "Tie"
            self.finished = True
            self.stats[self.winner] += 1

    def checkRows(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0]:
                self.cells = [(i, j) for j in range(3)]
                self.winner = self.board[i][0]
                return

    def checkCols(self):
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j]:
                self.cells = [(i, j) for i in range(3)]
                self.winner = self.board[0][j]
                return

    def checkDiagonals(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0]:
            self.cells = [(0, 0), (1, 1), (2, 2)]
            self.winner = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2]:
            self.cells = [(0, 2), (1, 1), (2, 0)]
            self.winner = self.board[0][2]

    def isFull(self):
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    return False
        return True


class SinglePlayerGame(Game):
    def __init__(self, screen, screen_settings, p1, p2):
        super().__init__()
        self.board = [['X', 'O', 'X'],
                      ['X', 'O', 'O'],
                      ['O', '', '']]
        self.screen = screen
        self.screen_settings = screen_settings
        self.need_screen_update = False
        self.p1 = p1
        self.p2 = p2
        self.playing = True

    def updateScreen(self):
        self.p1.updateScreen(self.screen, self.screen_settings, self.board)

    def checkEvents(self):
        self.move_has_made = False
        if not self.p2.clicked:
            row, col = self.p1.checkEvents(self.screen, self.screen_settings, self.board)
            if row is not None and col is not None:
                self.move(row, col)
            if not self.p1.playing:
                self.playing = False
                return
        if not self.p1.clicked:
            row, col = self.p2.checkEvents(self.screen, self.screen_settings, self.board)
            if row is not None and col is not None:
                self.move(row, col)
            if not self.p2.playing:
                self.playing = False
                return


class Multiplayer(Game):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
