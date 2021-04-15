import pygame
from network import Network
from sys import exit
from settings import ScreenSettings
from player import Player
from main_menu import MainMenu
from settings_menu import SettingsMenu


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

    def runSinglePlayer(self, board):
        p1 = Player(self.screen, self.screen_settings, board, "X")
        p2 = Player(self.screen, self.screen_settings, board, "O")
        p1.updateScreen()
        clock = pygame.time.Clock()
        while True:
            clock.tick()
            if not p2.clicked:
                p1.checkEvents()
                if not p1.playing:
                    break
            if not p1.turn:
                p2.turn = True
            if not p1.clicked:
                p2.checkEvents()
                if not p2.playing:
                    break
            if not p2.turn:
                p1.turn = True

    def runSettings(self):
        s = SettingsMenu(self.screen, self.screen_settings)
        clock = pygame.time.Clock()
        while True:
            clock.tick()
            action = s.checkEvents()
            if action == "300x300":
                self.screen = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
                self.screen_settings.changeResolution(300, 300)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "450x450":
                self.screen = pygame.display.set_mode((450, 450), pygame.RESIZABLE)
                self.screen_settings.changeResolution(450, 450)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "600x600":
                self.screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
                self.screen_settings.changeResolution(600, 600)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "750x750":
                self.screen = pygame.display.set_mode((750, 750), pygame.RESIZABLE)
                self.screen_settings.changeResolution(750, 750)
                s.need_draw_changes = True
                s.need_screen_changes = True
                continue
            elif action == "900x900":
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
                self.runSinglePlayer([['', '', ''], ['', '', ''], ['', '', '']])
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