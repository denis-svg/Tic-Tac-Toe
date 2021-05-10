import pygame
from network import Network
from sys import exit
import threading
from settings import ScreenSettings
from player import Player
from main_menu import MainMenu
from settings_menu import SettingsMenu
from game import SinglePlayerGame


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
        animation_in_process = False
        threads = []
        while True:
            clock.tick()
            game.checkEvents()
            # print(clock.get_fps())
            if not game.playing:
                break
            if game.move_has_made and not game.finished:
                game.updateScreen()
                game.checkWin()
            if game.winner != "No winner" and not animation_in_process:
                thread = threading.Thread(target=Player.afterMatchAnimation,
                                          args=(self.screen, self.screen_settings, game, game.winner, game.cells))
                threads.append(thread)
                thread.start()
                print(game.stats)
                animation_in_process = True
            if animation_in_process:
                if not threads[0].is_alive():
                    animation_in_process = False
                    game.resetGame()
                    game.updateScreen()
                    game.winner = "No winner"
                    game.finished = False
                    threads.pop()
            if animation_in_process and game.need_screen_update:
                pygame.display.update()
                game.need_screen_update = False

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