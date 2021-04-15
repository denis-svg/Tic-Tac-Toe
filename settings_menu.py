import pygame
from sys import exit
from button import SimpleButton as Button
from main_menu import MainMenu


class SettingsMenu(MainMenu):
    def __init__(self, screen, screen_settings):
        super(SettingsMenu, self).__init__(screen, screen_settings)
        self.buttons = self._getButtons()
        self.bg_image = self._getBgImg()
        self.previous_buttons_state = [False, False, False, False, False]

    def _getBgImg(self):
        w, h = round(self.screen_settings.screen_width * (2 / 3)), round(self.screen_settings.screen_height * 0.25)
        text_surface = self.bg_font.render("Resolution", True, (255, 255, 255))
        return pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))

    def _getButtons(self):
        buttons = []
        w, h = round(self.screen_settings.screen_width * (1 / 3)), round(self.screen_settings.screen_height * (1/12))
        x, y = round(self.screen_settings.screen_width * (1 / 3)), round(self.screen_settings.screen_height * (1/2.25))
        text_surface = self.button_font.render("300x300", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("300x300", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "300x300", x, y, w, h, img1, img2))

        y += h
        text_surface = self.button_font.render("450x450", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("450x450", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "450x450", x, y, w, h, img1, img2))

        y += h
        text_surface = self.button_font.render("600x600", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("600x600", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "600x600", x, y, w, h, img1, img2))

        y += h
        text_surface = self.button_font.render("750x750", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("750x750", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "750x750", x, y, w, h, img1, img2))

        y += h
        text_surface = self.button_font.render("900x900", True, (180, 180, 180))
        img1 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        text_surface = self.button_font.render("900x900", True, (255, 255, 255))
        img2 = pygame.transform.smoothscale(text_surface.convert_alpha(), (w, h))
        buttons.append(Button(self.screen, "900x900", x, y, w, h, img1, img2))

        return buttons

    def draw(self):
        self.screen.fill((0, 0, 0))
        x, y = round(self.screen_settings.screen_width * (1 / 6)), round(self.screen_settings.screen_height * (1 / 6))
        self.screen.blit(self.bg_image, (x, y))
        for button in self.buttons:
            button.draw()
        pygame.display.update()
