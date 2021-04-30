import pygame
from pygame import gfxdraw
from math import sqrt
from sys import exit


class Player:
    def __init__(self, character):
        self.character = character
        self.clicked = False
        self.playing = True

    def checkEvents(self, screen, screen_settings, board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicked = False
            elif event.type == pygame.VIDEORESIZE:
                screen_settings.changeResolution(event.w, event.h)
                Player.updateScreen(screen, screen_settings, board)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.playing = False

        if not self.clicked and self.playing:
            return self._checkMOUSEBUTTONDOWN(screen_settings, board)

        return None, None

    def _checkMOUSEBUTTONDOWN(self, screen_settings, board):
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // screen_settings.square_width
            y = mouse_pos[1] // screen_settings.square_height
            if x in [0, 1, 2] and y in [0, 1, 2]:
                if not board[y][x]:
                    self.clicked = True
                    return y, x
        return None, None

    @staticmethod
    def _drawO(screen, screen_settings, pos, color=(255, 255, 255), bg_color=(0, 0, 0)):
        w = screen_settings.square_width
        h = screen_settings.square_height
        rx = screen_settings.square_width // 2 - int(0.15 * w)
        ry = screen_settings.square_height // 2 - int(0.15 * h)
        rx1 = rx - round(sqrt(2 * (int(0.22 * w) - int(0.15 * w)) ** 2))
        ry1 = ry - round(sqrt(2 * (int(0.22 * h) - int(0.15 * h)) ** 2))
        gfxdraw.aaellipse(screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx, ry, color)
        gfxdraw.filled_ellipse(screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx, ry,
                               color)
        gfxdraw.aaellipse(screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx1, ry1, bg_color)
        gfxdraw.filled_ellipse(screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx1, ry1, bg_color)

    @staticmethod
    def _drawX(screen, screen_settings, pos, color=(255, 255, 255)):
        w = screen_settings.square_width
        h = screen_settings.square_height
        points = [(pos[0] * w + int(0.15 * w), pos[1] * h + int(0.22 * h)),
                  (pos[0] * w + int(0.22 * w), pos[1] * h + int(0.15 * h)),
                  (pos[0] * w + int(0.85 * w), pos[1] * h + int(0.78 * h)),
                  (pos[0] * w + int(0.78 * w), pos[1] * h + int(0.85 * h))]
        pygame.draw.polygon(screen, color, points)
        points = [(pos[0] * w + int(0.15 * w), pos[1] * h + int(0.78 * h)),
                  (pos[0] * w + int(0.22 * w), pos[1] * h + int(0.85 * h)),
                  (pos[0] * w + int(0.85 * w), pos[1] * h + int(0.22 * h)),
                  (pos[0] * w + int(0.78 * w), pos[1] * h + int(0.15 * h))]
        pygame.draw.polygon(screen, color, points, 0)

    @staticmethod
    def makeBoard(screen, screen_settings, color=(255, 255, 255), bg_color=(0, 0, 0), draw_bg=True):
        if draw_bg:
            screen.fill(bg_color)
        pygame.draw.line(screen, color, (screen_settings.square_width, 0),
                         (screen_settings.square_width, screen_settings.square_height * 3))
        pygame.draw.line(screen, color, (screen_settings.square_width * 2, 0),
                         (screen_settings.square_width * 2, screen_settings.square_height * 3))
        pygame.draw.line(screen, color, (0, screen_settings.square_height),
                         (screen_settings.square_width * 3, screen_settings.square_height))
        pygame.draw.line(screen, color, (0, screen_settings.square_height * 2),
                         (screen_settings.square_width * 3, screen_settings.square_height * 2))

    @staticmethod
    def drawMoves(screen, screen_settings, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    Player._drawX(screen, screen_settings, (j, i))
                elif board[i][j] == "O":
                    Player._drawO(screen, screen_settings, (j, i))

    @staticmethod
    def updateScreen(screen, screen_settings, board):
        Player.makeBoard(screen, screen_settings)
        Player.drawMoves(screen, screen_settings, board)
        pygame.display.update()

    @staticmethod
    def afterMatchAnimation(screen, screen_settings, winner, cells, disappear):
        if not disappear:
            if winner == "X":
                for cell in cells:
                    Player._drawX(screen, screen_settings, (cell[1], cell[0]))
            elif winner == "O":
                for cell in cells:
                    Player._drawO(screen, screen_settings, (cell[1], cell[0]))
            elif winner == "Tie":
                Player.makeBoard(screen, screen_settings, draw_bg=False)
        else:
            if winner == "X":
                for cell in cells:
                    Player._drawX(screen, screen_settings, (cell[1], cell[0]), color=(0, 0, 0))
            elif winner == "O":
                for cell in cells:
                    Player._drawO(screen, screen_settings, (cell[1], cell[0]), color=(0, 0, 0))
            elif winner == "Tie":
                Player.makeBoard(screen, screen_settings, color=(0, 0, 0), draw_bg=False)
        pygame.display.update()
