'''
[ Find the crossing (graphic calculations) ]

Description
You are given four tuples.
In each tuple there is coordinates x and y of a point.
There is one and only one line, that goes through two points, so with four points you can have two lines: first and second tuple is two points of a first line, thirs and fourth tuple is two points of the second line.
Your task is to find and return a tuple with x and y coordinates of lines crossing point.

Numbers can be positive as well as negative, integer or floats.
Your answer shouldn't be rounded.

Note, that if two lines are the same ( have infinite crossing points ) or parallel ( have no crossing points ), you will need to return None/Nothing depending on language.
'''


def find_the_crossing(a, b, c, d):
    # Unpack points
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d

    # Calculate the slopes (m1 and m2)
    # m = (y2 - y1) / (x2 - x1) for the first line
    # m = (y4 - y3) / (x4 - x3) for the second line
    denominator1 = (x2 - x1)
    denominator2 = (x4 - x3)

    if denominator1 == 0 or denominator2 == 0:
        # If one of the lines is vertical, handle it explicitly
        if denominator1 == 0 and denominator2 == 0:
            return None  # Two vertical lines are parallel
        elif denominator1 == 0:  # first line vertical
            x_cross = x1
            m2 = (y4 - y3) / (x4 - x3)
            y_cross = m2 * (x_cross - x3) + y3
            return (x_cross, y_cross)
        else:  # second line vertical
            x_cross = x3
            m1 = (y2 - y1) / (x2 - x1)
            y_cross = m1 * (x_cross - x1) + y1
            return (x_cross, y_cross)

    m1 = (y2 - y1) / denominator1  # Slope of the first line
    m2 = (y4 - y3) / denominator2  # Slope of the second line

    # Check if the lines are parallel
    if m1 == m2:
        return None  # Parallel lines do not intersect

    # Calculate intersection point
    # y1 = m1 * x + b1
    # y3 = m2 * x + b2
    # Set the two equations equal: m1 * x + b1 = m2 * x + b2
    # Solve for x:
    b1 = y1 - m1 * x1  # y-intercept of the first line
    b2 = y3 - m2 * x3  # y-intercept of the second line

    # m1 * x + b1 = m2 * x + b2
    # (m1 - m2) * x = b2 - b1
    x_cross = (b2 - b1) / (m1 - m2)
    y_cross = m1 * x_cross + b1  # Calculate y using the equation of the first line

    return (x_cross, y_cross)


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
