import random

class SudokuGenerator:
    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.get_board()
        self.box_length = 3

    def get_board(self):
        return [[0 for i in range(1,10)] for j in range(9)]

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()
    def valid_in_row(self, row, num):
        for item in range(9):
            if self.board[row][item] == num:
                return False
        return True

    # for input in self.board[row]:
    #     if num == input:
    #         return False
    def valid_in_col(self, col, num):
        for item in range(9):
            if self.board[item][col] == num:
                return False
        return True

        # for input in self.board[col]:
        #     if num == input:
        #         return False
        # return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[i + row_start][j + col_start] == num:
                    return False
        return True

        # for sudoku_num in range(0, row_start + 3):
        #     for sudoku_num in range(0, col_start + 3):
        #         if sudoku_num == num:
        #             return False
        # return True

    def is_valid(self, row, col, num):
        for item in range(9):
            if num == self.board[row][item]:
                return False
            elif num == self.board[item][col]:
                return False
        return True

    def fill_box(self, row_start, col_start):
        for i in range(3):
            for j in range(3):
                if self.board[i + row_start][j + col_start] == 0:
                    int_x = random.randint(1, 9)

                    while not self.is_number_unique(row_start, col_start, int_x):
                        int_x = random.randint(1, 9)
                    self.board[i + row_start][j + col_start] = int_x


        return self.board



    def is_number_unique(self, row_start, col_start, int_x):
        for i in range(3):
            for j in range(3):
                if self.board[i + row_start][j + col_start] == int_x:
                    return False
        return True















