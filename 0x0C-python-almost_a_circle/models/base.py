import json
import csv
import turtle


class Base:
    # Rest of the code...

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): a list of rectangle instances.
            list_squares (list): a list of square instances.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor('#000000')
        turt.shape('turtle')
        turt.color('#ffffff')
        turt.penup()
        turt.goto(-200, 200)
        for rect in list_rectangles:
            turt.goto(turt.xcor() + (rect.width + 20), turt.ycor() - (rect.height + 20))
            turt.up()
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.penup()

        turt.goto(-200, -20)
        for square in list_squares:
            turt.goto(turt.xcor() + (square.width + 20), turt.ycor() - (square.height + 20))
            turt.up()
            turt.down()
            for i in range(4):
                turt.forward(square.width)
                turt.left(90)
            turt.penup()
        turtle.Screen().exitonclick()
