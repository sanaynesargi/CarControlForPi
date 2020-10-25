import pygame, time, os
from arrow import Arrow

pygame.init()

# PYGAME VARIABLES
S_WIDTH, S_HEIGHT = 300, 300
DIMENSIONS = (S_WIDTH, S_HEIGHT)
win = pygame.display.set_mode(DIMENSIONS)

# COLORS
WHITE = (255, 255, 255)
RED = (255, 10, 10)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

def load_images():
    names = ['up', 'down', 'right', 'left']
    imgs = []

    for name in names:
        imgs.append(pygame.image.load(os.path.join('images', 'arrows', name + '.png')).convert())

    return imgs

def create_arrows(img_arr):
    names = ['up', 'down', 'left', 'right']
    arrs = []
    x, y = (S_WIDTH//2 - 25) - 60, (S_HEIGHT//2 - 25)

    for i in range(2):
        arrs.append(Arrow(x, y, 50, 50, win, img_arr[-(i + 1)], names[-(i + 1)], True))
        x += 120
        

    x = (S_WIDTH//2 - 25)
    y -= 60

    for i in range(2):
        arrs.append(Arrow(x, y, 50, 50, win, img_arr[i], names[i], True))
        y += 120
    
    x, y = (S_WIDTH//2 - 15), (S_HEIGHT//2 - 15)
    stop_img = pygame.image.load(os.path.join('images', 'stop.png')).convert()
    arrs.append(Arrow(x, y, 30, 30, win, stop_img, 'stop', False))

    return arrs

def initialize():
    images = load_images()
    arrows = create_arrows(images)

    return arrows

ARROWS = initialize()
def draw():
    win.fill((BLACK))

    for a in ARROWS:
        a.draw()

    pygame.display.update()


def toggle_arrow_presses(mode):
    for a in ARROWS[:4]:
        a.pressable = mode

def main():
    pygame.display.set_caption("Car Control Wizard")

    run = True
    while run:
        draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            for a in ARROWS:
                if a != ARROWS[-1]:
                    a.pressed = False
                    #toggle_arrow_presses(False)
                    
                if pygame.mouse.get_pressed()[0]:
                    if a == ARROWS[-1] and a.pressed:
                        a.pressed = False
                        #toggle_arrow_presses(True)
                    else:
                        a.pressed = a.check_press(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    pygame.quit()


if __name__ == "__main__":
    main()