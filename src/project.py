import pygame
import os
import random


class Surface():

    def __init__(self, resolution, size=15, color=pygame.Color(0, 0, 0), life=1000, direction=""):
        self.pos = resolution
        self.size = size
        self.color = color
        self.life = life
        self.direction = direction
        self.age = 0
        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        if self.direction == "up":
            self.direction_up()
        elif self.direction == "down":
            self.direction_down()

        self.update_surface()

        self.age += dt
        # Sets 255 as the maximum limit \/
        self.alpha = min(255, 255 * (self.age / self.life))
        if self.alpha == 255:
            return


    def direction_up(self):
        x, y = self.pos
        y -= self.size/1.5
        self.pos = (x, y)
        

    def direction_down(self):
        x, y = self.pos
        y += self.size/1.5
        self.pos = (x, y)

    def update_surface(self):
        surf = pygame.Surface((self.size*13.5, self.size))
        surf.fill(self.color)
        self.surface = surf
        return surf

    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)

class MultiSurfaces:
    def __init__(self, resolution):
        self.pos = resolution
        self.particles = [Surface(self.pos), Surface(self.pos), Surface(self.pos), Surface(self.pos)]
        self.multiSurfaces = self.update()
        
    def update(self):
        self._update_color()
        self._update_position()
        self._set_directions()
        
    def _update_color(self):
        # Red    
        self.particles[0].color = (255, 0, 0)
        # Green
        self.particles[1].color = (0, 255, 0)
        # White
        self.particles[2].color = (255, 255, 255)
        # Blue
        self.particles[3].color = (0, 0, 255)

    def _update_position(self):
        self.particles[0].pos = (0, self.pos[1] - 5)
        self.particles[1].pos = (self.pos[0] / 3.9, -10)
        self.particles[2].pos = (410, self.pos[1])
        self.particles[3].pos = (self.pos[0] / 1.3, -10)

    def _set_directions(self):
        self.particles[0].direction = "up"
        self.particles[1].direction = "down"
        self.particles[2].direction = "up"
        self.particles[3].direction = "down"

    def draw(self, screen):
        for particle in self.particles:
            particle.set_alpha(self.alpha)
            screen.blit(particle.surface, particle.pos)

class FireParticles():
    
    resolution_width = 800
    resolution_height = 600

    alpha_layer_qty = 2
    alpha_glow_difference_constant = 2

    def __init__(self, x=resolution_width // 2, y=resolution_height // 2, r=5):
        self.x = x
        self.y = y
        self.radius = r
        self.original_r = r
        self.alpha_layers = FireParticles.alpha_layer_qty
        self.alpha_glow = FireParticles.alpha_glow_difference_constant
        max_surf_size = 2 * self.radius * self.alpha_layers * self.alpha_layers * self.alpha_glow
        self.surf = pygame.Surface((max_surf_size, max_surf_size), pygame.SRCALPHA)
        self.burn_rate = 0.1 * random.randint(1, 4)

    def update(self):
        self.y -= 7 - self.radius
        self.x += random.randint(-self.radius, self.radius) 
        self.original_r -= self.burn_rate
        self.radius = int(self.original_r)
        if self.r <= 0:
            self.r = 1

    def draw(self, screen):
        max_surf_size = 2 * self.radius * self.alpha_layers * self.alpha_layers * self.alpha_glow
        self.surf = pygame.Surface((max_surf_size, max_surf_size), pygame.SRCALPHA)
        for i in range(self.alpha_layers, -1, -1):
            alpha = 255 - i * (255 // self.alpha_layers - 5)
            if alpha <= 0:
                alpha = 0
            radius = self.radius * i * i * self.alpha_glow
            if self.radius == 4 or self.radius == 3:
                r, g, b = (255, 0, 0)
            elif self.radius == 2:
                r, g, b = (255, 150, 0)
            else:
                r, g, b = (50, 50, 50)
            color = (r, g, b, alpha)
            pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), radius)
        screen.blit(self.surf, self.surf.get_rect(center=(self.x, self.y)))

class Fire:

    resolution_width = 800
    resolution_height = 600

    def __init__(self, x=resolution_width // 2, y=resolution_height // 2):
        self.x = x
        self.y = y
        self.flame_intensity = 2
        self.flame_particles = []
        #for i in range(self.flame_intensity * 25):
            #self.flame_particles.append(FireParticles(self.x + random.randint(-5, 5), self.y, random.randint(1, 5)))

    def draw(self):
        for i in self.flame_particles:
            if i.original_r <= 0:
                self.flame_particles.remove(i)
                #self.flame_particles.append(FireParticles(self.x + random.randint(-5, 5), self.y, random.randint(1, 5)))
                del i
                continue
            i.update()
            i.draw()

def main():
    pygame.init()
    pygame.display.set_caption("Elements Screen")

    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    surfaces = MultiSurfaces(resolution)
    flame = Fire(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                event.w
                event.h
                resolution = (event.w, event.h)
                screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
                surfaces = MultiSurfaces(resolution)
            if event.type == pygame.QUIT:
                running = False

        flame.draw()

        for particle in surfaces.particles:
            particle.update(dt)

        black = pygame.Color(0, 0, 0)
        #screen.fill(black)
        for particle in surfaces.particles:
            particle.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()
