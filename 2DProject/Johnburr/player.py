from pico2d import *
import gfw
from bullet import *
RES_DIR = './res'

class Player:
    SPARK_OFFSET = 5
    def __init__(self):
        self.pos = get_canvas_width() // 2,110
        self.x, self.y = self.pos
        self.dx, self.dy = 0, 0
        self.hh, self.hw =0, 0
        self.fidx = 0
        self.image = load_image(RES_DIR + '/player.png')
        self.action = 0
        self.dir = 0
        self.speed =100
        self.gravity = 3.0
        self.time =0
        self.life =50
        self.sit =0
    def fire(self):
        bullet = Bullet(self.x, self.y + Player.SPARK_OFFSET, self.dir, 700)
        if self.sit == 1:
            bullet = Bullet(self.x, self.y-8, self.dir, 700)
        gfw.world.add(gfw.layer.bullet, bullet)

    def draw(self):
        sx = self.fidx * 53
        sy = self.action * 60
        self.image.clip_draw(140 + sx, 430  -sy, 40, 60, self.x, self.y, 50, 80)


    def update(self):

        self.time += gfw.delta_time
        self.x += self.dx * self.speed * gfw.delta_time
        self.y += self.dy * self.speed * gfw.delta_time- self.gravity
        self.hw, self.hh = 0, 110
        self.x = clamp(self.hw, self.x, get_canvas_width() - self.hw)
        self.y = clamp(self.hh, self.y, get_canvas_height() - 30)
        if self.y < 110:
            self.y += self.gravity
        if self.dx != 0: #움직일때
            if self.y ==110:
                if self.dir == 1:
                    self.action = 1
                    self.fidx = int(self.time * 10 + 0.5) % 8
                elif self.dir == 0:
                    self.action = 2
                    self.fidx = int(self.time * 10 + 0.5) % 8
            elif self.y != 110:
                if self.dir == 0:
                    self.fidx = 5
                    self.action = 0
                elif self.dir == 1:
                    self.fidx = 4
                    self.action = 0
        elif self.dx == 0: #가만히 있을때
            if self.y == 110:
                if self.dir == 0:
                    self.action = 0
                    self.fidx = 1
                    if self.sit == 1:
                        self.fidx = 3
                        self.action = 0

                elif self.dir == 1:
                    self.action = 0
                    self.fidx = 0
                    if self.sit == 1:
                        self.fidx = 2
                        self.action = 0

            elif self.y !=110:
                if self.dir == 0:
                    self.fidx = 5
                    self.action = 0
                elif self.dir == 1:
                    self.fidx = 4
                    self.action = 0
        self.pos = self.x,self.y


    def handle_event(self, e):
        prev_dx = self.dx
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 3
                self.dir = 0
            elif e.key == SDLK_RIGHT:
                self.dir = 1
                self.dx += 3
            elif e.key == SDLK_DOWN:
                self.dy -= 3
                self.sit = 1
            elif e.key == SDLK_UP:
                self.dy += 7
            if e.key == SDLK_SPACE:
                self.fire()
           # elif e.key == SDLK_SPACE:
            #    self.fire()
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 3
            elif e.key == SDLK_RIGHT:
                self.dx -= 3
            elif e.key == SDLK_DOWN:
                self.dy += 3
                self.sit = 0
            elif e.key == SDLK_UP:
                self.dy -= 7


    def get_bb(self):
        hw = 20
        hh = 30
        x,y = self.x ,self.y
        return x - hw, y - hh, x + hw, y + hh

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0


