import pygame, sys, time
from pygame.locals import *
from random import *

def exit_game():
    sys.exit()

def run_game():

    global x, position
    x, position = 3, (0, 0)
    
    pygame.init()

    SIZE = (400, 400)
    BG_COLOUR = (255,255,255)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Mole_Mash")
    clock = pygame.time.Clock()

    Mole = pygame.image.load("Originals/mole_sprite.png")
    

    while True:
        time_passed = clock.tick(30)
        for event in pygame.event.get():
                if event.type == QUIT:
                    quit()

        screen.fill(BG_COLOUR)
        time = pygame.time.get_ticks()/1000

        def control():
            global x, position

            if time > x:
               
                x += 1
                position = (randint(1, 300), randint(1, 300))
            
            return position

        screen.blit(Mole, (control()))
        
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
