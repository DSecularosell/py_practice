"""
This is a simulation of the orbit of planets in our solar system
"""
from operator import truediv
import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Plant simulation!')

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False
    
    pygame.quit()  


main()
