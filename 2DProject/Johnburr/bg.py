from pico2d import *
import gfw
RES_DIR = './res'

def init(p):
    global space,floor,player
    space = gfw.image.load(RES_DIR +'/bg.png')
    floor = gfw.image.load(RES_DIR +'/floor.png')
    player = p
def draw():
    x,y = get_canvas_width() //2,get_canvas_height() //2
    px,py = player.x, player.y
    dx, dy = x-px,y -py
    space.draw(x+ dx * 0.02, y+dy *0.02)
    floor.draw(730,45,1460,90)

def update():
    pass