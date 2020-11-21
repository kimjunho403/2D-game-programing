from pico2d import *
import gfw
from player import Player
from enemy import Enemy
import gobj
from spaceship import Spaceship
import bg
import enemy_gen

def enter():
    global player, spaceship
    gfw.world.init(['bg','spaceship','enemy_bullet','enemy','bullet','player'])
    player = Player()
    bg.init(player)
    spaceship = Spaceship()
    gfw.world.add(gfw.layer.bg,bg)
    gfw.world.add(gfw.layer.spaceship, spaceship)
    gfw.world.add(gfw.layer.player, player)

    Enemy.load_all_images()

def check_enemy(e):
    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            dead = e.decrease_life(b.power)
            if dead:

                e.action = 'Dead'
                e.do_dead()
            b.remove()
            return

def check_enemy_bullet(eb):
        if gobj.collides_box(eb, player):
            player.decrease_life(eb.power)
            eb.remove()
            return
        if gobj.collides_box(eb, spaceship):
            spaceship_dead = spaceship.decrease_life(eb.power)
            if spaceship_dead:
                spaceship.remove()
            eb.remove()
            return

def update():
    gfw.world.update()
    enemy_gen.update()

    for eb in gfw.world.objects_at(gfw.layer.enemy_bullet):
        check_enemy_bullet(eb)

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)


def draw():
    gfw.world.draw()

    #gobj.draw_collision_box()

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
