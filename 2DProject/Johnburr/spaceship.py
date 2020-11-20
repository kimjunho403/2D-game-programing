from pico2d import *
import gfw
RES_DIR = './res'
def init():
    global spaceship
    spaceship = gfw.image.load(RES_DIR +'/spaceship.png')
def draw():
    x = get_canvas_width() //2
    spaceship.draw(x, 200,180,252)
def update():
    pass