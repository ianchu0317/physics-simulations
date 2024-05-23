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
# global time
TIME = 0
dt = 0.1
# Particles group
particles = pygame.sprite.Group()


# Particle class
class Particle(pygame.sprite.Sprite):
    def __init__(self, colour, velocity, acceleration, is_moving):
        super().__init__()
        # Aspects variables
        self.radius = 10
        self.colour = colour
        # Movement variables
        # Initial variables
        self.vel0 = velocity
        self.x_pos0 = X_POS
        # Mru variables for equation
        self.accel = acceleration
        self.vel = None
        self.x_pos = None
        # Static and direction
        self.is_moving = is_moving
        self.moving_right = True

    def update(self):
        # Update movement equations
        self.vel = self.vel0 + self.accel*dt
        self.x_pos = self.x_pos0 + self.vel0*dt + (self.accel/2)*dt**2
        # Reset position
        if self.x_pos > WIDTH:
            self.x_pos = 0

    def draw(self):
        print(self.x_pos, Y_POS)
        pygame.draw.circle(screen, self.colour, (self.x_pos, Y_POS), self.radius)


def update():
    # Update particles position and movements
    for particle in particles:
        particle.update()
        particle.draw()


def plot():
    # Plot all particles
    y_pos = 20
    for particle in particles:
        # Render texts into surfaces
        p_name = font.render(f'Particle: {particle.colour}', False, WHITE)
        accel_text = font.render(f'Acceleration: {particle.accel}', False, WHITE)
        vel_text = font.render(f'Velocity: {round(particle.vel, 2)}', False, WHITE)
        x_pos_text = font.render(f'X position: {round(particle.x_pos, 2)}', False, WHITE)
        p_info = [p_name, accel_text, vel_text, x_pos_text]

        # Plot movement information: acceleration, velocity, x position, time
        for text in p_info:
            screen.blit(text, (10, y_pos))
            y_pos += 20

        y_pos += 30


p1 = Particle('blue', 2, 1, False)
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

    # Update time
    TIME += dt
    dt += 0.1

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
