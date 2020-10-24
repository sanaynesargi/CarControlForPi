import pygame

class Arrow:

    def __init__(self, x, y, width, height, surface, img, name, ovverride):

        self.x = x
        self.y = y
        self.img = img
        self.surf = surface
        self.pressed = False
        self.name = name
        self.width = width
        self.height = height
        self.ovverride = ovverride

    def draw(self):
        if self.pressed:
            if self.name != 'stop':
                pygame.draw.rect(self.surf, (0, 0, 255), (self.x, self.y, self.width, self.height))
            else:
                pygame.draw.rect(self.surf, (255, 0, 0), (self.x, self.y, self.width, self.height))
        else:
            if self.ovverride:
                pygame.draw.rect(self.surf, (0, 255, 0), (self.x, self.y, self.width, self.height))
            else:    
                pygame.draw.rect(self.surf, (255, 128, 128), (self.x, self.y, self.width, self.height))

        self.surf.blit(self.img, (self.x + 5.35, self.y + 5.35))

    def get_dims(self):
        return (50, 50)

    def check_press(self, mx, my):

        return ((mx > self.x) and (mx < (self.x + 50))) and ((my > self.y) and (my < (self.y + 50)))

