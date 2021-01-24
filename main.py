import sys
from classes import Jeffery, MyEnemy, Attack, Wall
import pygame

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWSIZE = [WINDOWWIDTH, WINDOWHEIGHT]

FPS = 30

# Classes Go Here
player = Jeffery(2, 1, 1, 'Jeffery')
player_group = pygame.sprite.Group()
player_group.add(player)

wall1 = Wall(30, 300, (0, 0, 255))
wall1.rect.x = 600
wall1.rect.y = 120

wall_group = pygame.sprite.Group()
wall_group.add(wall1)

attack_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
# Main Loop Code Go Here

def main():
    global WINDOWSIZE, DISPLAYSURF, FPSCLOCK, FONT
    pygame.init()
    FONT = pygame.font.SysFont('Georgia', 25, True, False)
    DISPLAYSURF = pygame.display.set_mode(WINDOWSIZE)
    FPSCLOCK = pygame.time.Clock()

    # Initializations go here

    while True:
        character_direction = None
        if len(enemy_group) < 3:
            new_enemy = MyEnemy()
            enemy_group.add(new_enemy)
        for event in pygame.event.get():
            # Controls go here
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_direction = 'left'
                if event.key == pygame.K_RIGHT:
                    character_direction = 'right'
                if event.key == pygame.K_UP:
                    character_direction = 'up'
                if event.key == pygame.K_DOWN:
                    character_direction = 'down'
                if event.key == pygame.K_SPACE:
                    player.attack(attack_group)
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.QUIT:
                custom_quit()
        DISPLAYSURF.fill((0, 0, 0))

        # Update positions
        player_group.update(None, wall_group, character_direction)
        wall_group.update()
        attack_group.update()
        enemy_group.update(wall_group, attack_group, player)
        # Drawing new objects go here
        player_group.draw(DISPLAYSURF)
        wall_group.draw(DISPLAYSURF)
        attack_group.draw(DISPLAYSURF)
        enemy_group.draw(DISPLAYSURF)
        FPSCLOCK.tick(FPS)
        pygame.display.flip()


# Additional Modules go here
def custom_quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
