import gfw
from pico2d import *
import main_state
import title_state

RES_DIR = './res'
def enter():
    global image, e1_image,e2_image,e3_image,e4_image, e5_image,char_1,char_2,char_3,char_4,char_5, fidx,f
    image = load_image(RES_DIR + '/defeat_state.png')
    char_1 = '/alienfiles/armor/Idle (%d).png'
    char_2= '/alienfiles/blue/Idle (%d).png'
    char_3 = '/alienfiles/gray/Idle (%d).png'
    char_4 = '/alienfiles/predator/Idle (%d).png'
    char_5 = '/alienfiles/red/Idle (%d).png'
    fidx = 0
    f =0
    e1_image = load_image(RES_DIR + '/alienfiles/armor/Idle (1).png')
    e2_image = load_image(RES_DIR + '/alienfiles/blue/Idle (1).png')
    e3_image = load_image(RES_DIR + '/alienfiles/gray/Idle (1).png')
    e4_image = load_image(RES_DIR + '/alienfiles/predator/Idle (1).png')
    e5_image = load_image(RES_DIR + '/alienfiles/red/Idle (1).png')

    global bg_music
    bg_music = load_music('res/defeat_state_sound.mp3')
    bg_music.set_volume(60)
    bg_music.repeat_play()


def update():
    pass





def draw():
    global f
    f += gfw.delta_time
    fidx = int(f * 10 + 0.5) % 3+1
    fn = char_1 % (fidx)
    fn_2 = char_2 % (fidx)
    fn_3 = char_3 % (fidx)
    fn_4 = char_4 % (fidx)
    fn_5 = char_5 % (fidx)
    e1_image = load_image(RES_DIR + fn)
    e2_image = load_image(RES_DIR + fn_2)
    e3_image = load_image(RES_DIR + fn_3)
    e4_image = load_image(RES_DIR + fn_4)
    e5_image = load_image(RES_DIR + fn_5)
    image.draw(get_canvas_width() // 2,get_canvas_height() // 2,get_canvas_width() ,get_canvas_height())
    e1_image.draw(get_canvas_width() // 2+300, 300+100,60, 120)
    e2_image.draw(get_canvas_width() // 2+150, 300+50, 60, 120)
    e3_image.draw(get_canvas_width() // 2-150, 300+50, 60, 120)
    e4_image.draw(get_canvas_width() // 2, 300, 60, 120)
    e5_image.draw(get_canvas_width() // 2-300, 300+100, 60, 120)


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
        if mx > 20 and mx < 210 and my>30 and my<230:
            gfw.push(title_state)
        if mx > 1460 and mx < 1650 and my>30 and my<230:
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
