import pygame
from network import Network
from sys import exit
from settings import ScreenSettings
from player import Player
from main_menu import MainMenu


class TTTi:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.new_game = False
        self.screen_settings = ScreenSettings()
        self.screen = pygame.display.set_mode((self.screen_settings.screen_width, self.screen_settings.screen_height))
        pygame.display.set_caption("Tic Tac Toe")

    def runMultiPlayer(self):
        pass

    def runSinglePlayer(self, board):
        p1 = Player(self.screen, self.screen_settings, board, "X")
        p2 = Player(self.screen, self.screen_settings, board, "O")
        self._makeBoard()
        while True:
            if self.new_game:
                p1.checkEvents()
                if not p1.turn:
                    p2.turn = True
                p2.checkEvents()
                if not p2.turn:
                    p1.turn = True
            else:
                self._resetClick()

    def _makeBoard(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.line(self.screen, (255, 255, 255), (self.screen_settings.square_width, 0),
                         (self.screen_settings.square_width, self.screen_settings.square_height * 3))
        pygame.draw.line(self.screen, (255, 255, 255), (self.screen_settings.square_width * 2, 0),
                         (self.screen_settings.square_width * 2, self.screen_settings.square_height * 3))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.screen_settings.square_height),
                         (self.screen_settings.square_width * 3, self.screen_settings.square_height))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.screen_settings.square_height * 2),
                         (self.screen_settings.square_width * 3, self.screen_settings.square_height * 2))
        pygame.display.update()

    def _resetClick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.new_game = True

    def mainMenu(self):
        m = MainMenu(self.screen, self.screen_settings)
        action = ""
        while True:
            action = m.checkEvents()
            if action == "singleplayer":
                self.runSinglePlayer([['', '', ''], ['', '', ''], ['', '', '']])
            elif action == "multiplayer":
                self.runMultiPlayer()
            elif action == "settings":
                pass
            elif action == "quit":
                pygame.quit()
                exit()
            m.draw()


if __name__ == "__main__":
    t = TTTi()
    t.mainMenu()