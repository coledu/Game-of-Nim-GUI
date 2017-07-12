#####################################################################################################################
# Assignment: Final Project
# Authors: Sarah Watts and Dusty Cole
# Username: wattss and coled
# Purpose: Create a class that can be used to create an interactive Game of Nim.
# Acknowledgements: Original Code Provided by Dusty Cole, that was used as the base to the computer turn.
#####################################################################################################################
import turtle
import random
import copy



class Nim:
    def __init__(self, posn, circle):
        """
        Iniltilizes the function
        :param posn: Posn of the turtle using the point class
        :param circle: The number of circles that need to be draw
        :return:
        """

        self.posn = posn # Uses the Point class to get posn.
        self.circle = circle
    def game_window(self):
        """
        Creates Game window with the number of circles given by the number.
        :param t: Turtle
        :param number: A random integer between 15 and 40
        :return: The game window with the number of circles, for the game of nim.
        """
        t = turtle.Turtle()
        t.hideturtle()

        for total_num in range(self.circle):
            t.hideturtle()
            t.speed(20)
            t.penup()
            t.goto(self.posn.x,self.posn.y)
            t.pendown()
            t.color("#40e0d0")
            t.begin_fill()
            t.circle(30)
            t.end_fill()
            self.posn.x= self.posn.x+65
            if self.posn.x>=25:
                self.posn.y= self.posn.y-65
                self.posn.x=-300


    def button(self):
        """
        Makes the buttons for the game
        :param t: Turtle
        :return: The buttons of the game
        """
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(20)
        t.penup()
        t.color("black")
    # Draws one of the squares behind the "scoreboard"
        t.goto(70, 41)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
        t.penup()
        t.goto(70, 139)
    # Draws one of the squares  over  a button up arrow
        t.color("#20b2aa") # Turns the color to teal
        t.pendown()
        t.begin_fill()
        for y in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
        t.penup()

        t.goto(190, 40)
    # Draws another one of the square around the enter button
        t.color("#20b2aa") # Turns the color to teal
        t.pendown()
        t.begin_fill()
        for y in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()

        t.penup()
        t.goto(70, -59)
        t.color("#20b2aa") # Turns the color to teal
        t.pendown()
    # Draws the box around the down button
        t.begin_fill()
        for y in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
   # Draws the up arrow of the button
        t.penup()
        t.goto(70,143)
        t.pendown()
        t.color("#8b8378") # Turns the color a light grey
        t.begin_fill()
        for y in range(3):
            t.pendown()
            t.forward(100)
            t.left(120)
        t.end_fill()
    # Draws the down arrow of the button
        t.penup()
        t.goto(70, 40)
        t.pendown()
        t.begin_fill()
        for y in range(3):
            t.forward(100)
            t.right(120)
        t.end_fill()
    # Draws scoreboard
        t.penup()
        t.goto(75, 136)
        t.color("white")
        t.pendown()
        t.begin_fill()
        for y in range(4):
            t.forward(90)
            t.right(90)
        t.end_fill()
        t.color("black")
        t.penup()
        t.goto(90,35)
        t.pendown()
        t.write("1", font=("Arial", 75, "normal") )
        t.color("#8b8378")  # Turns the color a light grey
        t.penup()
    # Draws the circle for the enter button and writes "Enter" on the button
        t.goto(240,50)
        t.begin_fill()
        t.circle(40)
        t.end_fill()
        t.penup()
        t.color("white")
        t.goto(210,75)
        t.write("Enter", font=  ("Arial", 20, "normal"))
        t.color("white")
    # Writes "The Game of Nim" at the bottom of the screen
        t.penup()
        t.goto(30, -140)
        t.pendown()
        t.write("The Game ", font=("Arial", 40, "normal"))
        t.penup()
        t.goto(110, -185)
        t.write("of", font = ("Arial", 40, "normal"))
        t.goto(70, -245)
        t.write("Nim", font = ("Arial", 50, "normal"))
    def remove_circle(self, removing):
        """
        Removes the number of circles for the game of nim
        :param removing: The number of circles the user tries to remove
        :return: A list with x,y coords, of the last position that the turtle was in.
        """
        t = turtle.Turtle()
# For whatever number, either the user of the computer, is removing it will draw over the existing circles on the screen.
        for total_num in range(removing):
            t.speed(20)
            t.penup()
            t.goto(self.posn.x,self.posn.y)
            t.pendown()
            t.color("#696969") # Changes the color to dark grey
            t.begin_fill()
            t.circle(30)
            t.end_fill()
