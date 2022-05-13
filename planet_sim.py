"""
This is a simulation of the orbit of planets in our solar system
"""
from operator import truediv
import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Planet simulation!')
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (200,29,50)
DARK_GREY = (80,78,81)
class Planet:
    AU = 149.6e6 * 1000 # constant equal to distance from earth to sun in meters
    G = 6.67428e-11  # gravity constant
    SCALE = 250 / AU # 1AU = 100 pixels
    TIMESTEP = 3600 * 24 # One day

    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x,y), self.radius)
    
    # Im not gonna pretend to understand physics, but this works so...
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        if other.sun:
            self.distance_to_sun = distance
       
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.TIMESTEP # This is just f=m/a and the shove it into self.x_vel
        self.y_vel += total_fy / self.mass * self.TIMESTEP # Repeat for y

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x,self.y))





def main():
    run = True
    clock = pygame.time.Clock()
    sun = Planet(0, 0, 35, YELLOW, 1.98892 * 10e30)
    sun.sun = True
    
    earth =  Planet(-1 * Planet.AU, 0, 14, BLUE, 5.9742 * 10e24)

    mars = Planet(-1.524 * Planet.AU, 0, 10, RED, 6.39 * 10e23)
    
    mercury = Planet(0.387 * Planet.AU, 0, 6, DARK_GREY, 0.330 * 10e24)
    
    venus = Planet(0.723 * Planet.AU, 0, 12, WHITE, 4.8685 * 10e24)
    
    planets = [sun, earth, mars, mercury, venus]



    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
        
        pygame.display.update()
    
    pygame.quit()  

main()
