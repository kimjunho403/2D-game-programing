Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pico2d
Pico2d is prepared.
>>> pico2d.open_canvas()
>>> pico2d.hide_lattice()
>>> pico2d.show_lattice()
>>> pico2d.close_canvas()
>>> import pico2d as p
>>> p.open_canvas()
>>> p.close_canvas()
>>> random.randint(1,6)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    random.randint(1,6)
NameError: name 'random' is not defined
>>> from random import randint
>>>  randint(1,6)
 
SyntaxError: unexpected indent
>>> randint(1,6)
1
>>> from random import uniform as rndf
>>> rndf(0.1,0.5)
0.3743776797928232
>>> r = rndf
>>> r(0.1,0.5)
0.31810351541498294
>>> from random import *
>>> randrange(10,20)
19
>>> uniform(10,20)
11.257372875477765
>>> random()
0.48767325926718996
>>> from pico2d import *
>>> import os
>>> os.getcwd()
'C:\\Users\\N-Main\\AppData\\Local\\Programs\\Python\\Python38'
>>> open_canvas()
>>> load_image('grass.png')
cannot load grass.png
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    load_image('grass.png')
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> ch =load_image('character.png')
cannot load character.png
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ch =load_image('character.png')
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> os.chdir('C:/Users/N-Main/project/classfile/0914')
>>> ch =load_image('character.png')
>>> ch.draw_now(200,400)
>>> for y in range(100,501,100):
	for x in range(100,701,100):
		ch.draw_now(x,y)

		
>>> for y in range(100,501,100):
	for x in range(100,701,100):
		ch.draw_now(x,y)

		
>>> for s in range(100,300):
	clear_canvas_now()
	for y in range(100, 501, 100):
		for x in range(s,800,100):
			ch.draw_now(x,y)

			
>>> close_canvas()
>>> 