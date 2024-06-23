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

# Manage all balls
all_balls = pygame.sprite.Group()


# Class for Ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, position):
        # physics
        super().__init__()
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
    s = pymunk.Segment(b, init, final, 10)
    s.elasticity = 0.999999
    space.add(b, s)


# Create ball on mouse click
def create_ball(position):
    ball = Ball('red', position)
    all_balls.add(ball)


create_border((0, 0), (0, HEIGHT))
create_border((0, HEIGHT), (WIDTH, HEIGHT))
create_border((0, 0), (WIDTH, 0))
create_border((WIDTH, 0), (WIDTH, HEIGHT))


while run:
    # update time
    clock.tick(FPS)
    space.step(dt)
    screen.fill('white')

    # Draw simulation borders
    pygame.draw.rect(screen, 'grey', pygame.rect.Rect(0, HEIGHT - 10, WIDTH, 10))  # bottom
    pygame.draw.rect(screen, 'grey', pygame.rect.Rect(0, 0, WIDTH, 10))  # top
    pygame.draw.rect(screen, 'grey', pygame.rect.Rect(0, 0, 10, HEIGHT))  # left
    pygame.draw.rect(screen, 'grey', pygame.rect.Rect(WIDTH - 10, 0, 10, HEIGHT))  # right
    all_balls.update()

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_ball(pygame.mouse.get_pos())

    pygame.display.flip()
pygame.quit()
exit()
