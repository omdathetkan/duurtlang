from tkinter import *
import collections
import math




class Point:
    """convenience for point arithmetic"""
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __iter__(self):
        yield self.x
        yield self.y

class RegularPolygon:
    def __init__(self, num_sides, bbox_side, x, y):   # x, y are bbox center canvas coordinates
        self.bbox_side = bbox_side
        self.num_sides = num_sides
        self.side_length = None
        self.apothem = None
        self._calc_side_length()
        self.points = [Point(x - self.side_length // 2, y - self.apothem)]
        self._make_points()
        self.lines = []
        self._make_lines()

    def _calc_side_length(self):
        """Side length given the radius (circumradius):
        i/e the distance from the center to a vertex
        """
        self.side_length = 2 * (self.bbox_side // 2) * math.sin(math.pi / self.num_sides)

        # Apothem, i/e distance from the center of the polygon 
        # to the midpoint of any side, given the side length 
        self.apothem = self.side_length / (2 * math.tan(math.pi / self.num_sides))

    def _make_points(self):
        _angle = 2 * math.pi / self.num_sides
        for pdx in range(self.num_sides):
            angle = _angle * pdx
            _x = math.cos(angle) * self.side_length
            _y = math.sin(angle) * self.side_length
            self.points.append(self.points[-1] + Point(_x, _y))

    def _make_lines(self):
        for p0, p1 in zip(self.points[:-1], self.points[1:]):
            self.lines.append((*p0, *p1))

    def draw(self, canvas):
        for line in self.lines:
            canvas.create_line(line)
        # alternatively, use canvas.create_polygon(points coordinates) instead





class AbstractLed:
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

class LedSegment(AbstractLed):
    def render(self):
        w = 5
        h = 17
        self._canvas.create_rectangle(self._x - w/2, self._y - h/2, self._x + w/2, self._y + h/2, outline="#000", fill=self._from_rgb(self._r, self._g, self._b), width=1)

class LedSideways(AbstractLed):
    def render(self):
        r = 3
        self._canvas.create_oval(self._x - r, self._y - r, self._x + r, self._y + r, outline="#000", fill=self._from_rgb(self._r, self._g, self._b), width=1)


class Tile(AbstractLed):
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

class Board(AbstractLed):
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

canvas_width = 1000
canvas_height = 1000
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()


data = collections.deque([0, 255, 255, 0, 255, 255, 255, 0, 255])




led1 = LedSideways(w, 200, 200)
led1.data_in(data)
led1.render()

led2 = LedSegment(w, 200, 250)
led2.data_in(data)
led2.render()

led2 = LedSegment(w, 200, 280)
led2.data_in(data)
led2.render()

CENTER = Point(250, 250)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

CENTER = Point(250+310, 250)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

CENTER = Point(250+310+310, 250)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

#--

CENTER = Point(250+155, 250 + 90)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

CENTER = Point(250+155+310, 250 + 90)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

#--

CENTER = Point(250, 250 + 90 + 90)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

CENTER = Point(250+310, 250 + 90 + 90)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)

CENTER = Point(250+310+310, 250 + 90 + 90)
p = RegularPolygon(6, 200, *CENTER)
p.draw(w)
mainloop()


