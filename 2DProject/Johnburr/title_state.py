import gfw
from pico2d import *
import main_state

RES_DIR = './res'
def enter():
    global image
    image = load_image(RES_DIR + '/title.png')


    global bg_music
    bg_music = load_music('res/title_state_sound.mp3')
    bg_music.set_volume(60)
    bg_music.repeat_play()


def update():
    pass


def draw():
    image.draw(get_canvas_width() // 2,get_canvas_height() // 2,get_canvas_width() ,get_canvas_height())


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)


def exit():
    global image
    del image


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
