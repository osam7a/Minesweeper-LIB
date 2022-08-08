from Minesweeper import *

b = Board(5, 5)
b.place_mines(5, (0, 0))
print(b.show_real_board())
while True:
    inp = input("Enter row, column: ")
    f_or_m = inp[0]
    row = int(inp[1:].split()[0])
    col = int(inp[1:].split()[1])
    if f_or_m == "f":
        b.flag(row, col)
        print(b.visualize())
    elif f_or_m == "m":
        b.reveal(row, col)
        print(b.visualize())