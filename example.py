import turtle
import math
import ast  # lets us safely turn text the user types (like "[(0,0),(1,0)]") into real Python lists/tuples


def square(x_i, y_i, size):
    turtle.penup()
    turtle.goto(x_i, y_i)
    turtle.pendown()

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

square(15, 15, 150)

def rotation(x_c, y_c, angle, size):
    rad_angle = math.radians(angle + 135)
    half_diag = math.sqrt(2) * size / 2
    x = x_c + half_diag * math.cos(rad_angle)
    y = y_c + half_diag * math.sin(rad_angle)
    print(x,y)
    turtle.setheading(angle)
    square(x, y, size)

rotation(15, 15, 45, 150)

# turtle.clearscreen()

turtle.setheading(0)
def polygon(x_i, y_i, size, num_size):
    turtle.penup()
    turtle.goto(x_i, y_i)
    turtle.pendown()
    for _ in range(num_size):
        turtle.forward(size)
        turtle.right(360/num_size)

polygon(-150,-150, 50,6)
polygon(-200,250, 50,13)




def pol_vertices(x_c, y_c, size, num_sides):
    # unlike square()/polygon() above, this does NOT draw anything.
    # it just calculates and returns the (x, y) of every corner, as a list.
    # we need the full list of corners *before* drawing, because for the
    # chosen side we won't draw a straight line - we'll draw the generator
    # shape instead, and to do that we need to know where that side starts
    # and ends.
    vertices = []
    radius = size / (2 * math.sin(math.pi / num_sides))  # derived earlier: half-edge / sin(half the central angle)
    for i in range(num_sides):
        angle = math.radians(360 * i / num_sides + 180 / num_sides)  # the "+half-step" is what makes a square come out axis-aligned, like square() does
        vx = x_c + radius * math.cos(angle)
        vy = y_c + radius * math.sin(angle)
        vertices.append((vx, vy))
    return vertices


# =================================================================
# STEP 1 - ask the user for the polygon's own parameters: how many
# sides, where its center is, how long each side is, and which
# side number gets replaced. this is just the input-gathering you
# already wrote for num_sides/replaced_side - I added center/size
# since pol_vertices() needs them to actually place the polygon.
# =================================================================

num_sides = int(input("How many sides will the polygon have?: "))
x_c = float(input("Center x coordinate: "))
y_c = float(input("Center y coordinate: "))
size = float(input("Side length: "))

while True:
    replaced_side = int(input("Which side do you want to replace?: "))
    if 0 <= replaced_side < num_sides:
        break
    print("Out of range, try again.")


# =================================================================
# STEP 2 - ask for the shape that replaces that one side.
#
# we ask for it in a "normalized" frame: a list of (u, v) points
# that must start at (0, 0) and end at (1, 0) - as if that one
# side had length 1 and lay flat on the x-axis. we check that
# condition here so that step 4 (the transform) is guaranteed to
# line up perfectly with the real side's start/end, whatever
# shape the user draws in between.
# =================================================================

print("Now define the shape that replaces that side.")
print("Give a list of (u, v) points starting at (0,0) and ending at (1,0).")
print("Example (a Koch-style bump): [(0,0), (0.33,0), (0.5,0.29), (0.66,0), (1,0)]")

while True:
    raw_generator = input("Generator points: ")
    generator = ast.literal_eval(raw_generator)  # text -> real list of tuples, without the security risk of eval()
    if generator[0] == (0, 0) and generator[-1] == (1, 0):
        break
    print("The shape must start at (0,0) and end at (1,0). Try again.")


# the real corners of the polygon we're about to draw
vertices = pol_vertices(x_c, y_c, size, num_sides)


# =================================================================
# STEP 3 - map one normalized (u, v) point onto a real side.
#
# (dx, dy) is the vector from the side's start to its end: its
# LENGTH is the real side length, its DIRECTION is the real side's
# angle. using (dx, dy) as our "u axis" and the perpendicular
# (-dy, dx) as our "v axis" scales, rotates AND moves the
# normalized point onto the real side in one go - that's why no
# separate call to a length/angle formula is needed here, unlike
# in square()/rotation() above.
# =================================================================

def transform_point(u, v, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    x = start[0] + u * dx - v * dy
    y = start[1] + u * dy + v * dx
    return x, y


# =================================================================
# STEP 4 - draw one side of the polygon.
#
# "use_generator" is a plain True/False flag: if this is the side
# the user picked, walk through every (u, v) point of the generator,
# transformed onto this specific side. otherwise, just go straight
# from start to end like square()/polygon() always did.
# =================================================================

def draw_side(start, end, use_generator):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()

    if use_generator:
        for u, v in generator:
            turtle.goto(transform_point(u, v, start, end))
    else:
        turtle.goto(end)


# =================================================================
# STEP 5 - walk around the whole polygon, one side at a time.
#
# vertices[1:] + vertices[:1] is the vertex list shifted by one
# slot, so zip()-ing it against the original list pairs up
# (v0,v1), (v1,v2), ..., and finally (v_last, v0) - that last pair
# is what "closes" the polygon back to its starting corner.
# enumerate() additionally hands us the side's index i, so we can
# check it against replaced_side and decide which drawing mode to use.
# =================================================================

sides = zip(vertices, vertices[1:] + vertices[:1])
for i, (start, end) in enumerate(sides):
    draw_side(start, end, use_generator=(i == replaced_side))


turtle.exitonclick()

# case 3 
# arbitrary regular polgon given the number of sides 
# (all the other parameters still apply)
# DONE

# case 4 
# replace a side of the polygon with an arbitrary 
# series of lines scaled to the length of the side
# the user should provide the shape that will replace the side
# and whatever shape we chose, that has to be scaled to replace correctly the side of the polygon
