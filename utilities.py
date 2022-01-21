# Global variables
from typing import List, Tuple

first_players_turn: bool = True
continue_playing: bool = True
try_again: bool = True
matrix: List[List[int]] = []
scores_of_players: List[int] = []


# Functions
# Mtrix Creation
def get_matrix_based_on_number_rows_and_columns(columns: int = 5, rows: int = 5) -> List[List[int]]:
    return [[0 for x in range(columns)] for y in range(rows)]


def size_of_the_array() -> int:
    while True:
        size = input("Please enter the number of rows/columns 5-10: ")
        if size in ["5", "6", "7", "8", "9", "10"]:
            return int(size)
        elif size == "":
            print("Default Size selected: 5")
            return 5
        else:
            print("Wrong input. Please try again.")


def intialze_matrix() -> None:
    """
    This function initializes the matrix defined as global.
    """
    global matrix
    global scores_of_players
    while True:
        choice = input("Would you like to start a new game(N) or load a game(L): ")
        if choice in ["N", "n"]:
            matrix = matrix_based_on_user_input()
            break
        elif choice in ["L", "l"]:
            load_matrix_from_file_using_name()
            break
        else:
            print("Wrong input, please try again.")


def matrix_based_on_user_input() -> List[List[int]]:
    size = size_of_the_array()
    return get_matrix_based_on_number_rows_and_columns(size, size)


# Display
def display_of_the_board(arr) -> None:
    array_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

    array_size = len(arr)
    for number in range(array_size):
        print(f"   {number + 1}", end="")

    print()
    print("--", end="")
    for rows in arr:
        print("----", end="")

    counter = 0
    for row in arr:
        print()
        print(f"{array_of_letters[counter]}| ", end="")
        counter = counter + 1
        for cell in row:
            if cell == 0:
                print(" ", end="")
            elif cell == 1:
                print("X", end="")
            elif cell == 2:
                print("O", end="")
            elif cell == 3:
                print("*", end="")
            elif cell == 4:
                print("*", end="")
            print(" | ", end="")
    print()

    print("--", end="")
    for rows in arr:
        print("----", end="")
    print()
    show_score()


# Changing turns

def next_turn() -> None:
    global first_players_turn
    first_players_turn = not first_players_turn


# Users choices
def ask_user_to_input_a_column(arr) -> int:
    while True:
        display_of_the_board(arr)
        lenght_of_array = len(arr)
        user_choice = input(
            f"Please select a column from 1-{lenght_of_array}, press S to save the file, N to start new game, L to "
            f"Load a game or E to end the game: ")
        if user_choice in ["S", "s"]:
            # seve the game
            save_matrix_to_file_using_name()
        elif user_choice in ["E", "e"]:
            # exit the game
            print("Chosen E,")
            end_the_program()
        elif user_choice in ["N", "n"]:
            # new game
            intialze_matrix()
        elif user_choice in ["L", "l"]:
            # Load game
            load_matrix_from_file_using_name()
        elif user_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            if int(int(user_choice) <= lenght_of_array) and not choice_out_of_bounds(arr, int(user_choice) - 1):
                return int(user_choice)
            print(f"Column out of range, please try again.")
        else:
            print(f"Your input is invalid. Please try again.")


def convert_the_user_input_to_choice(arr) -> int:
    return ask_user_to_input_a_column(arr) - 1


def choice_out_of_bounds(arr, choice) -> bool:
    if arr[0][choice] != 0:
        return True
    else:
        return False


def get_users_choice(arr) -> int:
    return convert_the_user_input_to_choice(arr=arr)


# Definition of Mark
def mark(row, column) -> List[int]:
    return [row, column]


def get_marks_column(mk) -> int:
    return mk[1]


def get_marks_row(mk) -> int:
    return mk[0]


def get_the_players_mark(arr, column) -> List[int]:
    number_of_rows = len(arr)
    for row_index in range(number_of_rows - 1):
        if arr[row_index + 1][column] != 0:
            return mark(row_index, column)
    return mark(number_of_rows - 1, column)


def set_the_players_mark(coordinates_of_mark: List[int]) -> None:
    global matrix
    global first_players_turn
    if first_players_turn:
        matrix[get_marks_row(coordinates_of_mark)][get_marks_column(coordinates_of_mark)] = 1
    else:
        matrix[get_marks_row(coordinates_of_mark)][get_marks_column(coordinates_of_mark)] = 2


# def win_array
def win_array(players_number: int = -1, coordinates: object = None) -> list:
    if coordinates is None:
        coordinates = []
    return [players_number, coordinates]


def get_win_array_player(win_arr: list) -> bool:
    return win_arr[0]


def get_win_array_coordinates(win_arr: list) -> list:
    return win_arr[1]


# def of win coord

def winning_coordinates(row: int, column: int) -> List[int]:
    return [row, column]


def get_winning_coordinates_row(arr) -> int:
    return arr[0]


def get_winning_coordinates_column(arr) -> int:
    return arr[1]


