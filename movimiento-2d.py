"""
El presente programa simula tiro horizontal.
Cambiando las variables iniciales se puede utilizar para cualquier tiro oblicuo
"""

import pygame
from math import cos, sin, pi
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

# Listas de posiciones y velocidades para graficar
y_axis = []
x_axis = []
time_array = []
SAVED_GRAPHS = False


# Funciones de pasaje de unidades
# Metros a pixel
def convert_to_pixel(meter):
    return (LEN_Y_AXIS / len_y_axis) * meter


# Pixel a metros
def convert_to_meter(pixel):
    return (len_y_axis / LEN_Y_AXIS) * pixel


# Grados a radianes
def convert_to_radiant(degree):
    return (pi / 180) * degree


# Radianes a grados
def convert_to_degree(radiant):
    return (180 / pi) * radiant


# Clase partícula
class Particle:
    def __init__(self, colour):
        # Cuerpo
        self.radius = 10
        self.colour = colour
        self.is_moving = True
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
        # Trayectoria
        self.trajectory = []

    # Actualizar ecuaciones de posiciones
    def update(self):
        global x_axis
        global y_axis
        global time_array
        # eje x
        self.vel_x = self.vel0x + self.accel_x*TIME
        self.pos_x = self.pos0x + self.vel_x*TIME
        # eje y
        self.vel_y = self.vel0y + self.accel_y*TIME
        self.pos_y = self.pos0y - self.vel0y*TIME - (self.accel_y/2)*pow(TIME, 2)
        # Parar movimiento si llega objeto choca contra piso
        if (self.pos_y + 10) >= Y_MIN:
            self.is_moving = False
        # Actualizar listas de posiciones, velocidades y tiempo
        x_axis.append(round(convert_to_meter(abs(self.pos_x - X_MIN)), 2))
        y_axis.append(round(convert_to_meter(abs(self.pos_y - Y_MIN)), 2))
        time_array.append(TIME)
        # Actualizar centro de partícula
        self.center = (self.pos_x, self.pos_y)
        self.trajectory.append((int(self.pos_x), int(self.pos_y)))

    # Dibujar partícula a pantalla
    def draw(self):
        # Dibujar trayectoria trayectoria
        for dot in self.trajectory:
            screen.set_at(dot, (255, 255, 0))
        # Dibujar el cuerpo
        pygame.draw.circle(screen, self.colour, self.center, self.radius)


# Resetear programa
def reset(particle):
    global TIME
    TIME = 0
    # Reset velocity and positions
    particle.vel0x = convert_to_pixel(cos(angle) * vel)
    particle.vel0y = convert_to_pixel(sin(angle) * vel)
    particle.pos_x = particle.pos0x
    particle.pos_y = particle.pos0y
    # Clear array
    particle.trajectory.clear()
    time_array.clear()
    x_axis.clear()
    y_axis.clear()
    # Reset movement
    p1.is_moving = True


# Imprimir información a pantalla
def plot(particle):
    """
    Función imprime todos los datos que van dentro de la lista 'data',
    en borde superior izquierdo de la pantalla.
    :return:
    """
    text_y_pos = 20
    text_x_pos = 590
    # Tabla de información
    datas = [[':****INFORMACIÓN****', ''],
             ['Tiempo (s)', round(TIME, 2)],
             ['Distancia x (m)', round(convert_to_meter(abs(particle.pos_x - X_MIN)), 2)],
             ['Altura h (m)', round(convert_to_meter(abs(particle.pos_y - Y_MIN)), 2)],
             ['Velocidad x (m/s)', round(convert_to_meter(particle.vel_x), 2)],
             ['Velocidad y (m/s)', round(convert_to_meter(particle.vel_y), 2)],
             [':---------', ''],
             ['Altura de tiro (m): ', len_y_axis],
             ['Velocidad inicial (m/s)', vel],
             ['Ángulo de tiro (grados)', f'{round(convert_to_degree(angle), 1)}º']]
    # Renderizar información
    for info, data in datas:
        text = font.render(f'{info}: {data}', False, 'white')
        screen.blit(text, (text_x_pos, text_y_pos))
        text_y_pos += 20


def _plot(ax, x_data, y_data, f_name):
    ax.plot(x_data, y_data)
    ax.set_xlabel('Eje X', fontsize=8)
    ax.set_ylabel('Eje Y', fontsize=8)
    ax.set_title(f_name, fontsize=10)
    ax.grid(visible=True, linestyle=':', linewidth=0.5)
    return ax


p1 = Particle('red')

# Bucle principal de simulación
while run:
    clock.tick(FPS)
    screen.fill('black')

    # Dibujar bordes
    pygame.draw.line(screen, 'white', (X_MIN, Y_MAX), (X_MIN, Y_MIN))  # línea vertical
    pygame.draw.line(screen, 'white', (X_MIN, Y_MIN), (X_MAX, Y_MIN))  # línea horizontal

    # imprimir información
    plot(p1)

    # Actualizar el tiempo y movimiento si no choca con el piso
    if p1.is_moving:
        p1.update()
        TIME += dt
    else:
        # Graficar luego de que la pelota caiga al piso
        if not SAVED_GRAPHS:
            fig, ax = plt.subplots(1, 1, figsize=(10, 5))
            _plot(ax, x_axis, y_axis, 'Y en función de X')
            fig.savefig('./graphs/y_en_x.jpg')
            fig, ax = plt.subplots(1, 1, figsize=(10, 5))
            _plot(ax, time_array, x_axis, 'X en función de tiempo')
            fig.savefig('./graphs/x_en_t.jpg')
            fig, ax = plt.subplots(1, 1, figsize=(10, 5))
            _plot(ax, time_array, y_axis, 'Y en función de tiempo')
            fig.savefig('./graphs/y_en_t.jpg')
            SAVED_GRAPHS = True
    p1.draw()

    # Debug
    # print(p1.center, p1.vel0y)

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
            if event.key == pygame.K_UP:
                angle = convert_to_radiant(convert_to_degree(angle) + 1)
                reset(p1)
            if event.key == pygame.K_DOWN:
                angle = convert_to_radiant(convert_to_degree(angle) - 1)
                reset(p1)
            # Resetear simulación cambiando datos de la velocidad
            if event.key == pygame.K_RIGHT:
                vel += 1  # m/s
                reset(p1)
            if event.key == pygame.K_LEFT:
                vel -= 1  # m/s
                reset(p1)

    pygame.display.flip()
pygame.quit()
quit()

