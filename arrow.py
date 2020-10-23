import pygame

class Arrow:

    def __init__(self, x, y, surface, img):

        self.x = x
        self.y = y
        self.img = img
        self.surf = surface

    def draw(self):
        pygame.draw.rect(self.surf, (0, 255, 0), (self.x, self.y, 50, 50))

    def get_dims(self):
        return (50, 50)
