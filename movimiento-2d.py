"""
El programa es utilizado para tiro horizontal
"""

import pygame
from math import cos, sin

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

# Configuraciones globales de la simulación
# Posiciones en pixeles
Y_MAX = 100  # Altura máxima de tiro
Y_MIN = 600  # Altura mínima (piso)
X_MIN = 100  # Piso inicio
X_MAX = 700  # Piso longitud maxima
LEN_Y_AXIS = abs(Y_MAX - Y_MIN)  # Altura en píxeles
LEN_X_AXIS = abs(X_MAX - X_MIN)  # Distancia en píxeles
# Tiempo
dt = 0.1  # variación de tiempo
TIME = 0  # tiempo total
# Información de partícula del enunciado (UNIDADES FÍSICAS)
vel = 20  # m/s
angle = 30
# Eje y
accel_y = -10  # m/s2
len_y_axis = 45  # m


# Funciones de pasaje de unidades
# Metros a pixel
def convert_to_pixel(meter):
    return (LEN_Y_AXIS / len_y_axis) * meter


# Pixel a metros
def convert_to_meter(pixel):
    return (len_y_axis / LEN_Y_AXIS) * pixel


# Información de partícula en pixeles
# Eje y
accel_y = convert_to_pixel(accel_y)
vel0y = convert_to_pixel(sin(angle)*vel)
vely = vel0y
pos0y = Y_MIN - convert_to_pixel(len_y_axis)
posy = pos0y
# Eje x
vel0x = convert_to_pixel(cos(angle)*vel)
velx = vel0x
pos0x = X_MIN
posx = pos0x
# Cuerpo
radius = 10
colour = 'red'
center = (posx, posy)


# update particle
def update():
    global posx
    global posy
    global center

    # eje x
    posx = pos0x + velx*dt

    # eje y
    posy = pos0y - vel0y*dt + (accel_y / 2)*dt**2

    center = (posx, posy)


# Draw particle
def draw():
    pygame.draw.circle(screen, colour, center, radius)


# Bucle principal de simulación
while run:
    clock.tick(FPS)
    screen.fill('black')

    # Dibujar bordes
    pygame.draw.line(screen, 'white', (X_MIN, Y_MAX), (X_MIN, Y_MIN))  # línea vertical
    pygame.draw.line(screen, 'white', (X_MIN, Y_MIN), (X_MAX, Y_MIN))  # línea horizontal

    # Partícula
    draw()
    update()

    # Debug
    print(center, convert_to_meter(posx), convert_to_meter(posy))
    # Actualizar el tiempo
    dt += 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
quit()

