import pygame, sys
import time
from pygame.locals import *
from random import *



def exit_game():
    sys.exit()

def run_game():

    global x, position, regulator, time_data
    x, position, regulator, time_data = 0, (0, 0), 0, 0
    
    pygame.init()

    SIZE = (400, 400)
    BG_COLOUR = (255,255,255)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Mole_Mash")
    clock = pygame.time.Clock()

    Mole = pygame.image.load("Originals/mole_sprite.png")
    

    while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                    quit()

        screen.fill(BG_COLOUR)
        time = pygame.time.get_ticks()/1000

        time_data = time-regulator
        #print(time_data)

        def update_position():
            global position
            
            position = (randint(1, 300), randint(1, 300))

            return position


        def control():
            global x, position, regulator

            #print(time_data, x)

            if time_data > x:
                x += 1

                position = update_position()
            
            return position

        b = screen.blit(Mole, (control()))

        mouse = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b.collidepoint(mouse):
            regulator = time
            x = 0
            update_position()

        
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
