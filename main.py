import pygame as pyg
import Game
import Monster
import Projectile

pyg.init()
game = Game.Game()
background = pyg.image.load("assets/bg.jpg")
banner = pyg.image.load("assets/banner.png")

# generer la fenetre du jeu
pyg.display.set_caption("mon jeu")

# Gestion de la fenetre
screen = pyg.display.set_mode((1500, 920))


running = True

# Continue tant que le jeu est running
while running:
    # action sur la surface
    screen.blit(background, (0, 0))
    # Si la partie a commencé
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner, (0, 0))
        # mise a jour de la surface
    pyg.display.flip()
    for event in pyg.event.get():
        #  Fermeture de la fenetre
        if event.type == pyg.QUIT:
            running = False
            pyg.quit()
        # detecter si le joueur lache une touche
        elif event.type == pyg.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est appuyée
            if event.key == pyg.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pyg.KEYUP:
            game.pressed[event.key] = False

