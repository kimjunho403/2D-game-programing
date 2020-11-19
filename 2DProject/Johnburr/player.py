from pico2d import *
import gfw
RES_DIR = './res'

class Player:
    def __init__(self):
        self.x = get_canvas_width() // 2
        self.y = 110
        self.dx, self.dy = 0, 0
        self.fidx = 0
        self.image = load_image(RES_DIR + '/player.png')
        self.action = 0
        self.dir = 0
        self.gravity = 3.0
        self.time =0

    def draw(self):
        sx = self.fidx * 53
        sy = self.action * 60
        self.image.clip_draw(145 + sx, 430 + -sy, 30, 60, self.x, self.y, 40, 80)

    def update(self):
        self.time += gfw.delta_time
        self.x += self.dx
        self.y += self.dy - self.gravity
        if self.y < 100:
            self.y += self.gravity
        if self.dx != 0:
            self.fidx = int(self.time*10 + 0.5) % 8
        elif self.dx == 0:
            if self.dir == 0:
                self.fidx = 1
            elif self.dir == 1:
                self.fidx = 0

    def handle_event(self, e):
        prev_dx = self.dx
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 3
            elif e.key == SDLK_RIGHT:
                self.dx += 3
            elif e.key == SDLK_DOWN:
                self.dy -= 3
            elif e.key == SDLK_UP:
                self.dy += 7
           # elif e.key == SDLK_SPACE:
            #    self.fire()
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 3
            elif e.key == SDLK_RIGHT:
                self.dx -= 3
            elif e.key == SDLK_DOWN:
                self.dy += 3
            elif e.key == SDLK_UP:
                self.dy -= 7

        if prev_dx != self.dx:
            if self.dx < 0:
                self.action = 2
            elif self.dx > 0:
                self.action = 1
            elif prev_dx < 0:
                self.action = 0
                self.dir = 0
            elif prev_dx > 0:
                self.action = 0
                self.dir = 1
