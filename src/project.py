import pygame
from PIL import Image


class SomeClass():

    def method_1():
        ...

    def method_2():
        ...

    def method_n():
        ...



def main():
    pygame.init()
    pygame.display.set_caption("Zodiac Legends Title Screen")

    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
    pygame.quit()

def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
