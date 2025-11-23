import pygame
from PIL import Image


class Surface():

    def __init__(self, pos=(0, 0), size=15, life=1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 0, 0)
        self.age = 0
        self.life = life
        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        self.alpha = 255 * (1 - (self.age / self.life))
        self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size*13.5, self.size))
        surf.fill(self.color)
        self.surface = surf
        return surf

    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)



def main():
    pygame.init()
    pygame.display.set_caption("Zodiac Legends Title Screen")

    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    # List of 4 particles
    particles = [Surface(), Surface(), Surface(), Surface()]
    # List of positions
    new_positions = [(0, 588), (205, 0), (415, 588), (610, 0)]
    # List of colors (red, green, white, blue)
    new_color = [(255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255)]

    
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    particle = Surface(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for particle in particles:
            particle.update(dt)

        for i, particle in enumerate(particles):
            particle.pos = new_positions[i]
            particle.color = new_color[i]

        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        #particle.pos = (resolution[0]//2, resolution[0]//2)
        for particle in particles:
            particle.draw(screen)
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
