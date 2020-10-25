import pygame
import requests

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
        self.pressable = True

    def draw(self):
        url = 'http://192.168.86.30:5000/'
        if self.pressed:
            if self.name != 'stop':
                if self.name == 'up':
                    requests.post(url, headers={'direction': 'forward'})                
                if self.name == 'down':
                    requests.post(url, headers={'direction': 'backward'})
                if self.name == 'left':
                    requests.post(url, headers={'direction': 'left'})
                if self.name == 'right':
                    requests.post(url, headers={'direction': 'right'})

                pygame.draw.rect(self.surf, (0, 0, 255), (self.x, self.y, self.width, self.height))
            elif self.pressable and self.name == 'stop':
                requests.post(url, headers={'direction': 'stop'})
                pygame.draw.rect(self.surf, (0, 20, 128), (self.x, self.y, self.width, self.height))
        else:
            if self.ovverride:
                pygame.draw.rect(self.surf, (0, 255, 0), (self.x, self.y, self.width, self.height))
            else:    
                pygame.draw.rect(self.surf, (255, 20, 128), (self.x, self.y, self.width, self.height))

        self.surf.blit(self.img, (self.x + 5.35, self.y + 5.35))

    def get_dims(self):
        return (50, 50)

    def check_press(self, mx, my):

        return ((mx > self.x) and (mx < (self.x + 50))) and ((my > self.y) and (my < (self.y + 50)))