# Winnning conditions
def win_horizontally() -> (bool, list):
    global matrix
    global first_players_turn
    length_array = len(matrix)
    max_horizontal_check = len(matrix)
    for m in range(max_horizontal_check, 3, -1):
        for r in range(length_array):
            for c in range(length_array):
                try:
                    arr = []
                    winning_coordinates_arr = [winning_coordinates(r, c)]
                    for i in range(1, m):
                        arr.append(matrix[r][c] == matrix[r][c + i] and (matrix[r][c] == 1 or matrix[r][c] == 2))
                        winning_coordinates_arr.append(winning_coordinates(r, c + i))
                    if all(arr):
                        return True, win_array(matrix[r][c], winning_coordinates_arr)
                except IndexError:
                    pass
    return False, win_array()


def add_score_to_player(score_to_add, which_player):
    global scores_of_players
    if which_player == 1:
        scores_of_players[0] = scores_of_players[0] + score_to_add
    else:
        scores_of_players[1] = scores_of_players[1] + score_to_add


def increase_score(win_array):
    global scores_of_players
    if win_array:
        players_number = get_win_array_player(win_array)
        add_score_to_player(1, players_number)


def show_score():
    global scores_of_players
    global first_players_turn
    print(
        f"Player 1 score is: {scores_of_players[0]}, player 2 score is: {scores_of_players[1]}. It's Player {players_turn_to_number(first_players_turn)} turn.")


# def won_spot()

def replace_by_winning_spot(win_array: List) -> None:
    global matrix
    if win_array:
        coordinates = get_win_array_coordinates(win_array)
        for coordinate in coordinates:
            if get_win_array_player(win_array) == 1:
                matrix[get_winning_coordinates_row(coordinate)][
                    get_winning_coordinates_column(coordinate)] = 3
            else:
                matrix[get_winning_coordinates_row(coordinate)][
                    get_winning_coordinates_column(coordinate)] = 4


def make_column_fall(row, column):
    global matrix
    if matrix[row][column] == 3 or matrix[row][column] == 4:
        for r in range(row, 0, -1):
            matrix[r][column] = matrix[r - 1][column]
        matrix[0][column] = 0


def make_column_fall_for_all_cells():
    global matrix
    length_array = len(matrix)
    for r in range(length_array):
        for c in range(length_array):
            make_column_fall(r, c)


def vertically_out_of_bounds(row: int, arr: List[List[int]]):
    return True if row <= len(arr) - 4 else False


def win_vertically() -> Tuple[bool, list]:
    global matrix
    global first_players_turn
    length_array = len(matrix)
    max_horizontal_check = len(matrix)
    for m in range(max_horizontal_check, 3, -1):
        for r in range(length_array):
            for c in range(length_array):
                try:
                    winning_arr_bool: List[bool] = []
                    winning_coordinates_arr: List[List[int]] = [winning_coordinates(r, c)]
                    for i in range(1, m):
                        winning_arr_bool.append(
                            matrix[r][c] == matrix[r + i][c] and (matrix[r][c] == 1 or matrix[r][c] == 2))
                        winning_coordinates_arr.append(winning_coordinates(r + i, c))
                    if all(winning_arr_bool):
                        return True, win_array(matrix[r][c], winning_coordinates_arr)
                except IndexError:
                    pass
    return False, win_array()


def win_diagonally_left() -> Tuple[bool, list]:
    global matrix
    global first_players_turn
    length_array = len(matrix)
    max_horizontal_check = len(matrix)
    for m in range(max_horizontal_check, 3, -1):
        for r in range(length_array):
            for c in range(length_array):
                try:
                    arr = []
                    winning_coordinates_arr = [winning_coordinates(r, c)]
                    for i in range(1, m):
                        arr.append(
                            matrix[r][c] == matrix[r + i][c - i] and (matrix[r][c] == 1 or matrix[r][c] == 2) and (
                                    c - i >= 0))
                        winning_coordinates_arr.append(winning_coordinates(r + i, c - i))
                    if all(arr):
                        return True, win_array(matrix[r][c], winning_coordinates_arr)
                except IndexError:
                    pass
    return False, win_array()


def win_diagonally_right() -> Tuple[bool, list]:
    global matrix
    global first_players_turn
    length_array = len(matrix)
    max_horizontal_check = len(matrix)
    for m in range(max_horizontal_check, 3, -1):
        for r in range(length_array):
            for c in range(length_array):
                try:
                    arr = []
                    winning_coordinates_arr = [winning_coordinates(r, c)]
                    for i in range(1, m):
                        arr.append(matrix[r][c] == matrix[r + i][c + i] and (matrix[r][c] == 1 or matrix[r][c] == 2))
                        winning_coordinates_arr.append(winning_coordinates(r + i, c + i))
                    if all(arr):
                        return True, win_array(matrix[r][c], winning_coordinates_arr)
                except IndexError:
                    pass
    return False, win_array()


def win_diagonally(arr, coordinates_of_mark) -> bool:
    return win_diagonally_left(matrix, coordinates_of_mark) or win_diagonally_right(matrix, coordinates_of_mark)


