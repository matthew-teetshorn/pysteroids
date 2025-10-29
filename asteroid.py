import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        # if small asteroid return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # if larger asteroid split and spawn smaller asteroids
        new_angle = random.uniform(ASTEROID_NEW_ANGLE_MIN, ASTEROID_NEW_ANGLE_MAX)
        vector_1 = self.velocity.rotate(new_angle)
        vector_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector_1 * ASTEROID_NEW_VEL_K
        new_asteroid_2.velocity = vector_2 * ASTEROID_NEW_VEL_K