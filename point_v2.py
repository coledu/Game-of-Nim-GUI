''' File: points.py
    Demonstrates a small Point class and related main()    '''

import turtle # needed by both point class and main()
import random # needed by main()

class Point:
    """ Point class represents and manipulates x,y coordinates.
        Is dependent upon the turtle libraries for draw_point() method.
         In particular, a Screen must exist and the color mode should be set to 255"""

    def __init__(self, x=0, y=0): # Each Point object has its own x and y coordinates and possibly a turtle
        '''initializer method aka Constructor:
        Creates a new point at x, y. If no x, y are given, the point is created at 0, 0 '''
        self.x = x
        self.y = y
        self.turtle = None # To save space we only create a turtle if and when draw_point() is used

    def __str__(self):
        ''' Makes the str() function work with Points'''
        return "({0}, {1})".format(self.x, self.y)

    def distance_from_origin(self):
        ''' Compute my distance from the origin '''
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def user_set(self):
        ''' Allows the user to change the x and y value of a Point'''
        self.x=int(raw_input("Enter x: "))
        self.y=int(raw_input("Enter y: "))

    def draw_point(self, r=0, g=0, b=0, text = ""): # black is the default color
        '''instanciates a Turtle object and draws the Point on the Screen'''
        self.turtle = turtle.Turtle()
        self.turtle.color(r, g, b)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.showturtle()
        self.turtle.stamp()
        # This code was added from the original point.py class
        # to allow custom text to be written to the screen
        if text == "":
            self.turtle.write(str(self), True)
        else:
            self.turtle.write(text, True)
        self.turtle.hideturtle()


# The following code is removed because we instantiated objects
# using this class in another file (place_pin_classes.py)!!!


# def main():
#     '''Program demonstrates use of the Point class'''
#
#     p = Point()         # Instantiate an object of type Point at (0, 0)
#     print("point = "+ str(p))
#
#     q = Point(30, 40)     # Make a second point at (30, 40)
#     print("point = "+ str(q))
#
#     wn = turtle.Screen()
#     wn.colormode(255)   # change color modes
#
#     p.draw_point() # draw Point p as the default color of black
#     q.draw_point(255, 0, 0) # draw Point q as red (255, 0, 0)
#
#     print("\nPlease enter x and y values. To end enter x = 0 and y = 0.")
#     while q.x!=0 or q.y!=0:
#         q.user_set()
#         print("point = "+ str(q))
#         q.draw_point(random.randrange(256), random.randrange(256), random.randrange(256))
#
#     wn.bye()  # closes turtle window without requiring user click
#
# main()