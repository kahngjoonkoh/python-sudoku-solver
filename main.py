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
        if count == 3 or count == 6:
            print("---------------------")
        row_count = 0
        for item in row:
            if row_count == 3 or row_count == 6:
                print("|", end=" ")
            if not show_zero and item == 0:
                item = " "
            print(item, end=" ")
            row_count += 1
        print("")
        count += 1
    print("\n")


def assured_fill(input_grid):
    terminate = False
    while not terminate:
        terminate = scan(input_grid)
    return input_grid


def scan(input_grid):
    for i in range(len(input_grid)):
        row = input_grid[i]
        for j in range(len(row)):
            item = row[j]
            if item == 0:  # Detect a blank area.
                missing_num = scan_row([1, 2, 3, 4, 5, 6, 7, 8, 9], row)
                missing_num = scan_column(missing_num, input_grid, j)
                missing_num = scan_block(missing_num, input_grid, i, j)
                if len(missing_num) == 1:
                    input_grid[i][j] = missing_num[0]
                    print(f"Filled {missing_num[0]}")
                    return False
    return True


def scan_row(item_not_found, row):
    for item in row:
        if item in item_not_found:
            item_not_found.remove(item)
    return item_not_found


def scan_column(item_not_found, input_grid, column):
    temp_col = []
    for row in input_grid:
        temp_col.append(row[column])
    for item in temp_col:
        if item in item_not_found:
            item_not_found.remove(item)
    return item_not_found


def scan_block(item_not_found, input_grid, row, column):
    block = get_block(input_grid, row, column)
    for line in block:
        for item in line:
            if item in item_not_found:
                item_not_found.remove(item)
    return item_not_found


def get_block(input_grid, row, column):
    block = []
    if row <= 2:
        if column <= 2:
            for i in range(0, 3):
                block.append(input_grid[i][0:3])
            return block
        elif 3 <= column <= 5:
            for i in range(0, 3):
                block.append(input_grid[i][3:6])
            return block
        elif 6 <= column <= 8:
            for i in range(0, 3):
                block.append(input_grid[i][6:9])
            return block
    elif 3 <= row <= 5:
        if column <= 2:
            for i in range(3, 6):
                block.append(input_grid[i][0:3])
            return block
        elif 3 <= column <= 5:
            for i in range(3, 6):
                block.append(input_grid[i][3:6])
            return block
        elif 6 <= column <= 8:
            for i in range(3, 6):
                block.append(input_grid[i][6:9])
            return block
    elif 6 <= row <= 8:
        if column <= 2:
            for i in range(6, 9):
                block.append(input_grid[i][0:3])
            return block
        elif 3 <= column <= 5:
            for i in range(6, 9):
                block.append(input_grid[i][3:6])
            return block
        elif 6 <= column <= 8:
            for i in range(6, 9):
                block.append(input_grid[i][6:9])
            return block


def check_num_ability():
    pass


def solve_sudoku(input_grid):
    new_grid = assured_fill(input_grid)
    print_sudoku_grid(new_grid, show_zero=False)


grid = read_sudoku_file("output_file.sudoku")
print_sudoku_grid(grid, show_zero=False)
solve_sudoku(grid)
