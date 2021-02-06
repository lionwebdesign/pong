import pygame, sys

#Configuración general
pygame.init()
clock = pygame.time.Clock()

#Configuración de la pantalla
screen_width = 1024
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

#Distribución espacial de los elementos del juego
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

while True:
    #Imput control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    #visual
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    #Actualización de pantalla
    pygame.display.flip()
    clock.tick(60)