"""
El presente programa simula tiro horizontal.
Cambiando las variables iniciales se pueden
"""

import pygame
from math import cos, sin, pi

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

# Configuraciones globales de la simulación
# Posiciones en pixeles
Y_MAX = 300  # Altura máxima de tiro
Y_MIN = 600  # Altura mínima (piso)
X_MIN = 100  # Piso inicio
X_MAX = 700  # Piso longitud maxima
LEN_Y_AXIS = abs(Y_MAX - Y_MIN)  # Altura en píxeles
LEN_X_AXIS = abs(X_MAX - X_MIN)  # Distancia en píxeles

# Información de partícula del enunciado (UNIDADES FÍSICAS)
vel = 20  # m/s
angle = pi/6  # radianes
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


# Clase partícula
class Particle:
    def __init__(self, colour):
        # Cuerpo
        self.radius = 10
        self.colour = colour
        # Ecuaciones y variables iniciales
        # Eje y en píxeles
        self.accel_y = convert_to_pixel(accel_y)  # Gravedad en píxeles
        self.vel0y = convert_to_pixel(sin(angle) * vel)
        self.vel_y = self.vel0y
        self.pos0y = Y_MIN - convert_to_pixel(len_y_axis)
        self.pos_y = self.pos0y
        # Eje x en píxeles
        self.accel_x = 0
        self.vel0x = convert_to_pixel(cos(angle) * vel)
        self.vel_x = self.vel0x
        self.pos0x = X_MIN
        self.pos_x = self.pos0x
        # Centro de partícula (x, y)
        self.center = (self.pos_x, self.pos_y)

    # Actualizar ecuaciones de posiciones
    def update(self):
        # eje x
        self.vel_x = self.vel0x + self.accel_x*TIME
        self.pos_x = self.pos0x + self.vel_x*TIME
        # eje y
        self.vel_y = self.vel0y + self.accel_y*TIME
        self.pos_y = self.pos0y - self.vel0y*TIME - (self.accel_y/2)*pow(TIME, 2)
        # centro partícula
        self.center = (self.pos_x, self.pos_y)

    # Dibujar partícula a pantalla
    def draw(self):
        pygame.draw.circle(screen, self.colour, self.center, self.radius)


# Resetear programa
def reset(particle):
    global TIME
    TIME = 0
    particle.pos_x = particle.pos0x
    particle.pos_y = particle.pos0y


# Imprimir información a pantalla
def plot(particle):
    """
    Función imprime todos los datos que van dentro de la lista 'data',
    en borde superior izquierdo de la pantalla.
    :return:
    """
    text_y_pos = 20
    text_x_pos = 620
    # Tabla de información
    datas = [['****INFORMACIÓN****', ''],
             ['Tiempo (s)', round(TIME, 2)],
             ['Distancia x (m)', round(convert_to_meter(abs(particle.pos_x - X_MIN)), 2)],
             ['Altura h (m)', round(convert_to_meter(abs(particle.pos_y - Y_MIN)), 2)],
             ['Velocidad x (m/s)', round(convert_to_meter(particle.vel_x), 2)],
             ['Velocidad y (m/s)', round(convert_to_meter(particle.vel_y), 2)]]
    # Renderizar información
    for info, data in datas:
        text = font.render(f'{info}: {data}', False, 'white')
        screen.blit(text, (text_x_pos, text_y_pos))
        text_y_pos += 20


p1 = Particle('red')

# Bucle principal de simulación
while run:
    clock.tick(FPS)
    screen.fill('black')

    # Dibujar bordes
    pygame.draw.line(screen, 'white', (X_MIN, Y_MAX), (X_MIN, Y_MIN))  # línea vertical
    pygame.draw.line(screen, 'white', (X_MIN, Y_MIN), (X_MAX, Y_MIN))  # línea horizontal

    # Actualizar partícula
    p1.draw()
    p1.update()

    # imprimir información
    plot(p1)

    # Actualizar el tiempo
    TIME += dt

    # Debug
    # print(p1.center, p1.vel0y)

    for event in pygame.event.get():
        # Salir programa
        if event.type == pygame.QUIT:
            run = False
        # Resetear programa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset(p1)

    pygame.display.flip()
pygame.quit()
quit()

