import pygame as pyg

class Projectile(pyg.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.image = pyg.image.load("assets/projectile.png")
        self.image = pyg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 140
        self.rect.y = player.rect.y + 80
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def moove(self):
        self.rect.x += self.velocity
        self.rotate()
        # vérifier que le projectile ne touche pas
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            monster.damage(self.player.attack)
            self.remove()
        #vérifier que le projectile n'est pas sorti
        if self.rect.x > 1500:
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        # tourner le projectile
        self.angle += 1
        self.image = pyg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

