from math import cos, sin

GRAVITATIONAL_ACCELERATION = 9.8 
g = GRAVITATIONAL_ACCELERATION

def calculate_shift(t, init_speed, angle, height):
    return (
        init_speed * cos(angle) * t, # x(t)
        init_speed * sin(angle) * t - g/2 * t**2 + height  # y(t) 
    )

def calculate_velocity(t, init_speed, angle):
    return (
        init_speed * cos(angle), # x(t)
        init_speed * sin(angle) - g * t  # y(t) 
    )