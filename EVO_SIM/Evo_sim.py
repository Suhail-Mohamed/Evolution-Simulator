import pygame
import random
from random import randint
import math
from Cells import CELLS,Width,Height,distance,wind
from Food import FOOD
from Child import Child_cell
pygame.init()


Fps = 800  #game's speeds
Num_cells = 20
Num_food = 60
All_food = []
All_cells = []


def Around(cell,food):
    if (cell.x+cell.size>=food.x>=cell.x and cell.y+cell.size>=food.y>=cell.y):
        return True
    elif (cell.x+cell.size>=food.x+food.size>=cell.x and cell.y+cell.size>=food.y>=cell.y):
        return True
    elif (cell.x+cell.size>=food.x>=cell.x and cell.y+cell.size>=food.y+food.size>=cell.y):
        return True
    elif (cell.x+cell.size>=food.x+food.size>=cell.x and cell.y+cell.size>=food.y+food.size>=cell.y):
        return True

    elif((cell.x == food.x and cell.y == food.y) or (distance(cell.x,cell.y,food.x,food.y) < cell.speed)):
        return True
    else:
        return False

def make_food():
    for i in range(Num_food):
        F = FOOD()
        All_food.append(F)

def make_cells():
    for i in range(Num_cells):
        C = CELLS()
        All_cells.append(C)

def remove_dead():
    the_dead = []

    if(len(All_cells) == 0):
        return 
    
    for x in range(len(All_cells)):
        if(All_cells[x].health <= 0 ):
            the_dead.append(x)

    the_dead.reverse()

    for j in range(len(the_dead)):
        del All_cells[the_dead[j]]
          
def Game():

    make_food()
    make_cells()

    Running = True
    
    while Running:

        avg_speed = 0
        avg_strength = 0
        avg_sense = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        wind.fill((255, 255, 255))
        
        for i in All_cells:
            i.live()
            i.draw()

        for f in All_food:
            f.draw()

    
        if(len(All_cells) > 0):
           
            for j in range(len(All_cells)):
                for i in range(len(All_cells)):
                    if(All_cells[i].health > 75 and All_cells[j].health > 75):
                        All_cells[i].health-=75
                        All_cells[j].health-=75
                        Ch = Child_cell(All_cells[i].strength,All_cells[j].strength,All_cells[i].sense,All_cells[j].sense,All_cells[i].speed,All_cells[j].speed)
                        All_cells.append(Ch)
                        
                        
            for j in range(len(All_cells)):
                for i in range(len(All_cells)):
                    All_cells[j].prey_run(All_cells[i])  
            
            for j in range(len(All_cells)):
                for i in range(len(All_food)):
                    All_cells[j].find_food(All_food[i])
                    if(Around(All_cells[j], All_food[i])):
                        All_cells[j].eat(All_food[i])
                        All_food[i].delete()
            
            for j in range(len(All_cells)):
                for i in range(len(All_cells)):
                    All_cells[j].carnivore(All_cells[i])
                    if(Around(All_cells[j], All_cells[i])):
                        All_cells[j].eat_prey(All_cells[i])  

            
            remove_dead()

        for i in range(len(All_cells)):
            avg_speed = avg_speed + All_cells[i].speed
            avg_strength = avg_strength + All_cells[i].strength
            avg_sense = avg_sense + All_cells[i].sense

        length = len(All_cells)

        print("__________________")
        print("STATS:")
        print("******")
        print("AVERAGE SPEED: ", avg_speed/length)
        print("AVERAGE SENSE: ", avg_sense/length)
        print("AVERAGE STRENGTH: ", avg_strength/length)
        print("------------------")
                            
        pygame.display.update()
        pygame.time.Clock().tick(Fps)
        

Game()


