import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'black', 'yellow', 'purple', 'pink', 'cyan', 'brown']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try Again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

def randomize_colors(no_of_racers):
    random.shuffle(COLORS)
    return COLORS[:no_of_racers]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        x_pos = -WIDTH // 2 + (i + 1) * spacingx
        y_pos = -HEIGHT // 2 + 20
        racer.setpos(x_pos, y_pos)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= (HEIGHT // 2)- 10:
                return colors[turtles.index(racer)]

def main():
    no_of_racers = get_number_of_racers()
    init_turtle()
    colors = randomize_colors(no_of_racers)
    winner = race(colors)
    print("The winner is the turtle with color: ", winner[0].upper() + winner[1:])
    time.sleep(5)

if __name__ == "__main__":
    main()