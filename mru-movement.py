import pygame

pygame.init()
run = True

# Colours settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Text fonts settings
pygame.font.init()
font = pygame.font.SysFont('arial', 15)

# Display settings
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('MRU Simulation')

# Frame settings
FPS = 60
clock = pygame.time.Clock()

# Global settings
# X_POS, Y_POS of trajectory
Y_POS = 300
X_POS = 10
# Particles
particles = pygame.sprite.Group()


class Particle(pygame.sprite.Sprite):
    def __init__(self, colour, velocity, acceleration, is_moving):
        super().__init__()
        self.radius = 10
        self.colour = colour
        self.vel = velocity
        self.accel = acceleration
        self.X_POS = X_POS
        self.is_moving = is_moving
        self.moving_right = True

    def move(self):
        dv = 0
        dx = 0

        # Reset position if passed screen width
        if self.X_POS > WIDTH:
            self.X_POS = 0
        if self.X_POS < 0:
            self.X_POS = WIDTH

        # Move x position coordinates if particle is moving
        if self.is_moving:
            dv += self.accel  # MRUV case, acceleration not 0
            if self.moving_right:
                dx += self.vel
            else:
                dx -= self.vel

        self.vel += dv
        self.X_POS += dx

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.X_POS, Y_POS), self.radius)


def update():
    # Update particles position and movements
    for particle in particles:
        particle.draw()
        particle.move()


def plot():
    # Plot all particles
    y_pos = 20
    for particle in particles:
        # Render texts into surfaces
        p_name = font.render(f'Particle: {particle.colour}', False, WHITE)
        accel_text = font.render(f'Acceleration: {particle.accel}', False, WHITE)
        vel_text = font.render(f'Velocity: {round(particle.vel, 2)}', False, WHITE)
        x_pos_text = font.render(f'X position: {round(particle.X_POS, 2)}', False, WHITE)
        p_info = [p_name, accel_text, vel_text, x_pos_text]

        # Plot movement information: acceleration, velocity, x position, time
        for text in p_info:
            screen.blit(text, (10, y_pos))
            y_pos += 20

        y_pos += 30


p1 = Particle('blue', 2, 0.01, False)
p2 = Particle('red', 3, 0, True)
particles.add(p1)
particles.add(p2)

while run:
    clock.tick(FPS)

    # Screen background settings
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, Y_POS), (WIDTH, Y_POS))

    # Update all particles movement
    update()
    plot()  # plot all particles

    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            run = False
        # Player control direction (only for particle 1)
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
