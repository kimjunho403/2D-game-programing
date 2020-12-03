import random
import gfw
from pico2d import *
from enemy import Enemy
from flying_enemy import Flying_Enemy
global GEN_X
GEN_X = [ -30,1710 ]
next_wave = 0
wave_index = 0
num = 1
num_time = 0
difficulty = 0
swh = 0
def update():
    global next_wave, num_time, num, swh
    next_wave -= gfw.delta_time
    num_time += gfw.delta_time

    for n in range(0,5):
        if num_time > 20*n:
            num = n+1

    if num == 2 and swh == 0:
        swh += 1
        global GEN_X
        GEN_X += [-60]
    if num == 3 and swh == 1:
        swh += 1
        GEN_X += [1740]
    if num == 4 and swh == 2:
        swh += 1
        GEN_X += [-90]


    if next_wave < 0:
        generate_wave()


def generate_wave():
    global wave_index, next_wave, num, num_time, diffculty
    for x in GEN_X:
        level = enemy_level()
        speed = -(100 + 5 * wave_index)
        e = Enemy(num, x)


        gfw.world.add(gfw.layer.enemy, e)

    fe = Flying_Enemy(-30)
    gfw.world.add(gfw.layer.flying_enemy, fe)
    fe = Flying_Enemy(1710)
    gfw.world.add(gfw.layer.flying_enemy, fe)

    wave_index += 1
    if difficulty == 0:
        next_wave = random.uniform(6, 8)
    elif difficulty == 1:
        next_wave = random.uniform(5, 7)
    elif difficulty == 2:
        next_wave = random.uniform(4, 6)

LEVEL_ADJUST_PERCENTS = [ 10, 15, 15, 40, 15, 5 ] # -3 ~ 2



def enemy_level():
    level = (wave_index - 5) // 10 - 3;
    percent = random.randrange(100)
    pl = level
    pp = percent
    for p in LEVEL_ADJUST_PERCENTS:
        if percent < p:
            break
        percent -= p
        level += 1
    #print(pl, '->', level, ', ', pp, '->', percent)
    if level < 1: level = 1
    if level > 20: level = 20
    return level

