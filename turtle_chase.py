import turtle
import random


def turtle_chase():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Turtle Game")
    screen.bgcolor("light yellow")
    screen.setup(width=600, height=600)

    # Add text in the top right corner
    phase_text = turtle.Turtle()
    phase_text.penup()
    phase_text.hideturtle()
    phase_text.goto(270, 265)  # Position for the top right corner
    phase_text.write("Phase 2", align="right", font=("Courier", 13, "normal"))

    # Create the player turtle
    player = turtle.Turtle()
    player.shape("turtle")
    player.color("blue")
    player.speed(0)
    player.penup()
    player.goto(0, -250)

    # Create the food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("green")
    food.speed(0)
    food.penup()
    food.goto(random.randint(-280, 280), random.randint(-280, 280))
    food.shapesize(0.8)

    # Create the enemy
    enemy = turtle.Turtle()
    enemy.shape("triangle")
    enemy.color("red")
    enemy.speed("fastest")
    enemy.penup()
    enemy.goto(random.randint(-80, 80), random.randint(80, 80))
    enemy.shapesize(1.5)

    # Initialize the score
    score = 0

    # Display the score on the screen
    score_display = turtle.Turtle()
    score_display.speed(0)
    score_display.color("black")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 260)
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Function to move the player and change its face
    def move_up():
        player.setheading(90)
        y = player.ycor()
        y += 20
        player.sety(y)

    def move_down():
        player.setheading(270)
        y = player.ycor()
        y -= 20
        player.sety(y)

    def move_left():
        player.setheading(180)
        x = player.xcor()
        x -= 20
        player.setx(x)

    def move_right():
        player.setheading(0)
        x = player.xcor()
        x += 20
        player.setx(x)

    # Keyboard bindings
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")

    # Function to check for collision
    def is_collision(t1, t2):
        distance = t1.distance(t2)
        if distance < 20:  # Adjust the collision threshold as needed
            return True
        else:
            return False

    # Function to end the game
    def game_over(message):
        player.hideturtle()
        food.hideturtle()
        enemy.hideturtle()
        score_display.clear()
        if message == "Game Over!":
            score_display.color("red")
            score_display.goto(0,0)
        else:
            score_display.color("green")
            score_display.goto(0, -150)
        score_display.write(message, align="center", font=('Courier', 48, "bold"))

    # Main game loop
    while score < 50:
        # Check for collision with food
        if is_collision(player, food):
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        # Check for collision with enemy
        if is_collision(player, enemy):
            game_over("Game Over!")

            break

        # Move the enemy
        enemy.setheading(enemy.towards(player))
        enemy.forward(2)

        # Boundary checking for enemy
        if enemy.xcor() > 290 or enemy.xcor() < -290 or enemy.ycor() > 290 or enemy.ycor() < -290:
            enemy.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Update the screen
        screen.update()

    # Check if the player won
    if score >= 50:
        game_over("You Have Won")

        return True

    # Close the game window on click
    screen.exitonclick()
