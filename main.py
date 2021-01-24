import sys

import pygame

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWSIZE = [WINDOWWIDTH, WINDOWHEIGHT]

FPS = 30

# Classes Go Here
from classes import MyCharacter, MyEnemy, Attack


# Main Loop Code Go Here

def main():
    global WINDOWSIZE, DISPLAYSURF, FPSCLOCK, FONT
    pygame.init()
    FONT = pygame.font.SysFont('Georgia', 25, True, False)
    DISPLAYSURF = pygame.display.set_mode(WINDOWSIZE)
    FPSCLOCK = pygame.time.Clock()

    # Initializations go here

    while True:
        for event in pygame.event.get():
            # Controls go here
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.QUIT:
                custom_quit()
        DISPLAYSURF.fill(DISPLAYSURF.fill(pygame.color.Color('red')))

        # Update positions
        # Drawing new objects go here

        FPSCLOCK.tick(FPS)
        pygame.display.flip()


# Additional Modules go here
def custom_quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
