import pymunk
import pygame

# Set space
space = pymunk.Space()
space.gravity = (0, 500)

# Set body type and position
a = pymunk.Body(50, 100, body_type=pymunk.Body.DYNAMIC)
a.position = (50, 100)
# Attach body to shape
a_shape = pymunk.Poly(a, [(0, 1), (0, 3), (2, 4), (5, 6)])
space.add(a, a_shape)

print_options = pymunk.SpaceDebugDrawOptions()  # For easy printing

for _ in range(100):        # Run simulation 100 steps in total
    space.step(0.02)        # Step the simulation one step forward
    space.debug_draw(print_options)  # Print the state of the simulation
