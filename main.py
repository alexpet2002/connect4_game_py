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


def display_of_the_board(arr) -> None:
    print("---------------------", end="")
    for row in arr:
        print()
        print("| ", end="")
        for cell in row:
            if cell == 0:
                print(" ", end="")
            elif cell == 1:
                print("X", end="")
            elif cell == 2:
                print("O", end="")
            print(" | ", end="")
    print()
    print("---------------------")


def next_turn() -> None:
    global first_players_turn
    first_players_turn = not first_players_turn


def ask_user_to_input_a_column() -> int:
    user_choice = int(input("Please select a column from 1-5: "))
    return user_choice


def convert_the_user_input_to_choice() -> int:
    return ask_user_to_input_a_column() - 1


def get_users_choice() -> int:
    return convert_the_user_input_to_choice()

    # last_column


def choice_out_of_bounds(arr, choice) -> bool:
    if arr[0][choice] != 0:
        return True
    else:
        return False


def mark(row, column) -> list:
    return [row, column]


def get_marks_column(mk) -> int:
    return mk[1]


def get_marks_row(mk) -> int:
    return mk[0]


def get_the_players_mark(arr, column) -> list:
    number_of_rows = len(arr)
    for row_index in range(number_of_rows - 1):
        if arr[row_index + 1][column] != 0:
            return mark(row_index, column)
    return mark(number_of_rows - 1, column)


def set_the_players_mark(coordinates_of_mark: list, first_players_turn: bool) -> None:
    global matrix
    if first_players_turn:
        matrix[get_marks_row(coordinates_of_mark)][get_marks_column(coordinates_of_mark)] = 1
    else:
        matrix[get_marks_row(coordinates_of_mark)][get_marks_column(coordinates_of_mark)] = 2


def win_horizontally(arr, coordinates_of_mark) -> bool:
    r, c = get_marks_row(coordinates_of_mark), get_marks_column(coordinates_of_mark)

    try:
        if arr[r][c] == arr[r][c - 1] and arr[r][c] == arr[r][c - 2] and arr[r][c] == arr[r][c - 3]:
            return True
    except IndexError:
        pass

    try:
        if arr[r][c] == arr[r][c + 1] and arr[r][c] == arr[r][c - 1] and arr[r][c] == arr[r][c - 2]:
            return True
    except IndexError:
        pass

    try:
        if arr[r][c] == arr[r][c + 2] and arr[r][c] == arr[r][c + 1] and arr[r][c] == arr[r][c - 1]:
            return True
    except IndexError:
        pass

    try:
        if arr[r][c] == arr[r][c + 3] and arr[r][c] == arr[r][c + 2] and arr[r][c] == arr[r][c + 1]:
            return True
    except IndexError:
        pass
    return False


def vertically_out_of_bounds(row, arr):
    return True if row <= len(arr) - 4 else False


def win_vertically(arr, coordinates_of_mark) -> bool:
    r, c = get_marks_row(coordinates_of_mark), get_marks_column(coordinates_of_mark)

    if vertically_out_of_bounds(r, arr):
        if arr[r][c] == arr[r + 1][c] and arr[r][c] == arr[r + 2][c] and arr[r][c] == arr[r + 3][c]:
            return True
        else:
            return False
    else:
        return False


def win_diagonally_left(arr, coordinates_of_mark) -> bool:
    r, c = get_marks_row(coordinates_of_mark), get_marks_column(coordinates_of_mark)
    try:
        if arr[r][c] == arr[r + 1][c - 1] and arr[r][c] == arr[r + 2][c - 2] and arr[r][c] == arr[r + 3][c - 3]:
            return True
    except IndexError:
        pass
    try:
        if arr[r][c] == arr[r - 1][c + 1] and arr[r][c] == arr[r + 1][c - 1] and arr[r][c] == arr[r + 2][c - 2]:
            return True
    except IndexError:
        pass
    try:
        if arr[r][c] == arr[r - 2][c + 2] and arr[r][c] == arr[r - 1][c + 1] and arr[r][c] == arr[r + 1][c - 1]:
            return True
    except IndexError:
        pass
    try:
        if arr[r][c] == arr[r - 3][c + 3] and arr[r][c] == arr[r - 2][c + 2] and arr[r][c] == arr[r - 1][c + 1]:
            return True
    except IndexError:
        pass
    return False


def win_diagonally_right(arr, coordinates_of_mark) -> bool:
    r, c = get_marks_row(coordinates_of_mark), get_marks_column(coordinates_of_mark)
    try:
        if arr[r][c] == arr[r + 1][c + 1] and arr[r][c] == arr[r + 2][c + 2] and arr[r][c] == arr[r + 3][c + 3]:
            return True
    except IndexError:
        pass
    try:
        if arr[r][c] == arr[r - 1][c - 1] and arr[r][c] == arr[r + 1][c + 1] and arr[r][c] == arr[r + 2][c + 2]:
            return True
    except IndexError:
        pass
    try:
        if arr[r][c] == arr[r - 2][c - 2] and arr[r][c] == arr[r - 1][c - 1] and arr[r][c] == arr[r + 1][c + 1]:
            return True
    except IndexError:
        pass
    try:
        if arr[r][c] == arr[r - 3][c - 3] and arr[r][c] == arr[r - 2][c - 2] and arr[r][c] == arr[r - 1][c - 1]:
            return True
    except IndexError:
        pass
    return False


def win_diagonally(arr, coordinates_of_mark) -> bool:
    return win_diagonally_left(matrix, coordinates_of_mark) or win_diagonally_right(matrix, coordinates_of_mark)


def four_consecutive_marks(matrix, coordinates_of_mark) -> bool:
    return win_horizontally(matrix, coordinates_of_mark) or win_vertically(matrix,
                                                                           coordinates_of_mark) or win_diagonally(
        matrix, coordinates_of_mark)


def all_columns_are_taken(arr) -> bool:
    for row in arr:
        for cell in row:
            if cell == 0:
                return False
    return True


def conditions_to_stop(arr, coordinates_of_mark) -> bool:
    return all_columns_are_taken(arr) or four_consecutive_marks(arr, coordinates_of_mark)


def winning_message(first_players_turn) -> None:
    if first_players_turn:
        print("Player number 2 won!")
    else:
        print("Player number 1 won!")


def ending_message():
    print("end of program")


def do_you_wanna_try_again():
    global matrix
    global first_players_turn
    global continue_playing
    global try_again
    response = input("Do you want to replay? y/n")
    if response == "y":
        matrix = get_matrix_based_on_number_rows_and_columns()
        first_players_turn = True
        continue_playing = True
    elif response == "n":
        try_again = False
    else:
        print("Your inout is invalid, please try again: ")


def game_loop():
    global continue_playing
    while continue_playing:
        display_of_the_board(matrix)
        users_choice = get_users_choice()
        users_mark = get_the_players_mark(matrix, users_choice)
        set_the_players_mark(users_mark, first_players_turn)
        continue_playing = not conditions_to_stop(matrix, users_mark)
        next_turn()
    display_of_the_board(matrix)
    winning_message(first_players_turn)
    do_you_wanna_try_again()


if __name__ == '__main__':
    # imports

    # Declared variables
    matrix = get_matrix_based_on_number_rows_and_columns()
    first_players_turn = True
    continue_playing = True
    try_again = True

    # Functions

    while try_again:
        game_loop()

    ending_message()
