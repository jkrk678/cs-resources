# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def do_twice(f, v):
    f(v)
    f(v)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

def draw_border(cols):
    print('+ - - - - ' * cols, end='+')
    print(' ')

def draw_row(cols):
    print('|         ' * cols, end='|')
    print(' ')

def draw_border_and_rows(cols):
    draw_border(cols)
    do_four(draw_row, cols)

def draw_2x2_grid():
    do_twice(draw_border_and_rows, 2)
    draw_border(2)

draw_2x2_grid()

# Write a function that draws a similar grid with four rows and four columns.
def draw_4x4_grid():
    do_four(draw_border_and_rows, 4)
    draw_border(4)

draw_4x4_grid()