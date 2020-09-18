Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> pos = turtle.pos()
>>> pos
(0.00,0.00)
>>> pos[0]
0.0
>>> pos[1]
0.0
>>> x,y =pos
>>> y
0.0
>>> pos =123,45
>>> pos[1]
45
>>> x,y = pos
>>> x
123
>>> y
45
>>> pos
(123, 45)
>>> turtle.goto(*pos)
>>> x,y = y,x
>>> x,y
(45, 123)
>>> for i in range(10):
      print(i)

      
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1,10):

	print(i)

	
1
2
3
4
5
6
7
8
9
>>> n=10
>>> for i in range(1,n+1)
SyntaxError: invalid syntax
>>> for i in range(1,n+1)
SyntaxError: invalid syntax
>>> for i in range(1,n+1):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> for x,y,z in [(200,200,50),(-200,-200,30),(100,100,50)]:
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.circle(r)
	turtle.write((x,y))

	
Traceback (most recent call last):
  File "<pyshell#36>", line 5, in <module>
    turtle.circle(r)
NameError: name 'r' is not defined
>>> for x,y,r in [(200,200,50),(-200,-200,30),(100,100,50)]:
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.circle(r)
	turtle.write((x,y))

	
>>> import random
>>> def drunken_move():
	turtle.setheading(random.randint(0, 360))
	turtle.forward(random.randint(100,200))
	turtle.stamp()

	
>>> turtle.shape('turtle')
>>> while(True):
	drunken_move()for x,y,r in [(200,200,50),(-200,-200,30),(100,100,50)]:
		turtle.penup()
		turtle.goto(x,y)
		turtle.pendown()
		turtle.circle(r)
		turtle.write((x,y))
		
SyntaxError: invalid syntax
>>> while(True):
	drunken_move()

	
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 3176, in _goto
    screen._drawline(self.drawingLineItem,
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 2761, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    drunken_move()
  File "<pyshell#44>", line 3, in drunken_move
    turtle.forward(random.randint(100,200))
  File "<string>", line 12, in forward
turtle.Terminator
>>> 
================ RESTART: C:/Users/N-Main/Desktop/draw_circle.py ===============
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 13, in <module>
    draw_circle(0,0,50)
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 4, in draw_circle
    for a,b,c in [x,y,z]:
NameError: name 'z' is not defined
>>> 
================ RESTART: C:/Users/N-Main/Desktop/draw_circle.py ===============
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 14, in <module>
    draw_circle(0,0,50)
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 4, in draw_circle
    for a,b,c in [x,y,z]:
NameError: name 'z' is not defined
>>> 
================ RESTART: C:/Users/N-Main/Desktop/draw_circle.py ===============
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 16, in <module>
    draw_circle(0,0,50)
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 4, in draw_circle
    for a,b,c in [x,y,z]:
NameError: name 'z' is not defined
>>> 
================ RESTART: C:/Users/N-Main/Desktop/draw_circle.py ===============
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 16, in <module>
    draw_circle(0,0,50)
  File "C:/Users/N-Main/Desktop/draw_circle.py", line 4, in draw_circle
    for a,b,c in [x,y,r]:
TypeError: cannot unpack non-iterable int object
>>> 
================ RESTART: C:/Users/N-Main/Desktop/draw_circle.py ===============
>>> 
=============== RESTART: C:/Users/N-Main/Desktop/drunken_move.py ===============
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 17, in <module>
    turtle.onkey(retsart, 'Escape')
NameError: name 'retsart' is not defined
>>> 
=============== RESTART: C:/Users/N-Main/Desktop/drunken_move.py ===============
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\tkinter\__init__.py", line 1883, in __call__
    return self.func(*args)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 686, in eventfun
    fun()
  File "C:/Users/N-Main/Desktop/drunken_move.py", line 6, in drunken_move
    turtle.forward(random.randint(50,00))
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 248, in randint
    return self.randrange(a, b+1)
  File "C:\Users\N-Main\AppData\Local\Programs\Python\Python38\lib\random.py", line 226, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (50, 1, -49)

=============== RESTART: C:/Users/N-Main/Desktop/drunken_move.py ===============
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 25, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 8, in tree
    t.forward(length)
NameError: name 'length' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 25, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 8, in tree
    t.forward(Lenght)
NameError: name 'Lenght' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 25, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 9, in tree
    if length > MIN_LEGTH:
NameError: name 'length' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 25, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 9, in tree
    if length > MIN_LEGTH:
NameError: name 'length' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 25, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 9, in tree
    if Length > MIN_LEGTH:
NameError: name 'MIN_LEGTH' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 26, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 15, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 15, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 15, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    t.left(ANGLE)
  File "<string>", line 5, in left
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 27, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  [Previous line repeated 2 more times]
  File "C:/Users/N-Main/Desktop/tree.py", line 15, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 9, in tree
    t.forward(Length)
  File "<string>", line 5, in forward
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 27, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 13, in tree
    tree(sub)
  [Previous line repeated 2 more times]
  File "C:/Users/N-Main/Desktop/tree.py", line 15, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 12, in tree
    t.left(ANGLE)
  File "<string>", line 5, in left
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 25, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  [Previous line repeated 1 more time]
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 10, in tree
    t.forward(Length)
  File "<string>", line 5, in forward
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 26, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  [Previous line repeated 1 more time]
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 10, in tree
    t.forward(Length)
  File "<string>", line 5, in forward
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 26, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  [Previous line repeated 1 more time]
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 17, in tree
    t.left(ANGLE)
  File "<string>", line 5, in left
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 28, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  [Previous line repeated 2 more times]
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 9, in tree
    t.width(Length * WIDTH_RATE)
  File "<string>", line 5, in width
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 28, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 16, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 14, in tree
    tree(sub)
  [Previous line repeated 1 more time]
  File "C:/Users/N-Main/Desktop/tree.py", line 15, in tree
    t.right(2*ANGLE)
  File "<string>", line 5, in right
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 32, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 11, in tree
    rate = random.uniform(RAMDOM_RATE_MIN, RAMDOM_RATE_MAN)
NameError: name 'random' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 32, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 11, in tree
    rate = random.uniform(RAMDOM_RATE_MIN, RAMDOM_RATE_MAX)
NameError: name 'random' is not defined
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 32, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 18, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 18, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 18, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 20, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 20, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 20, in tree
    tree(sub)
  [Previous line repeated 1 more time]
  File "C:/Users/N-Main/Desktop/tree.py", line 18, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 18, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 21, in tree
    t.left(ANGLE)
  File "<string>", line 5, in left
turtle.Terminator
>>> 
=================== RESTART: C:/Users/N-Main/Desktop/tree.py ===================
Traceback (most recent call last):
  File "C:/Users/N-Main/Desktop/tree.py", line 46, in <module>
    tree(120)
  File "C:/Users/N-Main/Desktop/tree.py", line 32, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 32, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 32, in tree
    tree(sub)
  [Previous line repeated 2 more times]
  File "C:/Users/N-Main/Desktop/tree.py", line 34, in tree
    tree(sub)
  File "C:/Users/N-Main/Desktop/tree.py", line 31, in tree
    t.left(ANGLE)
  File "<string>", line 5, in left
turtle.Terminator
>>> 