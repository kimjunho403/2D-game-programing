from pico2d import *
import gfw
from timer import Timer
RES_DIR = './res'
class Spaceship:
    def __init__(self):
        global char
        self.image = load_image(RES_DIR + '/spaceship/0.png')
        self.hp_image = load_image(RES_DIR + '/space_ship_hp.png')
        self.life = 300
        self.x = get_canvas_width() // 2
        self.y = 200
        self.time = 0
        self.end_time = 0
        self.n =0
        self.pos =self.x, self.y
        self.is_boarding =0
        char = '/spaceship/%d.png'


    def draw(self):
        self.image.draw(self.x, self.y)
        for n in range(self.life//5):
            self.hp_image.draw(self.x + 70, self.y+n*5-120)


    def update(self):
         self.time += gfw.delta_time

         if self.time >=5 and self.is_boarding==1:
             self.end_time = 1
         if self.end_time == 1 and self.n !=7:
            self.n += 1
            fn = char % (self.n)
            self.image = load_image(RES_DIR + fn)
         if self.end_time == 1:
             self.y += 3



    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh-60

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def remove(self):
        gfw.world.remove(self)