def four_consecutive_marks(matrix, coordinates_of_mark) -> bool:
    return win_horizontally(matrix, coordinates_of_mark) \
           or win_vertically(matrix, coordinates_of_mark) \
           or win_diagonally(matrix, coordinates_of_mark)


# Stopping condition
def all_columns_are_taken(arr) -> bool:
    for row in arr:
        for cell in row:
            if cell == 0:
                return False
    return True


def conditions_to_stop(arr) -> bool:
    return all_columns_are_taken(arr)


# Sweep through board


def winning_message(score_of_players) -> None:
    if get_score_of_player_1(score_of_players) > get_score_of_player_2(score_of_players):
        print("Player number 1 won!")
    if get_score_of_player_1(score_of_players) < get_score_of_player_2(score_of_players):
        print("Player number 2 won!")
    else:
        print("It's a tie!")


def ending_message():
    print("end of program")


def do_you_wanna_try_again():
    global matrix
    global first_players_turn
    global continue_playing
    global try_again
    while True:
        response = input("Do you want to replay? y/n")
        if response in ["y", "Y"]:
            matrix = matrix_based_on_user_input()
            first_players_turn = True
            continue_playing = True
            break
        elif response in ["n", "N"]:
            try_again = False
            break
        else:
            print("Your inout is invalid, please try again: ")


def save_matrix(arr, scores_arr, name, first_players_turn: bool) -> None:
    import csv

    with open(f'{name}', 'w') as f:
        write = csv.writer(f)
        write.writerows(arr)
        write.writerow(scores_arr)
        write.writerow([players_turn_to_number(first_players_turn)])

    print(f"Successfully saved the metrix to the file {name}.csv")


def players_turn_to_number(first_players_turn: bool):
    if first_players_turn:
        return 1
    else:
        return 2


def players_turn_to_bool(first_players_turn: int):
    if first_players_turn == 1:
        return True
    else:
        return False


def load_matrix(name):
    import csv
    global matrix
    global scores_of_players
    global first_players_turn

    column = 0
    row = 0
    try:
        with open(f'{name}', newline='') as f:
            reader = csv.reader(f)
            matrix_file = list(reader)
        for row_list in matrix_file:
            for cell in row_list:
                matrix_file[row][column] = int(cell)
                column += 1
            column = 0
            row += 1

        first_players_turn = players_turn_to_bool(matrix_file.pop()[0])
        scores_of_players = matrix_file.pop()
        matrix = matrix_file
        print(f"Successfully loaded the metrix from file {name}.csv: ")
        display_of_the_board(matrix)
    except FileNotFoundError:
        print(f"File with the name {name}.csv was not found")


def ask_user_file_name() -> str:
    name_of_file = input("Please write the name of the file: ")
    return name_of_file


def load_matrix_from_file_using_name():
    print("Loading the file.")
    name = ask_user_file_name()
    load_matrix(name)


def save_matrix_to_file_using_name():
    global matrix
    global scores_of_players
    global first_players_turn
    print("Saving the file.")
    name = ask_user_file_name()
    save_matrix(matrix, scores_of_players, name, first_players_turn)


def scores(score_player_1, score_player_2):
    return [score_player_1, score_player_2]


def get_score_of_player_1(scores_arr):
    return scores_arr[0]


def get_score_of_player_2(scores_arr):
    return scores_arr[1]


def won_score(coordinates_of_the_mark) -> int:
    global matrix
    if win_diagonally(matrix, coordinates_of_the_mark):
        return 1
    elif win_vertically(matrix, coordinates_of_the_mark):
        return 1
    elif win_horizontally(matrix, coordinates_of_the_mark):
        return 1


def end_the_program():
    print("Ending program...")
    exit()


def game_loop():
    global continue_playing
    while continue_playing:
        users_choice: int = get_users_choice(matrix)
        users_mark: List[int] = get_the_players_mark(matrix, users_choice)
        set_the_players_mark(users_mark)
        check_for_win_combination: bool = True
        while check_for_win_combination:
            won_vertically: bool
            win_array_vertically: list
            won_vertically, win_array_vertically = win_vertically()

            won_horizontally: bool
            win_array_horizontally: list
            won_horizontally, win_array_horizontally = win_horizontally()

            won_diagonally_left: bool
            win_array_diagonally_left: list
            won_diagonally_left, win_array_diagonally_left = win_diagonally_left()

            won_diagonally_right: bool
            win_array_diagonally_right: list
            won_diagonally_right, win_array_diagonally_right = win_diagonally_right()

            win_arr: list = []
            if won_vertically:
                win_arr = win_array_vertically
            elif won_horizontally:
                win_arr = win_array_horizontally
            elif won_diagonally_left:
                win_arr = win_array_diagonally_left
            elif won_diagonally_right:
                win_arr = win_array_diagonally_right
            else:
                check_for_win_combination = False

            replace_by_winning_spot(win_arr)
            increase_score(win_arr)

            if win_arr:
                display_of_the_board(matrix)
            make_column_fall_for_all_cells()

        continue_playing = not conditions_to_stop(matrix)
        if not continue_playing:
            winning_message(scores_of_players)
            do_you_wanna_try_again()
        next_turn()

    display_of_the_board(matrix)
