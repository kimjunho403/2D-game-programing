import random
from pico2d import *

RES_DIR = '../res'


class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/floor.png')

    def draw(self):
        self.image.draw(730, 45, 1460, 90)

    def update(self):
        pass


class Back_ground:
    def __init__(self):
        self.image = load_image(RES_DIR + '/back_ground.png')

    def draw(self):
        self.image.draw(730, 400, 1460, 800)

    def update(self):
        pass


class Ball:
    balls = []

    def __init__(self, x, y, dx, dy):
        self.image = load_image(RES_DIR + '/ball21x21.png')
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.dx
        self.y += self.dy


class Boy:
    # constructor
    # def __init__(self, pos, delta):
    # 	self.x, self.y = pos
    # 	self.dx, self.dy = delta
    def __init__(self):
        self.x = get_canvas_width() // 2
        self.y = 110
        self.dx, self.dy = 0, 0
        self.fidx = 0
        self.image = load_image(RES_DIR + '/player.png')
        self.action = 0
        self.dir = 0
        self.gravity = 1.0

    def draw(self):
        sx = self.fidx * 53
        sy = self.action * 60
        self.image.clip_draw(150 + sx, 428 + -sy, 30, 60, self.x, self.y, 40, 80)

    def update(self):
        # if self.dx < 0:
        # 	self.action = 0
        # elif self.dx > 0:
        # 	self.action = 1
        # else:
        # 	self.action = 3

        self.x += self.dx
        self.y += self.dy - self.gravity
        if self.y < 100:
            self.y += self.gravity
        if self.dx != 0:
            self.fidx = (self.fidx + 1) % 8
        elif self.dx == 0:
            if self.dir == 0:
                self.fidx = 1
            elif self.dir == 1:
                self.fidx = 0

    def fire(self):
        ball = Ball(self.x, self.y, self.dx, self.dy)
        Ball.balls.append(ball)
        print('Ball count = %d' % len(Ball.balls))

    def handle_event(self, e):
        prev_dx = self.dx
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 2
            elif e.key == SDLK_RIGHT:
                self.dx += 2
            elif e.key == SDLK_DOWN:
                self.dy -= 1
            elif e.key == SDLK_UP:
                self.dy += 3
            elif e.key == SDLK_SPACE:
                self.fire()
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 2
            elif e.key == SDLK_RIGHT:
                self.dx -= 2
            elif e.key == SDLK_DOWN:
                self.dy += 1
            elif e.key == SDLK_UP:
                self.dy -= 3

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


if __name__ == "__main__":
    print("Running test code ^_^")
