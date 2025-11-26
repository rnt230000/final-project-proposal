import pygame
from PIL import Image


class Surface():

    def __init__(self, pos=(0, 0), size=15, color=pygame.Color(0, 0, 0), life=1000):
        self.pos = pos
        self.size = size
        self.color = color
        self.age = 0
        self.life = life
        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        x, y = self.pos
        y -= self.size/1.5
        self.pos = (x, y)

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

class MultiSurfaces:
    def __init__(self, pos):
        self.pos = pos
        self.particles = [Surface(), Surface(), Surface(), Surface()]
        self.multiSurfaces = self.update()
        
    def update(self):
        self._update_color()
        self._update_position()
        
    def _update_color(self):    
        self.particles[0].color = (255, 0, 0)
        self.particles[1].color = (0, 255, 0)
        self.particles[2].color = (255, 255, 255)
        self.particles[3].color = (0, 0, 255)

    def _update_position(self):
        self.particles[0].pos = (0, 588)
        self.particles[1].pos = (205, 0)
        self.particles[2].pos = (415, 588)
        self.particles[3].pos = (610, 0)

class SurfaceTrail:
    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life

    def update(self, dt):
        surface = Surface(self.pos, size=self.size)

        x, y = self.pos
        x += 7
        self.pos = (x, y)

    def _update_particle(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)

    def _update_pos(self):
        x, y = self.pos 
        y += self.size/1.5
        self.pos = (x, y)

def main():
    pygame.init()
    pygame.display.set_caption("Zodiac Legends Title Screen")

    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    surfaces = MultiSurfaces(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for particle in surfaces.particles:
            particle.update(dt)

        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        #particle.pos = (resolution[0]//2, resolution[0]//2)
        for particle in surfaces.particles:
            particle.draw(screen)
        pygame.display.flip()
        #dt = clock.tick(12)
    pygame.quit()

def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
