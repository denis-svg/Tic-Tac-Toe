class ScreenSettings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.square_width = self.screen_width // 3
        self.square_height = self.screen_height // 3

    def changeResolution(self, new_width, new_height):
        self.screen_width = new_width
        self.screen_height = new_height
        self.square_width = self.screen_width // 3
        self.square_height = self.screen_height // 3