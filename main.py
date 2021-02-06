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

ball_speed_x = 7
ball_speed_y = 7

def ball_animation():
    global ball_speed_x, ball_speed_y
    #Movimiento de la bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

while True:
    #Imput control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    ball_animation()

    #visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    #Actualización de pantalla
    pygame.display.flip()
    clock.tick(60)