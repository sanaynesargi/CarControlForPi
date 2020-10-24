import pygame

class Arrow:

    def __init__(self, x, y, surface, img):

        self.x = x
        self.y = y
        self.img = img
        self.surf = surface
        self.pressed = False

    def draw(self):
        if self.pressed:
            pygame.draw.rect(self.surf, (0, 0, 255), (self.x, self.y, 50, 50))
        else:
            pygame.draw.rect(self.surf, (0, 255, 0), (self.x, self.y, 50, 50))
        self.surf.blit(self.img, (self.x + 5.35, self.y + 5.35))

    def get_dims(self):
        return (50, 50)

    def check_press(self, mx, my):

        return ((mx > self.x) and (mx < (self.x + 50))) and ((my > self.y) and (my < (self.y + 50)))

