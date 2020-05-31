import pygame, sys
from pygame.locals import *
from random import *

def exit_game():
    sys.exit()

def run_game():
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
        screen.blit(Mole, (randint(0, 400), randint(0, 400)))
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
