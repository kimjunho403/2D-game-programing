import gfw
from pico2d import *
import main_state
import enemy_gen
RES_DIR = './res'
def enter():
    global image, exit_image, exit_2_image, start_image, start_2_image, easy_1_image ,easy_2_image, hard_1_image,hard_2_image,normal_1_image,normal_2_image
    image = load_image(RES_DIR + '/title.png')
    exit_image = load_image(RES_DIR + '/exit.png')
    exit_2_image = load_image(RES_DIR + '/exit2.png')
    start_image = load_image(RES_DIR + '/start.png')
    start_2_image = load_image(RES_DIR + '/start2.png')
    easy_1_image = load_image(RES_DIR + '/easy_1.png')
    easy_2_image = load_image(RES_DIR + '/easy_2.png')
    hard_1_image = load_image(RES_DIR + '/hard_1.png')
    hard_2_image = load_image(RES_DIR + '/hard_2.png')
    normal_1_image = load_image(RES_DIR + '/normal_1.png')
    normal_2_image = load_image(RES_DIR + '/normal_2.png')




    global bg_music, flip_wav
    bg_music = load_music('./res/title_state_sound.mp3')
    flip_wav = load_wav('./res/botton.wav')
    bg_music.set_volume(60)
    bg_music.repeat_play()

    global press_1, press_2, menu_press,select_1 ,select_2 ,select_3
    press_1 = False
    press_2 = False
    menu_press = False
    select_1 = False
    select_2 = False
    select_3 = False



def update():
    pass


def draw():
    image.draw(get_canvas_width() // 2,get_canvas_height() // 2,get_canvas_width() ,get_canvas_height())
    if menu_press == False:
        if press_1 == False:
            start_image.draw(get_canvas_width() // 2, 300)
        elif press_1 == True:
            start_2_image.draw(get_canvas_width() // 2, 300)
        if press_2 == False:
            exit_image.draw(get_canvas_width() // 2, 200)
        elif press_2 == True:
            exit_2_image.draw(get_canvas_width() // 2, 200)
    elif menu_press == True:
        if select_1 == False:
            easy_1_image.draw(get_canvas_width() // 2, 400)
        elif select_1 == True:
            easy_2_image.draw(get_canvas_width() // 2, 400)
        if select_2 == False:
            normal_1_image.draw(get_canvas_width() // 2, 300)
        elif select_2 == True:
            normal_2_image.draw(get_canvas_width() // 2, 300)
        if select_3 == False:
            hard_1_image.draw(get_canvas_width() // 2, 200)
        elif select_3 == True:
            hard_2_image.draw(get_canvas_width() // 2, 200)



def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

    if handle_mouse(e):
        return


def handle_mouse(e):
    global press_1, press_2, select_3, select_2, select_1, menu_press
    if e.type == SDL_MOUSEMOTION:
        mx = e.x
        my = get_canvas_height() - 1 - e.y
        if menu_press == False:
            if mx > get_canvas_width() // 2 - 193 and mx < get_canvas_width() // 2 + 193 and my > 250 and my < 350:
                if press_1 == False:
                    flip_wav.play()
                press_1 = True
            else:
                press_1 = False
            if mx > get_canvas_width() // 2 - 193 and mx < get_canvas_width() // 2 + 193 and my > 150 and my < 250:
                if press_2 == False:
                    flip_wav.play()
                press_2 = True
            else:
                press_2 = False
        elif menu_press == True:
            if mx > get_canvas_width() // 2 - 110 and mx < get_canvas_width() // 2 + 110 and my > 350 and my < 450:
                if select_1 == False:
                    flip_wav.play()
                select_1 = True
            else:
                select_1 = False
            if mx > get_canvas_width() // 2 - 110 and mx < get_canvas_width() // 2 + 110 and my > 250 and my < 350:
                if select_2 == False:
                    flip_wav.play()
                select_2 = True
            else:
                select_2 = False
            if mx > get_canvas_width() // 2 - 130 and mx < get_canvas_width() // 2 + 130 and my > 150 and my < 250:
                if select_3 == False:
                    flip_wav.play()
                select_3 = True
            else:
                select_3 = False



    if e.type == SDL_MOUSEBUTTONDOWN:
        if press_1 == True:
            menu_press = True

        if press_2 == True:
            gfw.quit()
        if select_1 == True:
            enemy_gen.difficulty = 0
            gfw.push(main_state)
        if select_2 == True:
            enemy_gen.difficulty = 1
            gfw.push(main_state)
        if select_3 == True:
            enemy_gen.difficulty = 2
            gfw.push(main_state)





def exit():
    global image, bg_music
    bg_music.stop()
    del bg_music
    del image


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
