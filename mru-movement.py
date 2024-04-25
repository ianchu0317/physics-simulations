import pygame

pygame.init()
run = True

# Colours settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Display settings
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('MRU Simulation')

# Frame settings
FPS = 60
clock = pygame.time.Clock()

# X_POS, Y_POS of trajectory
Y_POS = 300
X_POS = 10


class Particle:
    def __init__(self, colour, velocity, acceleration):
        self.radius = 10
        self.colour = colour
        self.vel = velocity
        self.accel = acceleration
        self.X_POS = X_POS
        self.is_moving = False
        self.moving_right = True

    def move(self):
        # Reset position if passed screen width
        if self.X_POS > WIDTH:
            self.X_POS = 0
        if self.X_POS < 0:
            self.X_POS = WIDTH

        # Move x position coordinates if particle is moving
        if self.is_moving:
            self.vel += self.accel  # MRUV case, acceleration not 0
            if self.moving_right:
                self.X_POS += self.vel
            else:
                self.X_POS -= self.vel

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.X_POS, Y_POS), self.radius)


p1 = Particle(BLUE, 2, 0)

while run:
    clock.tick(FPS)

    # Screen background settings
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, Y_POS), (WIDTH, Y_POS))

    p1.draw()
    p1.move()

    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            run = False
        # Player control direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.is_moving = not p1.is_moving
            if event.key == pygame.K_LEFT:
                p1.is_moving = True
                p1.moving_right = False
            if event.key == pygame.K_RIGHT:
                p1.is_moving = True
                p1.moving_right = True

    pygame.display.flip()

pygame.quit()
quit()
