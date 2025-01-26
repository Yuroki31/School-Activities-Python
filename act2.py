def print_grid():
    horizontal_line = "+ - - - - + - - - - +"
    vertical_line = "|         |         |"

    def print_horizontal_line():
        print(horizontal_line)

    def print_vertical_lines():
        for x in range(4):
            print(vertical_line)

    print_horizontal_line()
    print_vertical_lines()
    print_horizontal_line()
    print_vertical_lines()
    print_horizontal_line()

print_grid()
