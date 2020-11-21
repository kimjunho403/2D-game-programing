from pico2d import *
import gfw
import gobj
RES_DIR = './res'

class Bullet:
    SIZE = 10
    def __init__(self, x, y, dir,speed):
        self.pos = x, y
        self.dx = speed
        self.dir =dir
        self.image = load_image(RES_DIR + '/bullet.png')
        self.power = 30
        self.x, self.y = self.pos

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.dir == 1:
            self.x += self.dx * gfw.delta_time
        elif self.dir == 0:
            self.x -= self.dx * gfw.delta_time

        if self.x > get_canvas_width() + Bullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x -hw, self.y -hh, self.x +hw, self.y +hh