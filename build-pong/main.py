from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)
def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()