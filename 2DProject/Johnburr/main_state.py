from pico2d import *
import gfw
from player import Player
from enemy import Enemy
from flying_enemy import Flying_Enemy
from timer import Timer
import gobj
from spaceship import Spaceship
import bg
import enemy_gen

def enter():
    global player, spaceship, timer
    gfw.world.init(['bg','spaceship','enemy_bullet','enemy','flying_enemy','bullet','player','timer'])
    player = Player()
    timer = Timer()
    bg.init(player)
    spaceship = Spaceship()
    gfw.world.add(gfw.layer.bg,bg)
    gfw.world.add(gfw.layer.spaceship, spaceship)
    gfw.world.add(gfw.layer.player, player)
    gfw.world.add(gfw.layer.timer, timer)

    Enemy.load_all_images()
    Flying_Enemy.load_all_images()

def check_enemy(e):
    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            dead = e.decrease_life(b.power)
            if dead:

                e.action = 'Dead'
                e.do_dead()
            b.remove()
            return

def check_spaceship():
        if gobj.collides_box(spaceship, player):
            player.boarding()
            spaceship.is_boarding =1


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
    if timer.time == 0:
        check_spaceship()
    for eb in gfw.world.objects_at(gfw.layer.enemy_bullet):
        check_enemy_bullet(eb)
    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)
    for fe in gfw.world.objects_at(gfw.layer.flying_enemy):
        check_enemy(fe)


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
