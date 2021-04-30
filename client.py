import pygame
from network import Network
from sys import exit
from settings import ScreenSettings
from player import Player
from main_menu import MainMenu
from settings_menu import SettingsMenu
from game import SinglePlayerGame
from time import time


class TTTi:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen_settings = ScreenSettings()
        self.screen = pygame.display.set_mode((self.screen_settings.screen_width, self.screen_settings.screen_height),
                                              pygame.RESIZABLE)
        pygame.display.set_caption("Tic Tac Toe")

    def runMultiPlayer(self):
        pass

    def runSinglePlayer(self):
        game = SinglePlayerGame(self.screen, self.screen_settings, Player("X"), Player("O"))
        game.updateScreen()
        clock = pygame.time.Clock()
        i = 1
        animation = False
        winner = "No winner"
        while True:
            clock.tick()
            game.checkEvents()
            if not game.playing:
                break
            if game.move_has_made and not animation:
                game.updateScreen()
                winner = game.checkWin()
            if winner == "X" and not animation:
                game.playerX_wins += 1
                animation = True
            elif winner == "O" and not animation:
                game.playerO_wins += 1
                animation = True
            elif winner == "Tie" and not animation:
                game.ties += 1
                animation = True
            if winner != "No winner":
                if i <= 10:
                    if i % 2 != 0:
                        game.afterMatchAnimation(winner, disappear=True)
                    else:
                        game.afterMatchAnimation(winner, disappear=False)
                else:
                    game.resetGame()
                    game.updateScreen()
                    winner = "No winner"
                    animation = False
                    i = 1
                i += 1

    def runSettings(self):
        s = SettingsMenu(self.screen, self.screen_settings)
        clock = pygame.time.Clock()
        while True:
            clock.tick()
            action = s.checkEvents()
            if action == "300x300" and (self.screen_settings.screen_width != 300 or self.screen_settings.screen_width != 300):
                self.screen = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
                self.screen_settings.changeResolution(300, 300)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "450x450" and (self.screen_settings.screen_width != 450 or self.screen_settings.screen_width != 450):
                self.screen = pygame.display.set_mode((450, 450), pygame.RESIZABLE)
                self.screen_settings.changeResolution(450, 450)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "600x600" and (self.screen_settings.screen_width != 600 or self.screen_settings.screen_width != 600):
                self.screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
                self.screen_settings.changeResolution(600, 600)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "750x750" and (self.screen_settings.screen_width != 750 or self.screen_settings.screen_width != 750):
                self.screen = pygame.display.set_mode((750, 750), pygame.RESIZABLE)
                self.screen_settings.changeResolution(750, 750)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "900x900" and (self.screen_settings.screen_width != 900 or self.screen_settings.screen_width != 900):
                self.screen = pygame.display.set_mode((900, 900), pygame.RESIZABLE)
                self.screen_settings.changeResolution(900, 900)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "break":
                break
            if s.need_draw_changes:
                s.draw()
                s.need_draw_changes = False

    def mainMenu(self):
        m = MainMenu(self.screen, self.screen_settings)
        clock = pygame.time.Clock()
        while True:
            clock.tick()
            action = m.checkEvents()
            if action == "singleplayer":
                self.runSinglePlayer()
                m.need_screen_changes = True
                m.need_draw_changes = True
                continue
            elif action == "multiplayer":
                self.runMultiPlayer()
            elif action == "settings":
                self.runSettings()
                m.need_screen_changes = True
                m.need_draw_changes = True
                continue
            elif action == "quit":
                pygame.quit()
                exit()
            if m.need_draw_changes:
                m.draw()
                m.need_draw_changes = False


if __name__ == "__main__":
    t = TTTi()
    t.mainMenu()