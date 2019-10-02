import pygame
import random
from random import randint
import math
from Cells import CELLS,Width,Height,wind

class Child_cell(CELLS):

    def __init__(self,p1_st,p2_st,p1_se,p2_se,p1_sp,p2_sp):

        Mutation = random.randrange(-7,7)
        
        self.x = random.randrange(0,Width)
        self.y = random.randrange(0,Height)
        self.health = 100
        self.closest_food = []
        self.strength = (p1_st + p2_st)/2 + 2*Mutation
        self.sense = (p1_se + p2_se)/2 + Mutation
        self.speed = (p1_sp + p2_sp)/2

        if(self.speed < Mutation):
            self.speed = self.speed + random.randrange(1,5)
          
        if(self.strength > 18):
            self.size = 18
        elif(self.strength >=10 and self.strength <= 18):
            self.size = 14
        else:
            self.size = 10
         

