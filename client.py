import pygame
from sys import exit
from pygame import gfxdraw


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.square_width = self.screen_width // 3
        self.square_height = self.screen_height // 3
        self.ration = self.screen_width // self.screen_height


class Player:
    def __init__(self, screen, settings, board, character):
        self.screen = screen
        self.settings = settings
        self.board = board
        self.character = character
        self.turn = False
        if character == "X":
            self.turn = True

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self._checkMOUSEBUTTONDOWN()

    def _checkMOUSEBUTTONDOWN(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.turn:
                x = mouse_pos[0] // self.settings.square_width
                y = mouse_pos[1] // self.settings.square_height
                if x in [0, 1, 2] and y in [0, 1, 2]:
                    if not self.board[y][x]:
                        self.board[y][x] = self.character
                        self.turn = False
                        self._drawCharacter((x, y), self.character)

    def _drawCharacter(self, pos, character):
        w = self.settings.square_width
        h = self.settings.square_height
        if character == "X":
            points = [(pos[0] * w + int(0.15 * w), pos[1] * h + int(0.22 * h)),
                      (pos[0] * w + int(0.22 * w), pos[1] * h + int(0.15 * h)),
                      (pos[0] * w + int(0.85 * w), pos[1] * h + int(0.78 * h)),
                      (pos[0] * w + int(0.78 * w), pos[1] * h + int(0.85 * h))]
            pygame.draw.polygon(self.screen, (255, 255, 255), points)
            points = [(pos[0] * w + int(0.15 * w), pos[1] * h + int(0.78 * h)),
                      (pos[0] * w + int(0.22 * w), pos[1] * h + int(0.85 * h)),
                      (pos[0] * w + int(0.85 * w), pos[1] * h + int(0.22 * h)),
                      (pos[0] * w + int(0.78 * w), pos[1] * h + int(0.15 * h))]
            pygame.draw.polygon(self.screen, (255, 255, 255), points, 0)
        else:
            gfxdraw.aacircle(self.screen, pos[0] * w + 50, pos[1] * h + 50, 100, (255, 255, 255))
            gfxdraw.filled_circle(self.screen, pos[0] * w + 50, pos[1] * h + 50, 100, (255, 255, 255))
        pygame.display.update()


class TTTi:
    def __init__(self, board, character):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tic Tac Toe")

        self.character = character
        self.board = board
        self.player = Player(self.screen, self.settings, self.board, character)
        self.p2 = Player(self.screen, self.settings, self.board, "O")

    def runGame(self):
        self._makeBoard()
        while True:
            self.player.checkEvents()
            if not self.player.turn:
                self.p2.turn = True
            self.p2.checkEvents()
            if not self.p2.turn:
                self.player.turn = True

    def _makeBoard(self):
        pygame.draw.line(self.screen, (255, 255, 255), (self.settings.square_width, 0),
                         (self.settings.square_width, self.settings.square_height * 3))
        pygame.draw.line(self.screen, (255, 255, 255), (self.settings.square_width * 2, 0),
                         (self.settings.square_width * 2, self.settings.square_height * 3))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.settings.square_height),
                         (self.settings.square_width * 3, self.settings.square_height))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.settings.square_height * 2),
                         (self.settings.square_width * 3, self.settings.square_height * 2))
        pygame.display.update()


if __name__ == "__main__":
    t = TTTi([['', '', ''], ['', '', ''], ['', '', '']], "X")
    t.runGame()
