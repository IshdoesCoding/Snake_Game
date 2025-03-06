from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
score.penup()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_on = True

while game_on:

    screen.update()
    time.sleep(.1)
    snake.move()

    # collison with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.calc_Score()

    # collison with wall

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.reset()
        snake.reset()

    # self collision

    for segs in snake.segments[1::]:
        if snake.head.distance(segs) < 10:
            snake.reset()
            score.reset()


















screen.exitonclick()