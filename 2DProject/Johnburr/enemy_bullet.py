from pico2d import *
import gfw
import gobj
RES_DIR = './res'

class Enemy_Bullet:
    SIZE = 10
    def __init__(self, x, y, dir,speed):
        self.x, self.y = x, y
        self.dx = speed
        self.speed = speed
        self.dir =dir
        self.image = load_image(RES_DIR + '/enemy_bullet.png')
        self.power = 1
        self.time =0
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
        self.tx, self.ty = self.player.pos

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        #if self.dir == 1:
        #        self.x += self.dx * gfw.delta_time
        #elif self.dir == 0:
        #        self.x -= self.dx * gfw.delta_time
        self.move_to_player()

        if self.x > get_canvas_width() + Enemy_Bullet.SIZE:
            self.remove()




    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * 12)
        dx,dy = self.delta
        self.x += dx * self.speed * gfw.delta_time
        self.y += dy * self.speed * gfw.delta_time

    def set_target(self):
        dx, dy = self.tx - self.x, self.ty - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0:
            return
        self.delta = dx / distance, dy / distance

    def move_to_player(self):
        self.set_target()
        self.update_position()



    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x -hw, self.y -hh, self.x +hw, self.y +hh