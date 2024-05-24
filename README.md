# physics-simulations
Repositorio con simulaciones de Física.

--- 
## Movimiento 2D
![tiro oblicuo](https://github.com/ianchu0317/physics-simulations/assets/71509578/c338e71d-ce1c-4db1-be9a-f2770cf104c0)

- Archivo: [movimiento-2d.py](https://github.com/ianchu0317/physics-simulations/blob/main/movimiento-2d.py)

El programa realiza la simulación de un tiro oblicuo y confecciona 3 tablas distintas luego de la simulación:
1. Y en función de X
2. Y en función de tiempo
3. X en función de tiempo

Para realizar distintas simulaciones se puede modificar el código cambiando las variables iniciales del enunciado dado:
```py
# Información de partícula del enunciado (UNIDADES FÍSICAS)
vel = 20  # Velocidad inicial (m/s)
angle = pi/6  # Ángulo de tiro (radianes)
# Eje y
accel_y = -10  # Gravedad 'NO CAMBIAR', CONSTANTE (m/s2)
len_y_axis = 45  # Altura de tiro (m)
```
Se puede editar la confección del código en la línea 206:
```py
fig, ax = plt.subplots(1, 1, figsize=(10, 5))  # cantidad y tamaño del gráfico
_plot(ax, x_axis, y_axis, 'título del gráfico')
fig.savefig('ubicación y nombre del archivo')      
```
#### Controles
El botón `ESC (escape)` reinicia la simulación con datos actuales. 

Los botones de `(↑) arriba` y `(↓) abajo` reinicia la simulación pero aumentando y disminuyendo respectivamente 1º (grado) el ángulo del tiro actual.

---
## Movimiento 1D
- Archivo 1: [mru-movement.py](https://github.com/ianchu0317/physics-simulations/blob/main/mru-movement.py)
- Archivo 2: [mru2.py](https://github.com/ianchu0317/physics-simulations/blob/main/mru2.py)

Estos dos archivos simulan un movimiento rectilíneo (1 dimensión, eje X). 

El programa puede ser modificado para cambiar valores de simulación:
```py
# Sintaxis: Particle(color, velocidad inicial, aceleración, está moviendo)
p1 = Particle('blue', 2, 0.01, False)
p2 = Particle('red', 3, 0, True)
```

#### Controles
El botón `SPACE (barra espaciadora)` detiene o continúa la simulación.

Los botones de ``(←) izquierda`` y ``(→) derecha`` cambian el sentido del movimiento.
