"""
El presente programa simula movimientos circulares.
"""

import pygame
from math import cos, sin, pi, radians
from matplotlib import pyplot as plt

# Iniciar módulos
pygame.init()
run = True

# Configuraciones de pantalla
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Configuraciones actualización de la pantalla
FPS = 60
clock = pygame.time.Clock()

# Tiempo
dt = 1/FPS  # variación de tiempo
TIME = 0  # tiempo total de simulación

# Configuraciones de textos
pygame.font.init()
font = pygame.font.SysFont('arial', 15)


# Conversion de grados a radianes
def convert_to_radiant(degree):
    return (pi / 180) * degree


# Conversión radianes a grados
def convert_to_degree(radiant):
    return (180 / pi) * radiant


# Clase de la partícula
class Particle:
    def __init__(self, colour, vel0deg):
        # Apariencia de la partícula
        self.radius = 10  # px
        self.colour = colour
        # Características del movimiento circular
        self.RADIUS = 100  # px
        self.circ_centerx = WIDTH/2
        self.circ_centery = HEIGHT/2
        self.circ_center = (self.circ_centerx, self.circ_centery)
        # Ecuaciones del movimiento circular
        # Ecuaciones circulares
        self.accel_ang = 0
        self.vel0ang = radians(vel0deg)  # rad/s
        self.vel_ang = self.vel0ang
        self.angular0 = 0  # radianes
        self.angular = self.angular0
        # Ecuaciones tangenciales
        # Eje Y
        self.pos0x = WIDTH/2 + self.RADIUS
        self.pos_x = self.pos0x
        # Eje X
        self.pos0y = HEIGHT/2
        self.pos_y = self.pos0y

    # Actualizar partícula
    def update(self):
        # Actualizar ecuaciones angulares
        self.vel_ang = self.vel0ang + self.accel_ang*TIME
        self.angular = self.angular0 - self.vel0ang*TIME + (self.accel_ang/2)*pow(TIME, 2)
        # Actualizar ecuaciones tangenciales (de posición)
        self.pos_y = self.circ_centery + self.RADIUS*sin(self.angular)
        self.pos_x = self.circ_centerx + self.RADIUS*cos(self.angular)

    def draw(self):
        # Dibujar trayectoria circular
        pygame.draw.circle(screen, 'white', self.circ_center, self.RADIUS, width=1)
        # Dibujar posición de partícula
        pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.radius)


p1 = Particle('red', 50)

# Bucle principal de simulación
while run:
    clock.tick(FPS)
    screen.fill('black')

    # Dibujar Partículas
    p1.draw()
    p1.update()

    # imprimir información

    # Actualizar el tiempo y movimiento
    TIME += dt

    for event in pygame.event.get():
        # Salir programa
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
quit()
