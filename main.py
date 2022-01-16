# Prints a table
# def print_array_positions(n):
#     """ n: numbers of rows-columns
#         array: board of the game
#     >>> print_array_positions(10)
#         1     2     3     4     5     6     7     8     9     10
#     ------------------------------------------------------------
#     A|  A1 |  A2 |  A3 |  A4 |  A5 |  A6 |  A7 |  A8 |  A9 | A10 |
#     B|  B1 |  B2 |  B3 |  B4 |  B5 |  B6 |  B7 |  B8 |  B9 | B10 |
#     C|  C1 |  C2 |  C3 |  C4 |  C5 |  C6 |  C7 |  C8 |  C9 | C10 |
#     D|  D1 |  D2 |  D3 |  D4 |  D5 |  D6 |  D7 |  D8 |  D9 | D10 |
#     E|  E1 |  E2 |  E3 |  E4 |  E5 |  E6 |  E7 |  E8 |  E9 | E10 |
#     F|  F1 |  F2 |  F3 |  F4 |  F5 |  F6 |  F7 |  F8 |  F9 | F10 |
#     G|  G1 |  G2 |  G3 |  G4 |  G5 |  G6 |  G7 |  G8 |  G9 | G10 |
#     H|  H1 |  H2 |  H3 |  H4 |  H5 |  H6 |  H7 |  H8 |  H9 | H10 |
#     I|  I1 |  I2 |  I3 |  I4 |  I5 |  I6 |  I7 |  I8 |  I9 | I10 |
#     J|  J1 |  J2 |  J3 |  J4 |  J5 |  J6 |  J7 |  J8 |  J9 | J10 |
#     ------------------------------------------------------------
#
#     """
#
#     def array(n):
#         return [[" " for x in range(n)] for y in range(n)]
#
#     letters = "ABCDEFGHIJK"
#
#     numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#
#     array = array(n)
#
#     for i in range(len(array)):
#         for j in range(len(array)):
#             array[i][j] = letters[i] + numbers[j]
#     print("    ", end="")
#
#     for i in range(n):
#         print(str(i + 1) + "\t".expandtabs(5), end="")
#     print()
#     print("------" * n)
#
#     for i in range(n):
#         print(letters[i], end="")
#         for j in range(n):
#             print(("|" + array[i][j].center(5) + "\t").expandtabs(-2), end="")
#         print("|")
#     print("------" * n)


# turn = 0
# game_continues = True


# def pick_your_mrk():
#     mrk = input(f"Pick your mark, X or O ?")
#     if mrk == "O":
#         paikths1 = 'O'
#         paikths2 = 'X'
#
#     elif mrk == 'X':
#         paikths1 = 'X'
#         paikths2 = 'O'
#
#     else:
#         print("Your input is invalid, please try again!")


# def selection_of_user():
#     selection = int(input("Make your Selection(0-10): "))
#     values_range = list(range(1, 11))
#     if selection in values_range:
#         return selection
#     else:
#         selection = input("Try Again, Please make your selection (0 - 10) : ")
#         return selection


# def turns():
#     turn = 0
#
#     while game_continues:
#         turn += 1
#         turn = turn % 2
#         # turn % 2 == 0 doesnt work
#         # Ask for paikths 1 input
#         if turn == 0:
#             print("Player 2, your selection is ", selection_of_user())
#         # Ask for paikths 2 input
#         else:
#             print("Player 1, your selection is ", selection_of_user())


# def win_conditions()

def get_matrix_based_on_number_rows_and_columns(columns: int = 5, rows: int = 5) -> list:
    return [[0 for x in range(columns)] for y in range(rows)]


def display_of_the_matrix(arr) -> None:
    print("---------------------", end="")
    for row in arr:
        print()
        print("| ", end="")
        for cell in row:
            print(cell, end="")
            print(" | ", end="")
    print()
    print("---------------------")


if __name__ == '__main__':
    matrix = get_matrix_based_on_number_rows_and_columns()
    display_of_the_matrix(matrix)

# print_array_positions(10)
# turn_count = turns()
# turns()
# selection_of_user()
# pick_your_mrk()
# for i in range(int(input())):
#     try:
#         a, b = map(int, input().split())
#         print(a // b)
#     except Exception as e:
#         print("Error Code:", e)
