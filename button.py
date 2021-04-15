class Button:
    def __init__(self, screen, text, x, y, w, h):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h

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


class SimpleButton(Button):
    def __init__(self, screen, text, x, y, w, h, img1, img2):
        super(SimpleButton, self).__init__(screen, text, x, y, w, h)
        self.img1 = img1
        self.img2 = img2
        self.pressed = False

    def draw(self):
        if not self.pressed:
            self.screen.blit(self.img1, (self.x, self.y))
        elif self.pressed:
            self.screen.blit(self.img2, (self.x, self.y))

    def change(self, mode):
        self.pressed = mode
