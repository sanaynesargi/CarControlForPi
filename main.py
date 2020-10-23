# import RPi.GPIO as GPIO
import pygame, time
from arrow import Arrow

pygame.init()

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

# GLOBAL VARIBLES
FIRST_CONTROL_PINS = [5, 6, 19, 26]
SECOND_CONTOL_PINS = [21, 20, 16, 12]

# PYGAME VARIABLES
S_WIDTH, S_HEIGHT = 600, 600
DIMENSIONS = (S_WIDTH, S_HEIGHT)
win = pygame.display.set_mode(DIMENSIONS)

# COLORS
WHITE = (255, 255, 255)
RED = (255, 10, 10)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

def load_images():
    names = ['up', 'down', 'left', 'right']
    imgs = []

    for name in names:
        imgs.append(pygame.image.load(name + '.png').convert())

    return imgs

def initialize():
    images = load_images()

def draw():
    win.fill((BLACK))
    pygame.display.update()

def main():

    pygame.display.set_caption("Car Control Wizard")

    run = True
    while run:
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()