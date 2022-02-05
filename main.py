import pygame, sys, random

def ball_restart():
    global ballSpeed_x, ballSpeed_y

    ball.center = (screen_width/2, screen_height/2)
    ballSpeed_x *= random.choice((1,-1))
    ballSpeed_y *= random.choice((1, -1))

def ball_animation():
    global ballSpeed_x, ballSpeed_y
    ball.x += ballSpeed_x
    ball.y += ballSpeed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ballSpeed_y *= -1
    if ball.left<=0 or ball.right>=screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeed_x *= -1

def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    global opponent_speed
    if opponent.y < ball.y:
        opponent.top += opponent_speed
    if opponent.y > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
#General Setup
pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong')

balldim = 10
ball = pygame.Rect(screen_width/2 - (balldim/2), screen_height/2 - (balldim/2),balldim,balldim)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10,140)


bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ballSpeed_x = 4
ballSpeed_y = 4
player_speed = 0
opponent_speed = 3

while True:
    #handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player.y += player_speed
    player_animation()
    opponent_ai()



    #Visuals
    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)



    #Update Window
    pygame.display.flip()
    clock.tick(60)
