import pygame


class MyCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.max_health = None
        self.attack_damage = None
        self.move_speed = None
        self.name = None
        self.current_health = None

    def collide_hostile_check(self, hostile_group):
        return (False, [])

    def collide_wall_check(self, wall_group, direction):
        return (False, None)

    def damage_or_healing(self, amount):
        return False

    def update(self, hostile_group, wall_group, direction):
        pass


class MyEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = None
        self.move_speed = None

    def collide_wall_check(self, wall_group, direction):
        return (False, None)

    def collide_hostile_check(self, hostile_group):
        return (False, [])

    def update(self, wall_group, hostile_group, direction):
        pass

class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.damage = None
        self.mode = None
        self.count = None
        self.move_speed = None
        self.direction = None
    def update(self):
        pass
