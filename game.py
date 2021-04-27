class SinglePlayerGame:
    def __init__(self, screen, screen_settings, p1, p2):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.screen = screen
        self.screen_settings = screen_settings
        self.playerX_turn = True
        self.playerO_turn = False
        self.playerX_wins = 0
        self.playerO_wins = 0
        self.ties = 0
        self.p1 = p1
        self.p2 = p2
        self.move_has_made = False
        self.playing = True

    def updateScreen(self):
        self.p1.updateScreen(self.screen, self.screen_settings, self.board)

    def checkEvents(self):
        self.move_has_made = False
        if not self.p2.clicked:
            self.p1.checkEvents(self.screen, self.screen_settings, self.board, self.move)
            if not self.p1.playing:
                self.status = False
                return
        if not self.p1.clicked:
            self.p2.checkEvents(self.screen, self.screen_settings, self.board, self.move)
            if not self.p2.playing:
                self.status = False
                return

    def move(self, row, col):
        if row in [0, 1, 2] and col in [0, 1, 2]:
            if not self.board[row][col]:
                if self.playerX_turn:
                    self.board[row][col] = "X"
                else:
                    self.board[row][col] = "O"
                self.playerX_turn, self.playerO_turn = self.playerO_turn, self.playerX_turn
                self.updateScreen()
                self.move_has_made = True


    def resetGame(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.playerX_turn = True
        self.playerO_turn = False
        self.move_has_made = False

    def checkWin(self):
        winner = self.checkRows()
        if winner != "No winner":
            self.handleWin(winner)
            return winner

        winner = self.checkCols()
        if winner != "No winner":
            self.handleWin(winner)
            return winner

        winner = self.checkDiagonals()
        if winner != "No winner":
            self.handleWin(winner)
            return winner

        if self.isFull():
            winner = "Tie"
            self.handleWin(winner)
            return winner

        return winner

    def checkRows(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0]:
                return self.board[i][0]

        return "No winner"

    def checkCols(self):
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j]:
                return self.board[0][j]

        return "No winner"

    def checkDiagonals(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2]:
            return self.board[0][2]

        return "No winner"

    def isFull(self):
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    return False

        return True

    def handleWin(self, winner):
        if winner == "Tie":
            self.ties += 1

        elif winner == "O":
            self.playerO_wins += 1

        elif winner == "X":
            self.playerX_wins += 1
        print(winner)
        self.resetGame()
        self.updateScreen()