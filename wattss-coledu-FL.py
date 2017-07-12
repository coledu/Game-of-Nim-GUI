#####################################################################################################################
# Assignment: Final Project
# Authors: Dusty Cole and Sarah Watts
# Username: coledu and wattss
# Purpose: A version of The Game of Nim that is interactive with the user and allows them to play against the computer
# in a window and in a different way than the original code does.
# Acknowledgements: Dr. Jan Pearce for the handler_quit, and the handler_goto.
# Dr. Scott Hagen for the Point class used in the function
#####################################################################################################################
from gameofnim import Nim
import random
import turtle
import Tkinter
from point_v2 import Point

def main():
#Got this from Dr. Jan Pearce from on-turtle-onclick-exmaply.py
    def handler_quitit():
         wn.bye()
#Got this from Dr. Jan Pearce from on-turtle-onclick-exmaply.py
    def handler_goto(x, y):
        t.penup()
        t.speed()
        t.hideturtle()
        t.goto(x, y)
        b = t.position()
        tuple_1 = b
        x = int(tuple_1[0])
        y = int(tuple_1[1])
        return[x,y]

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.onclick(handler_goto)
    t.hideturtle()

    pile = random.randint(16,40)
    wn.bgcolor("white")
# Creates a Nim object to right the rules
    p4 = Point(0,0)
    rules = Nim(p4, pile)
    s=5
    rules.rules_window()
# This is the interactive button to enter the game
    while s!=0:
        coord = handler_goto(0,0)
        x = coord[0]
        y = coord[1]
        if 200<=x<=335 and -250<=y<=-220:
            rules.cover_button()
            wn.bgcolor("#696969")
            break

# Sets up a variable (set_up) to be  used by the Nim class to set up the window
    p = Point(-300,200)
    set_up= Nim(p, pile)
    set_up.game_window()
    set_up.button()
# Sets up a variable (removing) to be used to remove numbers and circles from the screen
    p1 = Point(-300,200)
    removing = Nim(p1, pile)

# Set ups a variable (update) used to update the square
    p2 = Point(-300, 200)
    update = Nim(p2, pile)
# Set ups a variable that tells the loser whether they win or lose
    p3 = Point(-300,0)
    pen = Nim(p3, pile)





    def player_turn():
        """
        Runs through the player turn, so that when they click on a button. Depending on what button they click on, and
        they enter the value by clicking another button that is present on the screen.
        :return:
        """

        t.speed(20)
        t.hideturtle()

        c = 1
        x = 0
        y = 0
# Runs loop while c greater than five, which cannot happen so it loop indefinably
        while c <5:

            coord = handler_goto(0,0)
            x = coord[0]
            y = coord[1]
# If the x value is between the coordinates of "up button"  and the value of c in not equal to c
            # the value of c increases by one, which in turn makes the scoreboard increase by one
            if 170>=x>=70 and 230>=y>=130 and c!=4:
                c += 1
                update.update_scoreboard(str(c))
                t.penup()
                t.goto(0,0)
# If the x value is between the coordinates of "down button" and the value of c is not equal to one,
            # the value of c decrease by one, which in turn makes the scoreboard decrease by one.
            elif 170>=x>=70 and -55<=y<=45 and c!=1:
                c -= 1
                update.update_scoreboard(str(c))
                t.penup()
                t.goto(0,0)
# If the a value is between the coordinates of "enter button" it enters the value of c into the program, and takes that
            #  number of circles away from the screen and the pile of circles.
            elif 290>=x>=190 and 139>=y>=39:
                removing.minus_circle(c)
                removing.remove_circle(c)
                break
    wn.onkey(handler_quitit, "q")
    wn.listen()
    r = 2
    while r !=0:
# Runs through the game with the user and the computer forever
        player_turn()
        if removing.value_circle() == 0:
# Breaks the function if the number of circles left after the player turn is zero.
            pen.win_statement("You Win!")
            break
        update.update_scoreboard("1")
        removing.com_turn()
        if removing.value_circle() == 0:
# Breaks the function if the number of circles left after the computer's turn is zero.
            pen.win_statement("You Lose!")
            break
        update.update_scoreboard("1")










    wn.listen()
    #wn.mainloop()
    Tkinter.mainloop()



main()