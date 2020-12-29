import pygame as pyg
import random

class Monster(pyg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pyg.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1400 - random.randint(0, 100)
        self.rect.y = 750
        self.game = game
        self.velocity = random.randint(1,3)
        print("ma vitesse" + str(self.velocity))

    def damage(self, amount):
        self.health -= amount

        # verification si le monstre meurt
        if self.health <= 0:

            self.remove()

    def update_health_bar(self, surface):
        #dessiner la barre de vie
        pyg.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.max_health, 5])
        pyg.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 10, self.health, 5])

    def forward(self):
        # si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            print("ma velo est " + str(self.velocity) + " et je suis en " + str(self.rect.x))
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

    def remove(self):
        self.game.all_monsters.remove(self)
