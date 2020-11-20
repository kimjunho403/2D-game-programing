from pico2d import *
import gfw
from player import Player
from enemy import Enemy
import gobj
import spaceship
import bg

def enter():
    global player
    gfw.world.init(['bg','spaceship','enemy','bullet','player'])
    player = Player()
    bg.init(player)
    spaceship.init()
    gfw.world.add(gfw.layer.bg,bg)
    gfw.world.add(gfw.layer.spaceship, spaceship)
    gfw.world.add(gfw.layer.player, player)

    global enemy_time
    enemy_time = 1

    Enemy.load_all_images()



def update():
    gfw.world.update()


    global enemy_time
    enemy_time -= gfw.delta_time
    if enemy_time <= 0:
        gfw.world.add(gfw.layer.enemy, Enemy())
        enemy_time = 5


def draw():
    gfw.world.draw()

    gobj.draw_collision_box()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if  __name__ == '__main__':
    gfw.run_main()
