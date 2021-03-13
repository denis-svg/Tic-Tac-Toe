import pygame
from pygame import gfxdraw
from math import sqrt
from sys import exit


class Player:
    def __init__(self, screen, screen_settings, board, character):
        self.screen = screen
        self.screen_settings = screen_settings
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
                x = mouse_pos[0] // self.screen_settings.square_width
                y = mouse_pos[1] // self.screen_settings.square_height
                if x in [0, 1, 2] and y in [0, 1, 2]:
                    if not self.board[y][x]:
                        self.board[y][x] = self.character
                        self.turn = False
                        self._drawCharacter((x, y), self.character)

    def _drawCharacter(self, pos, character):
        if character == "X":
            self._drawX(pos)
        else:
            self._drawO(pos)
        pygame.display.update()

    def _drawO(self, pos):
        w = self.screen_settings.square_width
        h = self.screen_settings.square_height
        rx = self.screen_settings.square_width // 2 - int(0.15 * w)
        ry = self.screen_settings.square_height // 2 - int(0.15 * h)
        rx1 = rx - round(sqrt(2 * (int(0.22 * w) - int(0.15 * w)) ** 2))
        ry1 = ry - round(sqrt(2 * (int(0.22 * h) - int(0.15 * h)) ** 2))
        gfxdraw.aaellipse(self.screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx, ry, (255, 255, 255))
        gfxdraw.filled_ellipse(self.screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx, ry,
                               (255, 255, 255))
        gfxdraw.aaellipse(self.screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx1, ry1, (0, 0, 0))
        gfxdraw.filled_ellipse(self.screen, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx1, ry1, (0, 0, 0))

    def _drawX(self, pos):
        w = self.screen_settings.square_width
        h = self.screen_settings.square_height
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