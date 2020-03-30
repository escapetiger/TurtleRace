"""
    Turtle Race 小游戏
    Author: Escape
    Version: 1.0
    Date: 2020/3/28
"""
import turtle
from turtle import Turtle
from random import randint
from Source import *


class TurtleRacer(Turtle):
    def __init__(self, name='', pcolor=''):
        Turtle.__init__(self, shape='turtle')
        self.name = name
        self.pcolor = pcolor

    def move(self):
        """
        MOVE THE TURTLES
        :return: x coordinate of this turtle
        """
        turtle.tracer(True)
        self.penup()
        self.forward(randint(1, 20))
        self.pendown()
        return self


def set_turtle(pos, speed=0, color="black", name=''):
    # TURTLE
    tt = TurtleRacer(name=name, pcolor=color)
    tt.speed(speed)
    tt.color(color)
    tt.penup()
    tt.goto(pos)
    tt.pendown()
    return tt


def update_game_info(new_turtle_list, info_list):
    i = 0
    info_list.clear()
    turtle.tracer(False)
    new_turtle_list = sorted(new_turtle_list, key=lambda x: x.xcor(), reverse=True)
    for i in range(4):
        write_text(str(i + 1),
                   writer=info_list,
                   pos=(-325, -210 - i * 25),
                   color=new_turtle_list[i].pcolor,
                   align="left", font=("Times", 16, "bold")
                   )

        stamp_at((-300, -200 - i * 25), info_list)

        write_text(new_turtle_list[i].name,
                   writer=info_list,
                   pos=(-275, -210 - i * 25),
                   color=new_turtle_list[i].pcolor,
                   align="left", font=("Times", 16, "bold")
                   )
    info_list.hideturtle()


def play():
    turtle.onkey(None, 'space')
    turtle.clear()
    # Game Page
    sc = Source('Game Page')
    set_window(title='TURTLE RACE')
    sc.bottom_ballon(color='#a7a4da')
    sc.finish_line()
    sc.runway()
    write_text('TURTLE RACE', pos=(0, 200), color='white', font=("Times", 30, "bold"))
    # Create turtle players and name them the way your like
    turtle_list = []
    color_list = ['Crimson', 'DarkslateBlue', 'SeaGreen', 'orange']
    name_list = ['China', 'America', 'Italy', 'Japan']
    turtle.tracer(False)
    for i in range(4):
        turtle_list.append(set_turtle((-250, 100 - i * 50), color=color_list[i], name=name_list[i]))
    # MAIN LOOP
    current_leader = turtle_list[0]
    info_list = Turtle()
    turtle.tracer(True)
    while current_leader.xcor() < 200:
        new_turtle_list = list(map(TurtleRacer.move, turtle_list))
        current_leader = max(new_turtle_list, key=lambda x: x.xcor())
        update_game_info(new_turtle_list, info_list)
    # Output game result
    write_text("{} won the game!".format(current_leader.name), pos=(0, -250), color='Cornsilk',
               font=("Times", 24, "bold"))


def main():
    # Home Page
    turtle.clear()
    sc = Source('Home Page')
    set_window(title='TURTLE RACE')
    sc.logo(pos=(0, 0))
    sc.bottom_ballon(color='#a7a4da')
    write_text('Aurthor: Escape', pos=(300, 300), color='white', font=('Times', 12))
    write_text('TURTLE RACE', pos=(0, 200), color='white', font=("Times", 30, "bold"))
    write_text("press spacebar to start game", pos=(0, -300), color='white', font=("Courier", 16, "bold"))

    turtle.hideturtle()
    # The game start once press spacebar
    turtle.onkey(play, "space")
    turtle.listen()
    turtle.done()
    return "EVENTLOOP"

if __name__ == '__main__':
    main()
    turtle.mainloop()
