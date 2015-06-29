import pygame
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nick's Frisbee Golf Challenge")

done = False
clock = pygame.time.Clock()


def ball(x, y):
    pygame.draw.circle(screen, black, [x, y], 15)

def game_over():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game over", True, red)
    screen.blit(text, (150, 250))

def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, int(yloc + ysize + space), xsize, 500])

def Score(score_count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score_count), True, green)
    screen.blit(text, (0, 0))

x = 50
y = 20
y_speed = 15
ground = 575
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0, 350)
space = 200
obspeed = 2.5
score_count = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 10

    screen.fill(white)
    obstacle(xloc, yloc, xsize, ysize)
    ball(x, y)
    Score(score_count)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        game_over()
        y_speed = 0
        obspeed = 0

    if x + 20 > xloc and y - 20 < ysize and x - 15 < xsize + xloc:
        game_over()
        obspeed = 0
        y_speed = 0

    if xloc < -80:
        xloc = 700
        ysize = randint(0, 350)
        score_count += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

