import pygame
from sys import exit


class Button:
    def __init__(self, screen, text, x, y, w, h, img1, img2):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img1 = img1
        self.img2 = img2
        self.pressed = False

    def draw(self):
        if not self.pressed:
            self.screen.blit(self.img1, (self.x, self.y))
        else:
            self.screen.blit(self.img2, (self.x, self.y))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.w and self.y <= y1 <= self.y + self.h:
            return True
        return False

    def mouseIsOver(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.w and self.y <= y1 <= self.y + self.h:
            return False
        return True

    def change(self, mode):
        self.pressed = mode


class MainMenu:
    def __init__(self, screen, screen_settings):
        self.screen = screen
        self.screen_settings = screen_settings
        self.bg_font = pygame.font.SysFont("ubuntu", 160, True, True)
        self.button_font = pygame.font.SysFont("ubuntu", 160, False, False)
        self.bg_image = self._getBgImg()
        self.buttons = self._getButtons()

    def _getBgImg(self):
        w, h = round(self.screen_settings.screen_width * (2 / 3)), round(self.screen_settings.screen_height * 0.25)
        text_surface = self.bg_font.render("Tic Tac Toe", True, (255, 255, 255))
        return pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))

    def _getButtons(self):
        buttons = []
        w, h = round(self.screen_settings.screen_width * (1 / 3)), round(self.screen_settings.screen_height * (1/12))
        x, y = round(self.screen_settings.screen_width * (1 / 3)), round(self.screen_settings.screen_height * (1/2))
        text_surface = self.button_font.render("singleplayer", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("singleplayer", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "singleplayer", x, y, w, h, img1, img2))

        y += h
        text_surface = self.button_font.render("multiplayer", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("multiplayer", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "multiplayer", x, y, w, h, img1, img2))

        y += h
        x2 = x + round((w - round(w * 0.73)) / 2)
        text_surface = self.button_font.render("settings", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (round(w * 0.73), h))
        text_surface = self.button_font.render("settings", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (round(w * 0.73), h))
        buttons.append(Button(self.screen, "settings", x2, y, round(w * 0.73), h, img1, img2))

        y += h
        x2 = x + round((w - round(w * 0.36)) / 2)
        text_surface = self.button_font.render("quit", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (round(w * 0.36), h))
        text_surface = self.button_font.render("quit", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (round(w * 0.36), h))
        buttons.append(Button(self.screen, "quit", x2, y, round(w * 0.36), h, img1, img2))

        return buttons

    def draw(self):
        self.screen.fill((0, 0, 0))
        x, y = round(self.screen_settings.screen_width * (1 / 6)), round(self.screen_settings.screen_height * (1 / 6))
        self.screen.blit(self.bg_image, (x, y))
        for button in self.buttons:
            button.draw()
        pygame.display.update()

    def checkEvents(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.buttons:
                        if button.click(mouse_pos):
                            return button.text
        for button in self.buttons:
            if button.mouseIsOver(mouse_pos):
                button.change(False)
            else:
                button.change(True)

        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            for button in self.buttons:
                if button.click(mouse_pos):
                    return button.text

        return ""
