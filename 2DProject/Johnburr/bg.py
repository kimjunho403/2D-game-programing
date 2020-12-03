from pico2d import *
import gfw
import gobj
RES_DIR = './res'

def init(p):
    global space,floor,player
    space = gfw.image.load(gobj.res('bg.png'))
    floor = gfw.image.load(gobj.res('floor.png'))
    player = p
def draw():
    x,y = get_canvas_width() //2,get_canvas_height() //2
    px,py = player.x, player.y
    dx, dy = x-px,y -py
    space.draw(x+ dx * 0.02, y+dy *0.02)
    floor.draw(840,45,1690,90)

def update():
    pass