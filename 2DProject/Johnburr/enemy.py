import random
from pico2d import *
import gfw
import gobj

class Enemy:
    POSITIONS = [( 1680// 2, 140)]
    ACTIONS = ['Attack','Dead','Idle','Walk']
    images = {}
    FPS = 12
    def __init__(self):
        if len(Enemy.images) == 0:
            Enemy.load_all_images()

        self.pos = (random.choice([-10, get_canvas_width()+10]), 140)
        self.delta = 0.1, 0.1
        self.find_nearest_pos()
        char = random.choice(['green', 'gray', 'red', 'blue', 'armor'])
        self.images = Enemy.load_images(char)
        self.action = 'Walk'
        self.speed = 200
        self.fidx = 0
        self.time = 0

    def find_nearest_pos(self):
        x, y = self.pos
        nearest_dsq = 1000000000
        index = 0
        nearest_index = 0
        for (px, py) in Enemy.POSITIONS:
            dsq = (x-px)**2 + (y-py)**2
            if nearest_dsq > dsq:
                nearest_dsq = dsq
                nearest_index = index
            index += 1
        self.patrol_order = nearest_index
        self.set_patrol_target()

    def set_patrol_target(self):
        self.set_target(Enemy.POSITIONS[self.patrol_order])
        self.patrol_order = (self.patrol_order + 1) % len(Enemy.POSITIONS)

    def set_target(self, target):
        x,y = self.pos
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance

    @staticmethod
    def load_all_images():
        Enemy.load_images('armor')
        Enemy.load_images('blue')
        Enemy.load_images('green')
        Enemy.load_images('red')
        Enemy.load_images('gray')

    @staticmethod
    def load_images(char):
        if char in Enemy.images:
            return Enemy.images[char]

        images = {}
        count = 0
        file_fmt = '%s/alienfiles/%s/%s (%d).png'
        for action in Enemy.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Enemy.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Enemy.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        done = False
        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True
        self.pos = x,y
        if done:
            self.set_patrol_target()

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, 60, 120)

