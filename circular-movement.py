"""
El presente programa simula movimientos circulares.
"""

import pygame
from math import cos, sin, pi, radians, degrees
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
    def __init__(self, colour, vel0deg, accel_ang, r):
        # Apariencia de la partícula
        self.radius = 10  # px
        self.colour = colour
        # Características del movimiento circular
        self.RADIUS = r  # px
        self.circ_centerx = WIDTH/2
        self.circ_centery = HEIGHT/2
        self.circ_center = (self.circ_centerx, self.circ_centery)
        # Ecuaciones del movimiento circular
        # Ecuaciones circulares
        self.accel_ang = accel_ang
        self.vel0ang = radians(vel0deg)  # rad/s
        self.vel_ang = self.vel0ang
        self.angular0 = 0  # radianes
        self.angular = self.angular0
        # Ecuaciones tangenciales
        self.accel_tan = self.RADIUS*self.accel_ang
        self.vel_tan = self.RADIUS*self.vel_ang
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
        self.accel_tan = self.RADIUS*self.accel_ang
        self.vel_tan = self.RADIUS*self.vel_ang
        # Posiciones
        self.pos_y = self.circ_centery + self.RADIUS*sin(self.angular)
        self.pos_x = self.circ_centerx + self.RADIUS*cos(self.angular)

    def draw(self):
        # Dibujar trayectoria circular
        pygame.draw.circle(screen, 'white', self.circ_center, self.RADIUS, width=1)
        # Dibujar posición de partícula
        pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.radius)


# Resetear simulación
def reset(particle):
    global TIME
    TIME = 0
    # Reset velocity and positions
    particle.pos_x = particle.pos0x
    particle.pos_y = particle.pos0y


# Imprimir información en pantalla
def plot(particle):
    text_y_pos = 20
    text_x_pos = 550
    # Tabla de información
    datas = [[':****INFORMACIÓN****', ''],
             ['Tiempo (s)', round(TIME, 2)],
             ['Posición X (px)', round(particle.pos_x, 2)],
             ['Posición Y (px)', round(particle.pos_y, 2)],
             [':--Información angular--', ''],
             ['Aceleración angular(rad/s2): ', particle.accel_ang],
             ['Velocidad angular (rad/s): ', round(particle.vel_ang, 2)],
             ['Posición angular (grados)', f'{round(degrees(particle.angular), 1)}º'],
             [':--Información tangencial--', ''],
             ['Aceleración tangencial (px/s2): ', round(particle.accel_tan, 2)],
             ['Velocidad tangencial (px/s): ', round(particle.vel_tan, 2)]]
    # Renderizar información
    for info, data in datas:
        text = font.render(f'{info}: {data}', False, 'white')
        screen.blit(text, (text_x_pos, text_y_pos))
        text_y_pos += 20


p1 = Particle('red', 50, -0.01, 100)

# Bucle principal de simulación
while run:
    clock.tick(FPS)
    screen.fill('black')

    # Dibujar Partículas
    p1.draw()
    p1.update()

    # imprimir información
    plot(p1)

    # Actualizar el tiempo y movimiento
    TIME += dt

    for event in pygame.event.get():
        # Salir programa
        if event.type == pygame.QUIT:
            run = False
        # Resetear programa
        if event.type == pygame.KEYDOWN:
            # Resetear programa con datos actuales
            if event.key == pygame.K_ESCAPE:
                reset(p1)
            # Resetear simulación cambiando datos del ángulo de tiro
    pygame.display.flip()
pygame.quit()
quit()
