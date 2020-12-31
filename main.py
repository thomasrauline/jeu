import pygame as pyg
import Game
import Monster
import Projectile

pyg.init()
game = Game.Game()
background = pyg.image.load("assets/bg.jpg")

# Gestion de la fenetre
screen = pyg.display.set_mode((1500, 920))

# Banniere
banner = pyg.image.load("assets/banner.png")
banner = pyg.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = (screen.get_width() - banner.get_width())/2
banner_rect.y = (screen.get_height() - banner.get_height())/2

# gérer le bouton de début de partie
play_button = pyg.image.load("assets/button.png")
play_button = pyg.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = (screen.get_width() - play_button.get_width())/2
play_button_rect.y = (screen.get_height() - play_button.get_height())/1.4
# generer la fenetre du je
pyg.display.set_caption("mon jeu")



running = True

# Continue tant que le jeu est running
while running:
    # action sur la surface
    screen.blit(background, (0, 0))
    # Si la partie a commencé
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(banner, (banner_rect.x, banner_rect.y))
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
        elif event.type == pyg.MOUSEBUTTONDOWN:
            #vérification si la souris est sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()

