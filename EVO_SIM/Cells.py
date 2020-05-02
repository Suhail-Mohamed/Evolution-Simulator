import pygame
import random
from random import randint
import math


Width = 700 #game window width
Height = 700 #game window height
wind = pygame.display.set_mode((Width, Height)) #set the game window

def distance(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

class CELLS:
    def __init__(self):
        
        self.x = random.randrange(0,Width)
        self.y = random.randrange(0,Height)
        self.strength = random.randrange(1,30)
        self.health = 100
        self.closest_food = [] #an array where the closest food to the cell goes inside of
        
        if(self.strength > 18):
            self.speed = random.randrange(1,15)
            self.sense = random.randrange(5,20)
        elif(self.strength >= 10 and self.strength <= 18):
            self.speed = random.randrange(5,15)
            self.sense = random.randrange(5,25)
        else:
            self.speed = random.randrange(6,20)
            self.sense = random.randrange(25,35)
 
        if(self.strength > 18):
            self.size = 18
        elif(self.strength >=10 and self.strength <= 18):
            self.size = 14
        else:
            self.size = 10
    
    def Move(self):

        D = ["left","right","up","down"]
        what_direction = random.choice(D)

        #left,right,up and down
        if(what_direction == "left"): #left
            self.x-=self.speed
        elif(what_direction == "right"): #right
             self.x+=self.speed
        elif(what_direction == "up"): #up
            self.y-=self.speed
        elif(what_direction == "down"): #down
            self.y+=self.speed
        
        if(self.x + self.speed > Width):
            self.x = 0
        elif(self.x - self.speed < 0):
            self.x = Width
        
        if(self.y + self.speed > Height):
            self.y = 0
        elif(self.y - self.speed < 0):
            self.y = Height

    def draw(self):
        #based on the traits the Cells change colour
        r = max(0, min(255, 100+ self.strength*5))
        g = max(0, min(255, 100+self.speed*5))
        b = max(0, min(255, 100+self.sense*5))
        pygame.draw.ellipse(wind,(r,g,b), pygame.Rect(self.x, self.y, self.size, self.size))
        
    def eat(self,food):
        self.health += food.energy

    def energy_lost(self):
        self.health = self.health - 0.5

    def carnivore(self,cell):
        #if the difference between one cell and another is 4, the stronger cell can 
        #eat the weaker cell
        if(self.strength - cell.strength > 4):
 
            info = []
            find_smallest = []
            smallest_dist = Height + Width #arbitrary big number
        
            D = round(distance(self.x,self.y,cell.x,cell.y))

            if (D < self.sense):
                info = [cell,D]
                find_smallest.append(info)
            
            for i in range (len(find_smallest)):
                if(find_smallest[i][1] < smallest_dist):
                    F = find_smallest[i][0]
                    self.closest_food = [F.get_coordinates(),F.size]         
        else:
            pass    
    
    def eat_prey(self,cell):
        Prob = random.uniform(0,1)
        #there is a 40% chance the cell with actually eat its prey
        if((self.strength - cell.strength) > 4 and Prob < 0.4):
            self.health+=cell.health
            cell.health = 0
    
    def find_food(self,food):
        info = []
        find_smallest = []
        smallest_dist = Height + Width #arbitrary big number
    
        D = round(distance(self.x,self.y,food.x,food.y))

        if (D < self.sense):
            info = [food,D]
            find_smallest.append(info)
        
        for i in range (len(find_smallest)):
            if(find_smallest[i][1] < smallest_dist):
                F = find_smallest[i][0]
                self.closest_food = [F.get_coordinates(),F.size]
                  
    def go_to(self):
        the_foodx = self.closest_food[0][0]
        the_foody = self.closest_food[0][1]
        the_foodsize = self.closest_food[1]

        if(self.x + self.size < the_foodx ):
            self.x+=self.speed
        if(self.x > the_foodx + the_foodsize):
            self.x-=self.speed

        if(self.y > the_foody + the_foodsize):
            self.y-=self.speed
        if(self.y + self.size < the_foody):
            self.y+=self.speed
    
    def prey_run(self,cell):
        if(cell.strength - self.strength > 4):
            #this thing can eat you
            if(distance(self.x,self.y,cell.x,cell.y) < self.sense):
                #it is close

                # non-diagonal cases 
                if(cell.x == self.x):
                    self.y+=self.speed
                if(cell.y == self.y):
                    self.x+=self.speed

                # They are at a diagonal to you          
                if(self.x - cell.x > 0):                
                    self.x+=self.speed                 
                else:                               
                    self.x-=self.speed

    def get_coordinates(self):
        coordinates = [self.x, self.y]
        return coordinates
    
    def live (self):
        self.Move()
        self.energy_lost()

        if(len(self.closest_food) > 0):
            self.go_to()
            self.closest_food = []
