from pico2d import *
import gfw
RES_DIR = './res'
class Timer:
    def __init__(self):
        self.x = get_canvas_width() // 2
        self.y = 800
        self.time =300
        self.minute = self.time//60
        self.second = self.time %60
        self.image = load_image(RES_DIR + '/timerfiles/cut.png')
        self.second_image = load_image(RES_DIR + '/timerfiles/0.png')
        self.second_10_image = load_image(RES_DIR + '/timerfiles/0.png')
        self.minute_image = load_image(RES_DIR + '/timerfiles/5.png')

    def draw(self):
        self.second_image.draw(self.x+100, self.y)
        self.second_10_image.draw(self.x+50, self.y)
        self.minute_image.draw(self.x-50, self.y)
        self.image.draw(self.x, self.y)


    def update(self):
        pass
