import pymunk
import pygame

pygame.init()
run = True

# Screen setting
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Simulation space setting
space = pymunk.Space()
space.gravity = (0, 500)

# Time setting
clock = pygame.time.Clock()
FPS = 60
dt = 1/FPS


# Class for Ball
class Ball:
    def __init__(self, color, position):
        # physics
        self.mass = 500
        self.moment = 50
        self.elasticity = 1
        # appearance
        self.color = color
        self.radius = 20
        # pymunk
        self.body = pymunk.Body(self.mass, self.moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = self.elasticity
        space.add(self.body, self.shape)

    # Update display
    def update(self):
        pygame.draw.circle(screen, self.color, self.body.position, self.radius)


# Create borders
def create_border(init, final):
    b = pymunk.Body(body_type=pymunk.Body.STATIC)
    s = pymunk.Segment(b, init, final, 5)
    s.elasticity = 0.7
    space.add(b, s)


create_border((0, 0), (0, HEIGHT))
create_border((0, HEIGHT), (WIDTH, HEIGHT))
create_border((0, 0), (WIDTH, 0))
create_border((WIDTH, 0), (WIDTH, HEIGHT))

# Create ball
b1 = Ball('blue', (WIDTH/2, 0))
b2 = Ball('red', (WIDTH/3, 0))

while run:
    # update time
    clock.tick(FPS)
    space.step(dt)
    screen.fill('white')

    b1.update()
    b2.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
exit()