# Moves the turtle to the next row to start removing circle
            self.posn.x=self.posn.x+65
            if self.posn.x>=25:
                self.posn.y= self.posn.y-65
                self.posn.x=-300
    def update_scoreboard(self, number):
        """
        This updates the original square and returns the number that the user chose depedning on what button they clicked.
        :param x: The number of the user's current choice
        """
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.speed(20)
        t.goto(75, 136)
        t.color("white")
        t.begin_fill()
    # Makes a new square in order to update the scoreboard
        for y in range(4):
            t.forward(90)
            t.right(90)
        t.end_fill()
        t.color("black")
        t.penup()
        t.goto(90,40)
        t.pendown()
    # Writes the number provided in teh square
        t.write(number, font=("Arial", 75, "normal") )
    def com_turn(self):
        """This is the computer turn and it find the remainder and subtract that from the pile. If remainder is zero it is random 1-4.
        It return the number in the pile."""
        circle = copy.deepcopy(self.circle)
# Creates a turtle to use in the computer turns
        t = turtle.Turtle()
        t.hideturtle()
        com_take= circle%5
        if com_take==0:
            com_take= random.choice(["1","2","3","4"])#Random number between 1-4 if remainder is zero.

        com_take=str(com_take)
        self.update_scoreboard(com_take)
        com_take = int(com_take)
        self.remove_circle(com_take)
        self.circle -= com_take
        return self.circle

    def minus_circle(self, subtracting):
        """
        Subracts a number from the number of circles left in order to for computer's turn to work.
        :param subtracting: The number of circles that the user takes
        :return:
        """
        self.circle -= subtracting
        return self.circle

    def value_circle(self):
        """
        Returns the value of the circle
        :return:
        """
        return self.circle

    def win_statement(self, text):
        """
        Uses a turtle to create a win statement.
        :param text: What the win statement will be, depending on if the computer wins or the user wins.
        :return:
        """
        wn = turtle.Screen()
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color("white")
        t.goto(self.posn.x, self.posn.y)
        t.write(text, font= ("Arial", 60, "normal"))
        wn.exitonclick()

    def rules_window(self):
        """
        Creates a window that starts at the beginng of the game that states the rules of the game itself.
        :return:
        """
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-200,230)
        t.color("#696969")
        t.write("The Game of Nim", font=(("Arial"), 40, "normal"))
        t.penup()
        t.goto(-330, 200)
        t.write("Welcome to the Game of Nim!", font= (("Arial"), 20, "normal"))

        t.goto(-330, 130)
        t.write("The objective of the game is to beat the computer" + "\n" + "by taking the last circle.", font= (("Arial"), 20, "normal"))

        t.goto(-330, 60)
        t.write("The rules are simple you can take one to four circles" +"\n" "at a time.", font = (("Arial"), 20, "normal"))

        t.goto(-330, -10)
        t.write("To choose how many circles you want to remove" +"\n" +"just click on the up and down buttons.", font= (("Arial"), 20, "normal"))

        t.goto(-330, -50)
        t.write("To enter you choice press the circular button.", font = (("Arial"), 20, "normal"))

        t.goto(-330, -95)
        t.write("Press q at anytime to exit the game.", font = (("Arial"), 20, "normal"))

        t.goto(-330, -140)
        t.write("Have fun!", font = (("Arial"), 20, "normal"))

        t.goto(-330, -220)
        t.write("Press the Play Game button to continue on with" +"\n" + "the game.", font = (("Arial"),20, "normal"))
        t.goto(200, -250)
        t.color("#20b2aa")
        t.pendown()
        t.begin_fill()
    # Creates the play game button
        for y in range(2):
            t.forward(135)
            t.left(90)
            t.forward(30)
            t.left(90)
        t.end_fill()
        t.color("#696969")
        t.penup()
        t.goto(200, -250)
        t.write("Play Game", font = ("Arial", 20, "normal"))
    def cover_button(self):
        """
        Covers the play game button for when the user starts the game of nim.
        :return:
        """
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(20)
        t.penup()
        t.goto(190,-260)
        t.setheading(0)
        t.color("#696969")
        t.pendown()
        t.begin_fill()
        for y in range(2):
            t.forward(150)
            t.left(90)
            t.forward(70)
            t.left(90)
        t.end_fill()
        t.goto(0,0)







