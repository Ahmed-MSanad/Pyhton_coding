import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-100+40*turtle_index)
    turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
