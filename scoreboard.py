from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open('data.txt') as file:
            high = int(file.read())
        self.score = 0
        self.high_score = high
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()




    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}, High Score: {self.high_score}", align = "center", font = ("Arial",20, "normal"))




    def calc_Score(self):
       self.score += 1
       self.update_score()

    # def game_0ver(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over, final score: {self.score}", align="center", font=("Arial", 20, "normal"))


    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()