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
import victory_state
import defeat_state

def enter():
    global player, spaceship, timer, count
    gfw.world.init(['bg','spaceship','enemy_bullet','enemy','flying_enemy','bullet','player','timer'])
    player = Player()
    timer = Timer()
    bg.init(player)
    spaceship = Spaceship()
    gfw.world.add(gfw.layer.bg,bg)
    gfw.world.add(gfw.layer.spaceship, spaceship)
    gfw.world.add(gfw.layer.player, player)
    gfw.world.add(gfw.layer.timer, timer)
    count = 0

    Enemy.load_all_images()
    Flying_Enemy.load_all_images()

    global bg_music, flip_wav, enemy_die_wav, spaceship_wav
    bg_music = load_music('./res/main_state_sound.mp3')
    bg_music.set_volume(60)
    bg_music.repeat_play()
    flip_wav = load_wav('./res/beshot.wav')
    enemy_die_wav = load_wav('./res/enemy_die.wav')
    spaceship_wav = load_wav('./res/spaceship_die.wav')
    flip_wav.set_volume(100)
    enemy_die_wav.set_volume(200)





def check_enemy(e):
    dead = False
    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e) and not dead:
            dead = e.decrease_life(b.power)
            if dead:
                enemy_die_wav.play()
                e.action = 'Dead'
                e.do_dead()
            b.remove()
            return

def check_spaceship():
        if gobj.collides_box(spaceship, player):
            player.boarding()
            spaceship.is_boarding = 1
        if spaceship.y > 900:
            gfw.push(victory_state)


def check_enemy_bullet(eb):
        spaceship_dead = False
        if gobj.collides_box(eb, player):
            player_dead = player.decrease_life(eb.power)
            flip_wav.play()
            if player_dead:
                gfw.push(defeat_state)
            eb.remove()
            return
        if gobj.collides_box(eb, spaceship):
            spaceship_dead = spaceship.decrease_life(eb.power)
            eb.remove()
        if spaceship_dead:
            global count
            if count == 0:
                spaceship_wav.play()
            count += gfw.delta_time
            spaceship.remove()
            if count > 0.5:
                gfw.push(defeat_state)
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

def pause():
    enemy_gen.num = 1
    enemy_gen.num_time = 0
    enemy_gen.next_wave = 0
    enemy_gen.swh =0
    enemy_gen.GEN_X = [ -30,1710 ]
    Enemy.choice_num = 1

def resume():
    pass

def exit():
    global bg_music
    bg_music.stop()
    del bg_music


if  __name__ == '__main__':
    gfw.run_main()
