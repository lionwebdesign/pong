import pygame, sys

#Configuración general
pygame.init()
clock = pygame.time.Clock()

#Configuración de la pantalla
screen_width = 1024
screen_height = 576
sceen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

while True:
    #Imput control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    #Actualización de pantalla
    pygame.display.flip()
    clock.tick(60)