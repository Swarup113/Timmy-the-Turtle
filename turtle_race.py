import turtle, random

from tkinter import messagebox


def turtle_race():
    import turtle, random

    screen = turtle.Screen()

    screen.bgcolor("lightgreen")

    # Add text in the top right corner
    phase_text = turtle.Turtle()
    phase_text.penup()
    phase_text.hideturtle()
    phase_text.goto(270, 265)  # Position for the top right corner
    phase_text.write("Phase 1", align="right", font=("Courier", 13, "normal"))

    screen = turtle.Screen()

    screen.setup(width=600, height=600)

    race = False

    did_i_win = False

    colors = ['Red', 'Blue', 'Green']

    while True:

        user_bet = screen.textinput(title="Enter Your Bet",
                                    prompt="Which Turtle Do You Want To Bet On? Type One Of the RGB Colors: ").title()

        if len(user_bet) != 0 and user_bet in colors:
            break

    x_coordinates = -50

    turtles = []

    # Create the starting line
    starting_line = turtle.Turtle()
    starting_line.penup()
    starting_line.goto(-100, -250)
    starting_line.pendown()
    starting_line.pensize(3)
    starting_line.color("black")
    starting_line.goto(100, -250)
    starting_line.hideturtle()

    # Create the finishing line
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.goto(-100, 280)
    finish_line.pendown()
    finish_line.pensize(5)
    finish_line.color("#196F3D")
    finish_line.goto(100, 280)
    finish_line.hideturtle()

    for i in range(3):
        new_turtle = turtle.Turtle()

        new_turtle.shape('turtle')

        new_turtle.color(colors[i])

        new_turtle.penup()

        new_turtle.goto(x_coordinates, -250)

        new_turtle.left(90)

        x_coordinates += 50

        turtles.append(new_turtle)

    if user_bet:
        race = True

    while race:

        for single_turtle in turtles:

            random_distance = random.randint(0, 10)

            single_turtle.forward(random_distance)

            if single_turtle.ycor() > 260:

                race = False

                winner = single_turtle.pencolor()

                if winner == user_bet:

                    messagebox.showinfo(title="Race Info", message="Congrats! You've Won")

                    did_i_win = True

                    screen.clear()

                    screen.reset()

                    return winner, did_i_win


                else:

                    messagebox.showinfo(title="Race Info", message=f"You've Lost! The {winner} Turtle is the Winner")

                    try_again = messagebox.askyesno(title="Try Again", message="Try again?")

                    if try_again:

                        screen.clear()
                        screen.reset()

                        return turtle_race()

                    else:
                        return None, None
