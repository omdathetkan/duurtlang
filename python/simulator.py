from tkinter import *
import collections

class Led:
    def __init__(self, canvas, x, y, angle = 0) -> None:
        self._canvas = canvas
        self._x = x
        self._y = y
        self._a = angle
        self._r = 0
        self._g = 0
        self._b = 0

    def _from_rgb(self, r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def data_in(self, data):
        self._r = data.popleft()
        self._g = data.popleft()
        self._r = data.popleft()

    def render_children(self):
        pass

    def render(self):
        r = 3
        self._canvas.create_oval(self._x - r, self._y - r, self._x + r, self._y + r, outline="#000", fill=self._from_rgb(self._r, self._g, self._b), width=1)

class LedSegment(Led):
    def render(self):
        w = 5
        h = 17
        self._canvas.create_rectangle(self._x - w/2, self._y - h/2, self._x + w/2, self._y + h/2, outline="#000", fill=self._from_rgb(self._r, self._g, self._b), width=1)

class LedSideways(Led):
    def render(self):
        w = 5
        h = 17
        self._canvas.create_rectangle(self._x - w/2, self._y - h/2, self._x + w/2, self._y + h/2, outline="#000", fill=self._from_rgb(self._r, self._g, self._b), width=1)

class Tile(Led):
    def __init__(self, canvas, x, y) -> None:
        self._canvas = canvas

        self._leds = [
            LedSegment(10, 10),
            LedSegment(10, 10),
            LedSegment(10, 10),
            LedSegment(10, 10),
            LedSegment(10, 10),

            LedSideways(10, 20),
            LedSideways(10, 20),
            LedSideways(10, 20),
            LedSideways(10, 20),
        ]

    def data_in(self):
        
        pass

class Board(Led):
    def __init__(self, canvas) -> None:
        self._canvas = canvas

        self._tiles [
            Tile(100, 100),
            Tile(100, 100),
            Tile(100, 100),
            Tile(100, 100),
            Tile(100, 100),
            Tile(100, 100),
            Tile(100, 100),
        ]

    def data_in(self, bytes):
        pass
        

master = Tk()

canvas_width = 500
canvas_height = 500
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()


data = collections.deque([0, 255, 255, 0, 255, 255, 255, 0, 255])



led1 = Led(w, 50, 50)
led1.data_in(data)
led1.render()

led2 = LedSegment(w, 100, 50)
led2.data_in(data)
led2.render()

led2 = LedSegment(w, 100, 80)
led2.data_in(data)
led2.render()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")


mainloop()
