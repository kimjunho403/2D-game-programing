from pico2d import *
import gfw
RES_DIR = './res'
class Spaceship:
    def __init__(self):
        self.image = load_image(RES_DIR + '/spaceship.png')
        self.hp_image = load_image(RES_DIR + '/space_ship_hp.png')
        self.life = 300
        self.x = get_canvas_width() // 2
        self.y = 200

    def draw(self):
        self.image.draw(self.x, self.y)
        for n in range(self.life//5):
            self.hp_image.draw(self.x + 70, self.y+n*5-120)

    def update(self):
        pass

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh-60

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def remove(self):
        gfw.world.remove(self)