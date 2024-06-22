import pymunk
import pygame

pygame.init()
run = True

WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
space = pymunk.Space()
space.gravity = (0, 9.8)

clock = pygame.time.Clock()
FPS = 60
dt = 1/FPS

class Ball:
    def __init__(self):
        self.mass = 30
        self.radius = 10

# Create ball
body = pymunk.Body(50, 50, body_type=pymunk.Body.DYNAMIC)
body.position = (WIDTH/2, 0)
shape = pymunk.Circle(body, 10)
space.add(body, shape)

while run:
    clock.tick(FPS)
    space.step(dt)
    screen.fill('white')

    pygame.draw.circle(screen, 'red', shape.body.position, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
exit()
