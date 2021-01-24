import pygame
import random


class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Jeffery(pygame.sprite.Sprite):
    def __init__(self, max_health, attack_damage, move_speed, name):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill((0, 255, 0))
        # file_image = pygame.image.load(r'E:\Pycharm Projects\halftermprojectThree\player.png')
        # pygame.transform.scale(file_image, (30, 30), self.image)
        self.rect = self.image.get_rect()
        self.max_health = max_health
        self.attack_damage = attack_damage
        self.move_speed = move_speed
        self.name = name
        self.current_health = max_health

    def collide_hostile_check(self, hostile_group):
        return (False, [])

    def collide_wall_check(self, wall_group):
        result = pygame.sprite.spritecollide(self, wall_group, False)
        if result:
            return (True, result)
        else:
            return (False, None)

    def damage_or_healing(self, amount):
        return False

    def attack(self, attack_group):
        new_attack = Attack()
        new_attack.damage = self.attack_damage
        new_attack.mode = 'melee'
        new_attack.count = 0
        new_attack.rect.midleft = self.rect.midright
        new_attack.rect.x -= 1

        attack_group.add(new_attack)

    def update(self, hostile_group, wall_group, direction):
        if direction:
            if direction == 'up':
                self.rect.y -= self.move_speed * 30
            elif direction == 'down':
                self.rect.y += self.move_speed * 30
            elif direction == 'right':
                self.rect.x += self.move_speed * 30
            elif direction == 'left':
                self.rect.x -= self.move_speed * 30
        hit_walls = self.collide_wall_check(wall_group)
        if hit_walls[0]:
            if direction:
                if direction == 'up':
                    self.rect.y += self.move_speed * 30
                elif direction == 'down':
                    self.rect.y -= self.move_speed * 30
                elif direction == 'right':
                    self.rect.x -= self.move_speed * 30
                elif direction == 'left':
                    self.rect.x += self.move_speed * 30


class MyEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.move_speed = 1 / 3
        self.image = pygame.Surface([30, 30])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.choice([570, 30, 330]), random.choice([570, 30, 330]))

    def collide_wall_check(self, wall_group):
        result = pygame.sprite.spritecollide(self, wall_group, False)
        if result:
            return (True, result)
        else:
            return (False, None)

    def collide_hostile_check(self, hostile_group):
        hits = pygame.sprite.spritecollide(self, hostile_group, True)
        if hits:
            self.kill()

    def update(self, wall_group, hostile_group, player):
        direction = ''
        if player.rect.x > self.rect.x:
            direction += 'right'
        if player.rect.x < self.rect.x:
            direction += 'left'
        if player.rect.y < self.rect.y:
            direction += 'up'
        if player.rect.y > self.rect.y:
            direction += 'down'
        if 'up' in direction:
            self.rect.y -= self.move_speed * 30
        elif 'down' in direction:
            self.rect.y += self.move_speed * 30
        elif 'right' in direction:
            self.rect.x += self.move_speed * 30
        elif 'left' in direction:
            self.rect.x -= self.move_speed * 30
        hit_walls = self.collide_wall_check(wall_group)
        if hit_walls[0]:
            if direction:
                if direction == 'up':
                    self.rect.y += self.move_speed * 30
                elif direction == 'down':
                    self.rect.y -= self.move_speed * 30
                elif direction == 'right':
                    self.rect.x -= self.move_speed * 30
                elif direction == 'left':
                    self.rect.x += self.move_speed * 30
        self.collide_hostile_check(hostile_group)

class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([90, 10])
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect()
        self.damage = None
        self.mode = None
        self.count = 0
        self.move_speed = None
        self.direction = None

    def update(self):
        self.count += 1
        if self.count == 3:
            self.kill()
