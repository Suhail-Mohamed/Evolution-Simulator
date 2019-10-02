import pygame
import random
from random import randint
import math
from Cells import Width,Height,wind

class FOOD:
    def __init__(self):
       
        self.x = random.randrange(0,Width)
        self.y = random.randrange(0,Height)
        self.energy = random.randrange(10,50)
        self.colour = [0,0,0]
        self.size = 5

        if self.energy > 25:
            self.size = 10
            self.colour = [255,0,0]
        else:
            self.size = 8
            self.colour = [255,0,199]
         

    def draw(self):
        pygame.draw.rect(wind,(self.colour[0],self.colour[1],self.colour[2]),(self.x, self.y,self.size,self.size))
        #print(self.size)
    def delete(self):
         self.x = random.randrange(0,Width) 
         self.y = random.randrange(0,Height)
         #print(self.size)
         
    def get_coordinates(self):
        coordinates = [self.x, self.y]
        return coordinates


