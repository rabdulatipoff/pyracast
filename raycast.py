import math, sys, pygame
from pygame.time import delay
pygame.init()

class CVect():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def to_PVect(self):
        return PVect(math.sqrt(self.x ** 2 + self.y ** 2), math.atan(self.y / self.x))
    
class PVect():
    def __init__(self, r = 0, phi = 0):
        self.r = r
        self.phi = phi
    
    def to_CVect(self):
        return CVect(self.r * math.cos(self.phi), self.r * math.sin(self.phi))

class GameMap():
    def __init__(self, level = None, cell_size=32):
        self.level = self.maze if level is None else level
        self.size = (len(self.level), len(self.level[0]))
        self.cell_size = cell_size

    maze = [
        '##########',
        '#........#',
        '#.##.##..#',
        '#.#....#.#',
        '#.######.#',
        '#........#',
        '#........#',
        '########.#',
        '#........#',
        '##########',
    ]


class Viewport():
    def __init__(self, fov=math.radians(90), pos=CVect(), dir=PVect()):
        self.fov = fov
        self.pos = pos
        self.dir = dir

    def cast_ray(self, screen, dir, level):
        #line = CVect(5, 5), CVect(12, 8)
        cdir = dir.to_CVect()
        ray = CVect(self.pos.x, self.pos.y)
        #slope = float(cdir.y - self.pos.y) / (cdir.x - self.pos.x)
        slope = round(cdir.x) > 0 and float(cdir.y) / cdir.x or cdir.y
        while level.level[int(ray.y // level.cell_size)][int(ray.x // level.cell_size)] != '#':
            screen.set_at((int(ray.x), int(ray.y)), (255, 255, 255))
            ray.x += cdir.x
            ray.y += slope
            #print(ray.x, ray.y)
        #screen.set_at((int(ray.y), int(ray.x)), (255, 255, 255))

    def move(self, pos, level):
        if (pos.x > 0 and
            pos.x < (level.size[0] * level.cell_size) and
            pos.y > 0 and
            pos.y < (level.size[1] * level.cell_size)):
            if level.level[pos.y // level.cell_size][pos.x // level.cell_size] != '#':
                self.pos = pos

class Player():
    pass
    #x = 0
    #y = 0
    #mapc = '@'

def findplayer():
    ln = 0
    #for line in map:
    
if __name__ == '__main__':
    # Display setup
    size = width, height = 320, 320
    screen = pygame.display.set_mode(size)

    view_distance = 1
    view = Viewport(fov = 360, pos = CVect(100, 50), dir = PVect(view_distance, math.radians(0)))

    csize = 32

    level = GameMap()
    #gamemap = [list(i) for i in level.level]
    redraw = 0
    pygame.key.set_repeat(30, 30)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                view.move(CVect(view.pos.x, view.pos.y - 5), level)
                redraw = 1
            if keys[pygame.K_s]:
                view.move(CVect(view.pos.x, view.pos.y + 5), level)
                redraw = 1
            if keys[pygame.K_a]:
                view.move(CVect(view.pos.x - 5, view.pos.y), level)
                redraw = 1
            if keys[pygame.K_d]:
                view.move(CVect(view.pos.x + 5, view.pos.y), level)
                redraw = 1
            if keys[pygame.K_LEFT]:
                view.dir.phi -= math.radians(5)
                redraw = 1
            if keys[pygame.K_RIGHT]:
                view.dir.phi += math.radians(5)
                redraw = 1
        if redraw:
            screen.fill((0, 0, 0))
            for i in range(width):
                    view.cast_ray(screen, PVect(1, view.dir.phi - math.radians(view.fov / 2) + (i * math.radians(view.fov) / width)), level)
                    redraw = 0
            pygame.display.flip()
        delay(32)











