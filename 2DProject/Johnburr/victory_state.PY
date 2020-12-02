import gfw
from pico2d import *
import main_state
import title_state
RES_DIR = './res'
def enter():
    global image, spaceship_image,engine_image, time, cw , ch,  scroll, speed,victory_image,quit_image,again_image, fidx
    image = load_image(RES_DIR + '/victory_state.png')
    spaceship_image = load_image(RES_DIR + '/spaceship/7.png')
    engine_image = load_image(RES_DIR + '/engine.png')
    victory_image = load_image(RES_DIR + '/victory.png')
    quit_image = load_image(RES_DIR + '/quit_button.png')
    again_image = load_image(RES_DIR + '/again_button.png')
    time = 0
    cw , ch = get_canvas_width(), get_canvas_height()
    scroll = 0
    fidx = 0
    speed = 500

    global bg_music
    bg_music = load_music('res/victory_state_sound.mp3')
    bg_music.set_volume(60)
    bg_music.repeat_play()


def update():
    global fidx, time, scroll
    time += gfw.delta_time
    fidx = int(time * 30 + 0.5) % 4
    scroll += speed * gfw.delta_time



def draw():

    sx = fidx * 53
    #image.draw(get_canvas_width() // 2,get_canvas_height() // 2,get_canvas_width() ,get_canvas_height())


    left, bottom = 0, 0
    page = image.h * cw // image.w
    curr = int(-scroll) % page
    if curr > 0:
        sh = int(1 + image.w * curr / cw)
        sb = image.h - sh
        src = 0, sb, image.w, sh
        dh = int(sh * cw / image.w)
        dst = 0, curr - dh, cw, dh
        image.clip_draw_to_origin(*src, *dst)
    dst_high = round(image.h * cw / image.w)
    while curr + dst_high < ch:
        dst = 0, curr, cw, dst_high
        image.draw_to_origin(*dst)
        curr += dst_high
    if curr < ch:
        dh = ch - curr
        sh = int(1 + image.w * dh / cw)
        src = 0, 0, image.w, sh
        dh = int(sh * cw / image.w)
        dst = 0, curr, cw, dh
        image.clip_draw_to_origin(*src, *dst)

    victory_image.draw(get_canvas_width() // 2,750)
    quit_image.draw(100,100)
    again_image.draw(1600, 100)
    spaceship_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    engine_image.clip_draw(0 + sx, 0, 45, 215, get_canvas_width() // 2, get_canvas_height() // 2 - 210)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    if handle_mouse(e):
        return


def handle_mouse(e):
    global mx , my
    if e.type == SDL_MOUSEMOTION:
        mx = e.x
        my = get_canvas_height() - 1 - e.y


    if e.type == SDL_MOUSEBUTTONDOWN:
        if mx > 60 and mx < 140 and my>50 and my<150:
            gfw.push(title_state)
        if mx > 1560 and mx < 1640 and my>40 and my<160:
            gfw.push(main_state)

def exit():
    global image, bg_music
    del image
    del bg_music


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
