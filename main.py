def read_sudoku_file(file_name):
    file = file_name
    f = open(file, "r")
    g = []
    for lines in f.readlines():
        new = lines.strip("\n")

        temp = []
        for char in new:
            temp.append(int(char))
        g.append(temp)
    return g


def print_sudoku_grid(input_grid, show_zero=True):
    count = 0
    for row in input_grid:
        row.insert(6, "|")
        row.insert(3, "|")
        if count == 3 or count == 6:
            print("---------------------")
        for item in row:
            if not show_zero and item == 0:
                item = " "
            print(item, end=" ")
        print("")
        count += 1


grid = read_sudoku_file("output_file.sudoku")
print_sudoku_grid(grid, show_zero=False)
