import pygame as pyg
from Projectile import Projectile

class Player(pyg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.game = game
        self.max_health = 100
        self.attack = 40
        self.velocity = 2
        self.all_projectiles = pyg.sprite.Group()
        self.image = pyg.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 700

    def launch_projectile(self):
        # creer un projectile
        self.all_projectiles.add(Projectile(self))

    def moove_right(self):
        # si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def moove_left(self):
        self.rect.x -= self.velocity

    def damage(self, amount):
        self.health -= amount

        # verification si le monstre meurt
        if self.health <= 0:

            self.game.game_over()

    def update_health_bar(self, surface):
        #dessiner la barre de vie
        pyg.draw.rect(surface, (60, 63, 60), [self.rect.x + 47, self.rect.y + 25, self.max_health, 5])
        pyg.draw.rect(surface, (111, 210, 46), [self.rect.x + 47, self.rect.y + 25, self.health, 5])

