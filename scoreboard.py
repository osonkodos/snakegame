from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as high_score_file:
            data = int(high_score_file.read())
        self.high_score = data
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)

        self.write(f"high score: {self.high_score} | score: {self.score}",
                   align=ALIGNMENT,
                   font=(FONT))

    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"high score: {self.high_score} | score: {self.score}",
                   align=ALIGNMENT, font=(FONT))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.high_score}")


        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=(FONT))
