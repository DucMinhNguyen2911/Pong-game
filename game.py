import pygame

#initialize
pygame.init()

pygame.display.set_caption("Pong game")

#set up game window
x = 900
y = 600
SIZE = (x,y)
#set up background color
#www.google.com/search?q=color+picker
BG_COLOR = (80, 88, 102)

canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")
ball_image = pygame.image.load("assets/ball.png")

x1 = 0
y1 = (y - 120) / 2
x2 = x - 30
y2 = y1
pup_pressed = False
pdown_pressed = False
w_pressed = False
s_pressed = False

ball_x, ball_y = x/2, y/2
speed_x, speed_y= 225, 225
loop = True

ball_speed = 1000
while loop:
    #pooling
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_pressed = True
            elif e.key == pygame.K_s:
                s_pressed = True
            elif e.key == pygame.K_UP:
                pup_pressed = True
            elif e.key == pygame.K_DOWN:
                pdown_pressed = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False
            elif e.key == pygame.K_UP:
                pup_pressed = False
            elif e.key == pygame.K_DOWN:
                pdown_pressed = False
    if w_pressed:
        if y1 != 0:
            y1 -=5
    if s_pressed:
        if y1 != y-120:
            y1 +=5
    if pup_pressed:
        if y2 != 0:
            y2 -=5
    if pdown_pressed:
        if y2 != y-120:
            y2 +=5
    canvas.fill(BG_COLOR)

    canvas.blit(paddle_image, (x1,y1))
    canvas.blit(paddle_image, (x2,y2))
    canvas.blit(ball_image, (ball_x, ball_y))
    clock.tick(60)

    passed = clock.tick(60)
    sec = passed / ball_speed

    ball_x += speed_x * sec
    ball_y += speed_y * sec

    #statements when ball hits barriers and horizontal edges
    if ball_y > y-20:
        ball_y += -(speed_y * sec)
        speed_y = -speed_y
        ball_speed -=10
    if ball_x < 30 and ball_y > y1-19 and ball_y < y1 + 120 + 19:
        ball_x += -(speed_x * sec)
        speed_x = -speed_x
        ball_speed -= 10
    if ball_y < 0:
        ball_y += -(speed_y * sec)
        speed_y = -speed_y
        ball_speed -= 10
    if ball_x > x2-20 and ball_y > y2-19 and ball_y < y2 + 120 + 19:
        ball_x += -(speed_x * sec)
        speed_x = -speed_x
        ball_speed -= 10

    # statements when ball vertical edges
    if ball_x < 0:
        print("Player 2 win")
        break
    if ball_x > x-20:
        print("Player 1 win")
        break

    pygame.display.flip()

