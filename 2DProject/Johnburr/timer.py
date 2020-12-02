from pico2d import *
import gfw
RES_DIR = './res'
class Timer:
    def __init__(self):
        global char
        self.x = get_canvas_width() // 2
        self.y = 800
        self.time = 180
        self.s_time = 0
        self.minute = self.time//60
        self.second = self.time %60
        self.image = load_image(RES_DIR + '/timerfiles/cut.png')
        self.second_image = load_image(RES_DIR + '/timerfiles/0.png')
        self.second_10_image = load_image(RES_DIR + '/timerfiles/0.png')
        self.minute_image = load_image(RES_DIR + '/timerfiles/5.png')
        char = '/timerfiles/%d.png'

    def draw(self):
        self.second_image.draw(self.x+100, self.y)
        self.second_10_image.draw(self.x+50, self.y)
        self.minute_image.draw(self.x-50, self.y)
        self.image.draw(self.x, self.y)


    def update(self):
        self.s_time += gfw.delta_time
        if self.s_time >1 and self.time!=0:
            self.time -= 1
            minute = self.time // 60
            second_10 = (self.time % 60)//10
            second_1 = (self.time % 60) % 10
            fn = char % (minute)
            self.minute_image = load_image(RES_DIR + fn)
            fn = char % (second_10)
            self.second_10_image = load_image(RES_DIR + fn)
            fn = char % (second_1)
            self.second_image = load_image(RES_DIR + fn)

            self.s_time =0



