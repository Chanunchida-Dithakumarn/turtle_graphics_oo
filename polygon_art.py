import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self):
        return turtle.goto(self.location[0], self.location[1])


def get_new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class PolygonArt():
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def run(self):
        choice = int(input(f"Enter number of art you would like to generate 1 to 9: "))
        for _ in range(30):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            reduction_ratio = 0.618
            num_levels = 2

            if choice == 1:
                num_sides = 3
                art = Polygon(num_sides, size, orientation, location, color, border_size)
                art.draw()
            elif choice == 2:
                num_sides = 4
                art = Polygon(num_sides, size, orientation, location, color, border_size)
                art.draw()
            elif choice == 3:
                num_sides = 5
                art = Polygon(num_sides, size, orientation, location, color, border_size)
                art.draw()
            elif choice == 4:
                num_sides = random.randint(3, 5)
                art = Polygon(num_sides, size, orientation, location, color, border_size)
                art.draw()
            elif choice == 5:
                num_sides = 3
                art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                art.draw()
            elif choice == 6:
                num_sides = 4
                art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                art.draw()
            elif choice == 7:
                num_sides = 5
                art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                art.draw()
            elif choice == 8:
                num_sides = random.randint(3, 5)
                art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                art.draw()
            elif choice == 9:
                num_sides = random.randint(3, 5)
                num_levels = random.randint(0, 2)
                art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio)
                art.draw()
        turtle.done()


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        if self.num_levels > 0:
            for i in range(self.num_levels):
                super().draw()
                self.size *= self.reduction_ratio
                self.location[0] += self.size * (1 - self.reduction_ratio) / 2
                self.location[1] += self.size * (1 - self.reduction_ratio) / 2
                super().draw()


run = PolygonArt()
run.run()
