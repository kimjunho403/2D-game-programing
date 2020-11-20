from pico2d import *
import gfw
from player import Player
import spaceship
import bg

def enter():
    global player
    gfw.world.init(['bg','spaceship','bullet','player'])
    player = Player()
    bg.init(player)
    spaceship.init()
    gfw.world.add(gfw.layer.bg,bg)
    gfw.world.add(gfw.layer.spaceship, spaceship)
    gfw.world.add(gfw.layer.player,player)

def exit():
    pass
def update():
    gfw.world.update()


def draw():
    gfw.world.draw()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)


if  __name__ == '__main__':
    gfw.run_main()
