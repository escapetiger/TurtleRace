"""
    自绘的素材库
    Author: Escape
    Version: 1.0
    Date: 2020/3/28
"""
import turtle


class Source(object):
    def __init__(self, name=''):
        """
        :param name: The name of the corresponding environment
        """
        self.name = name

    def logo(self, pos):
        """
        Draw the logo at the specific position. Here I simply draw a logo by rotating a polyline
        :param pos: position - tuple
        :return: None
        """
        turtle.color('white')
        turtle.setpos(pos)
        turtle.speed(10)
        turtle.tracer(False)
        for i in range(180):
            turtle.pendown()
            turtle.forward(100)
            turtle.right(30)
            turtle.forward(20)
            turtle.left(60)
            turtle.forward(50)
            turtle.right(30)

            turtle.penup()
            turtle.setposition(0, 0)
            turtle.pendown()

            turtle.right(2)

        turtle.penup()
        return None

    def line(self, start, end, ltype='straight', color='white', linewidth=4):
        """
        Draw a line using endpoints
        :return: None
        """
        if ltype == 'straight':
            turtle.color(color)
            turtle.pensize(linewidth)
            turtle.penup()
            turtle.setpos(start)
            turtle.pendown()
            turtle.goto(end)
            turtle.penup()
        return None

    def parallelogram(self, angle=45, length=25):
        """
        Draw the parallelogram with filled color
        :return: polygon - Turtle object
        """
        from math import sin
        polygon = turtle.Turtle()
        polygon.penup()
        polygon.begin_poly()
        angles = [angle, 180 - angle, angle, 180 - angle]
        lengths = [length, length * sin(angle), length, length * sin(angle)]
        for angle, len in zip(angles, lengths):
            polygon.left(angle)
            polygon.forward(len)

        polygon.end_poly()

        # poly = polygon.get_poly()
        return polygon

    def finish_line(self, xcor=200):
        """
        Draw the finish line
        :param xcor: x-coordinate of finish line
        :return: None
        """
        turtle.tracer(False)
        polygon = self.parallelogram(angle=45, length=25)
        turtle.register_shape('parallelogram', polygon.get_poly())

        # Draw the black part
        polygon.color('black')
        for i in range(8):
            polygon.penup()
            polygon.setpos(xcor, (150 - (i * 20 * 2)))
            polygon.pendown()
            polygon.shape('parallelogram')
            polygon.stamp()

        # Draw the white part
        polygon.color('white')
        for i in range(8):
            polygon.penup()
            polygon.setpos(xcor, (130 - (i * 20 * 2)))
            polygon.pendown()
            polygon.shape('parallelogram')
            polygon.stamp()

        return None

    def runway(self, start_line=-260, finish_line=195, color='white', linewidth=4):
        """
        Draw the runway
        :param start_line:
        :param finish_line:
        :param color:
        :param linewidth:
        :return:
        """
        turtle.tracer(True)
        for i in range(5):
            start, end = (start_line, 125 - i * 50), (finish_line, 125 - i * 50)
            self.line(start, end, color=color, linewidth=linewidth)
        turtle.penup()
        return None

    def bottom_ballon(self, color, width=800, height=300):
        """
        Draw the bottom ballon.
        :param color: The color of ballon
        :return: None
        """
        turtle.setpos(-width / 2, -180)
        turtle.color(color)

        # Begin to draw bottom ballon
        turtle.begin_fill()
        turtle.pendown()
        for i in [width, height, width, height]:
            turtle.forward(i)
            turtle.right(90)
        turtle.end_fill()
        # Finish

        turtle.penup()
        return None


def write_text(text, writer=turtle, pos=(0, 0), align='center', color='black', font=('Times', 16, 'bold')):
    """
    Write text at the specific position using corresponding writer
    :return: None
    """
    writer.penup()
    writer.setpos(pos)
    writer.color(color)
    writer.write(text, align=align, font=font)
    writer.penup()
    return None


def set_window(title, bgcolor='#7bb4ff'):
    """
    Set the attributes of the window, etc. backgroundcolor, title, size
    :param bgcolor: background color
    :return: None
    """
    window = turtle.Screen()
    window.title(title)
    turtle.bgcolor(bgcolor)
    turtle.penup()
    return None


def stamp_at(pos, writer=turtle, shape='turtle'):
    """
    Put a stamp on a specific position using a writer
    :return: None
    """
    writer.penup()
    writer.setpos(pos)
    writer.pendown()
    writer.shape(shape)
    writer.stamp()
    writer.penup()
    return None
