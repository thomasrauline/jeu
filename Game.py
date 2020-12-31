import pygame as pyg
import Player
import Monster

class Game:

    def __init__(self):
        # boolean jeu en cours
        self.is_playing = False
        #génère le jeu
        self.all_players = pyg.sprite.Group()
        self.player = Player.Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pyg.sprite.Group()

    def game_over(self):
        # relance le jeu au début
        # reset monstres
        self.all_monsters = pyg.sprite.Group()
        #reset personnage
        self.player = Player.Player(self)
        # remetre au bouton du début
        self.is_playing = False

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.player.update_health_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.moove()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Gestion du personnage
        if self.pressed.get(pyg.K_LEFT) and self.player.rect.x > 0:
            self.player.moove_left()
        if self.pressed.get(pyg.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1500:
            self.player.moove_right()

    def spawn_monster(self):
        self.all_monsters.add(Monster.Monster(self))

    def check_collision(self, sprite, group):
        return pyg.sprite.spritecollide(sprite, group, False, pyg.sprite.collide_mask)
