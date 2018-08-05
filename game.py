import pygame

#initialize
pygame.init()

pygame.display.set_caption("Pong game")

#set up game window
SIZE = (600,600)
BG_COLOR = (80, 88, 102)

canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")
ball_image = pygame.image.load("assets/ball.png")
x1 = 0
y1 = 240
x2 = 570
y2 = 240
pup_pressed = False
pdown_pressed = False
w_pressed = False
s_pressed = False

ball_x, ball_y = 300, 300
speed_x, speed_y= 225, 225
loop = True
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
        y1 -=5
    elif s_pressed:
        y1 +=5
    elif pup_pressed:
        y2 -=5
    elif pdown_pressed:
        y2 +=5
    canvas.fill(BG_COLOR)

    canvas.blit(paddle_image, (x1,y1))
    canvas.blit(paddle_image, (x2,y2))
    canvas.blit(ball_image, (ball_x, ball_y))
    clock.tick(60)

    passed = clock.tick(60)
    sec = passed / 1000

    ball_x += speed_x * sec
    ball_y += speed_y * sec

    if ball_x > 580:
        ball_x += -(speed_x * sec)
        speed_x = -speed_x
    elif ball_y > 580:
        ball_y += -(speed_y * sec)
        speed_y = -speed_y
    elif ball_x < 0:
        ball_x += -(speed_x * sec)
        speed_x = -speed_x
    elif ball_y < 0:
        ball_y += -(speed_y * sec)
        speed_y = -speed_y
    elif ball_x > x2-20:
        ball_x += -(speed_x * sec)
        speed_x = -speed_x


    pygame.display.flip()

