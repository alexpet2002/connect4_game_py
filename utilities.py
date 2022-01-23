# Global metavlhtes
from typing import List, Tuple

first_players_turn: bool = True
continue_playing: bool = True
try_again: bool = True
matrix: List[List[int]] = []
scores_of_players: List[int] = []


# Synarthseis
# Dhmiourgia Pinaka
def get_matrix_based_on_number_rows_and_columns(columns: int = 5, rows: int = 5) -> List[List[int]]:
    """
    Επιστρέφει τον πίνακα τιμών με μέγεθος βασισμένο στις επιλογές του χρήστη.
    @param columns: int
    @param rows: int
    @return: List[List[int]]

    """
    return [[0 for x in range(columns)] for y in range(rows)]


def size_of_the_array() -> int:
    """
    Επιστρέφει τον αριθμό στηλών που επιθυμεί ο χρήστης να υπάρχουν στον πίνακα του.
    Εάν ο χρήστης δεν εισάγει αριθμό, ο προκαθορισμένος αριθμός στηλών είναι 5.
    @return: int

    """
    while True:
        print(f"Καλωσήλθατε στο παιχνίδι!")
        size = input("Δώστε αριθμό στηλών παιχνιδιού (5-10): ")
        if size in ["5", "6", "7", "8", "9", "10"]:
            return int(size)
        elif size == "":
            print("Προκαθορισμένος αριθμός στηλών : 5")
            return 5
        else:
            print("Δοκιμάστε ξανά.")


def intialize_matrix() -> None:
    """
    Εμφανίζει τον πίνακα ανάλογα με την επιλογή του παίκτη.

    """
    global matrix
    global scores_of_players
    while True:
        choice = input("Επιθυμείτε νέο παιχνίδι(N) ή φόρτωση παιχνιδιού από αρχείο(L); ")
        if choice in ["N", "n", "ν", "Ν"]:
            matrix = matrix_based_on_user_input()
            break
        elif choice in ["L", "l", "Λ", "λ"]:
            load_matrix_from_file_using_name()
            break
        else:
            print("Δοκιμάστε ξανά.")


def matrix_based_on_user_input() -> List[List[int]]:
    """
    Επιστρέφει τον πίνακα βάσει του αριθμού που εισάγει ο χρήστης.
    @rtype: List[List[int]]
    @return: list
    """
    size = size_of_the_array()
    return get_matrix_based_on_number_rows_and_columns(size, size)


# Apeikonisi tou pinaka
def display_of_the_board(arr) -> None:
    """
    Απεικόνιση του πίνακα με αριθμημένες στήλες και γραμμές.
    @param arr: list
    """
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
                print("O", end="")
            elif cell == 2:
                print("X", end="")
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


# Allagh seiras

def next_turn() -> None:
    """
    Αλλάζει τν σειρά των παίκτων.

    """
    global first_players_turn
    first_players_turn = not first_players_turn


# Users choices
def ask_user_to_input_a_column(arr) -> int:
    """
    Ζητάει από τον χρήστη να εισάγει τον αριθμό στήλης στην οποία επιθυμεί να εισάγει το πιόνι του.
    Αλλιώς, αν επιθυμεί να αποθηκεύσει το παιχνίδι ή να αρχίσει καινούριο ή να φορτώσει άλλο αρχείο ή να τελειώσει το
    παιχνίδι.
    @param arr: list
    @return: int

    """
    while True:
        display_of_the_board(arr)
        length_of_array = len(arr)
        user_choice = input(
            f"Παρακαλώ επιλέξτε στήλη από 1-{length_of_array}, πατήστε S για να αποθηκεύσετε το αρχείο, N για να αρχίσετε νέο παιχνίδι, L για "
            f" φορτώση παιχνίδιου ή E για να τερματίσετε το παιχνίδι: ")
        if user_choice in ["S", "s", "Σ", "σ"]:
            # apothikevsi paixnidiou
            save_matrix_to_file_using_name()
        elif user_choice in ["E", "e", "ε", "Ε"]:
            # termatismos paixnidiou
            print("Chosen E,")
            end_the_program()
        elif user_choice in ["N", "n", "Ν", "ν"]:
            # neo paixnidi
            intialize_matrix()
        elif user_choice in ["L", "l", "λ", "Λ"]:
            # Fortosh paixnidiou
            load_matrix_from_file_using_name()
        elif user_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            if int(int(user_choice) <= length_of_array) and not choice_out_of_bounds(arr, int(user_choice) - 1):
                return int(user_choice)
            print(f"Ο αριθμός είναι εκτός των ορίων του ταμπλώ, Δοκιμάστε ξανά.")
        else:
            print(f"Δοκιμάστε ξανά.")


def convert_the_user_input_to_choice(arr) -> int:
    """
    Μετατρέπει την επιλογή στήλης του παίκτη.
    Αφαιρεί μια μονάδα από τον αριθμό που έχει εισάγει ο χρήστης έτσι ώστε να αντιστοιχεί στην
    πραγματική τοποθεσία πιονιού.
    @param arr: list
    @return: int

    """
    return ask_user_to_input_a_column(arr) - 1


def choice_out_of_bounds(arr, choice) -> bool:
    """
    Ελέγχει εάν υπάρχουν διαθέσιμες θέσεις στην στήλη που έχει επιλέξει ο χρήστης.
    @param arr: list
    @param choice: int
    @return: bool

    """
    if arr[0][choice] != 0:
        return True
    else:
        return False


def get_users_choice(arr) -> int:
    """
    Επιστρέφει
    @param arr: list
    @return:

    """
    return convert_the_user_input_to_choice(arr=arr)


# Orismos tou pioniou
def mark(row, column) -> List[int]:
    """
    Επιστρέφει την λίστα με τις συντεταγμένες του πιονιού.
    @param row: int
    @param column: int
    @return: List[int]

    """
    return [row, column]


def get_marks_column(mk) -> int:
    """
    Επιστρέφει την 2η θέση της λίστας με τις συντεταγμένες του πιονιού, δηλαδή την αντίστοιχη στήλη.
    @param mk: list
    @return: int

    """
    return mk[1]


def get_marks_row(mk) -> int:
    """
    Επιστρέφει την 1η θέση της λίστας με τις συντεταγμένες του πιονιού, δηλαδή την αντίστοιχη γραμμή.
    @param mk: list
    @return: int

    """
    return mk[0]


def get_the_players_mark(arr, column) -> List[int]:
    """
    Ελέγχει τη διαθεσιμότητα θέσεων στην στήλη που επέλεξε ο χρήστης.
    Επιστρέφει τις συντεταγμένες της πρώτης διαθέσιμης θέσης.
    @param arr: array
    @param column: int
    @return: List[int]

    """
    number_of_rows = len(arr)
    for row_index in range(number_of_rows - 1):
        if arr[row_index + 1][column] != 0:
            return mark(row_index, column)
    return mark(number_of_rows - 1, column)


def set_the_players_mark(coordinates_of_mark: List[int]) -> None:
    """
    Εισάγει τον αριθμό 1 ή 2 ανάλογα με την σειρά του παίκτη στην διαθέσιμη θέση.
    Χρησιμοποιεί την 'global matrix' και την global 'first_players_turn'.
    @param coordinates_of_mark: List[int]

    """
    global matrix
    global first_players_turn
    if first_players_turn:
        matrix[get_marks_row(coordinates_of_mark)][get_marks_column(coordinates_of_mark)] = 1
    else:
        matrix[get_marks_row(coordinates_of_mark)][get_marks_column(coordinates_of_mark)] = 2


# def win_array
def win_array(players_number: int = -1, coordinates: object = None) -> list:
    """
    Επιστρέφει λίστα με πρώτο στοιχείο τον αριθμό του παίκτη και δεύτερο στοιχείο την λίστα με τις συντεταγμένες.
    @param players_number: int
    @param coordinates: None
    @return: list

    """
    if coordinates is None:
        coordinates = []
    return [players_number, coordinates]


def get_win_array_player(win_arr: list) -> bool:
    """
    Επιστρέφει την πρώτη θέση της λίστας, δηλαδή τον αριθμό του παίκτη.
    @param win_arr: list
    @return: bool
    """
    return win_arr[0]


def get_win_array_coordinates(win_arr: list) -> list:
    """
    Επιστρέφει την δεύτερη θέση της λίστας, δηλαδή τις συντεταγμένες του παίκτη.
    @param win_arr: list
    @return: list
    """
    return win_arr[1]


# def of win coord

def winning_coordinates(row: int, column: int) -> List[int]:
    """
    Επιστρέφει την λίστα με τις συντεταγμένες του πιονιού.
    @param row: int
    @param column: int
    @return: List[int]

    """
    return [row, column]


def get_winning_coordinates_row(arr) -> int:
    """
    Επιστρέφει την πρώτη θέση της λίστας με τις συντεταγμένες του πιονιού, δηλαδή την αντίστοιχη γραμμή.
    @param arr: list
    @return: int

    """
    return arr[0]


def get_winning_coordinates_column(arr) -> int:
    """
    Επιστρέφει την δεύτερη θέση της λίστας με τις συντεταγμένες του πιονιού, δηλαδή την αντίστοιχη στήλη.
    @param arr: list
    @return: int

    """
    return arr[1]


# Proipothesis gia niki
def win_horizontally() -> Tuple[bool, list]:
    """
    Ελέγχει αν ο παίκτης συμπλήρωσε τετράδα με τα πιόνια του οριζόντια.
    Επιστρέφει την λίστα με την πρώτη θέση να είναι ο αριθμός του παίκτη.
    Η δεύτερη θέση αντιστοιχεί όλες τις συντεταγμένες των πιονιών του παίκτη που κέρδισε οριζόντια.
    @return: Tuple[bool, list]

    """
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
    """
    Προσθέτει την βαθμολογία στον παίκτη.
    @param score_to_add: List[int]
    @param which_player: int
    """
    global scores_of_players
    if which_player == 1:
        scores_of_players[0] = scores_of_players[0] + score_to_add
    else:
        scores_of_players[1] = scores_of_players[1] + score_to_add


def increase_score(win_array):
    """
    Προσθέτει την βαθμολογία στον παίκτη που κέρδισε.
    @param win_array:
    """
    global scores_of_players
    if win_array:
        players_number = get_win_array_player(win_array)
        add_score_to_player(1, players_number)


def show_score():
    """
    Δείχνει την βαθμολογία του κάθε παίκτη.

    """
    global scores_of_players
    global first_players_turn
    print(
        f"Βαθμολογία του παίκτη 1: {scores_of_players[0]}, Βαθμολογία του παίκτη 2: {scores_of_players[1]}. Είναι η σειρά του παίκτη {players_turn_to_number(first_players_turn)} .")


# def won_spot()

def replace_by_winning_spot(win_array: List) -> None:
    """
    Αντικαθιστά τους αριθμούς 1,2 των πιονιών στον πίνακα με 3,4 αντίστοιχα, εφόσον ο παίκτης έχει
    συμπληρώσει 4 συνεχόμενα πιόνια.
    @param win_array: list

    """
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
    """
    Αντικαθιστά το πιόνια του νικητή με αυτά που βρίσκονται από πάνω.
    @param row: int
    @param column: int
    """
    global matrix
    if matrix[row][column] == 3 or matrix[row][column] == 4:
        for r in range(row, 0, -1):
            matrix[r][column] = matrix[r - 1][column]
        matrix[0][column] = 0


def make_column_fall_for_all_cells():
    """
    Αντικαθιστά το πιόνια του νικητή με αυτά που βρίσκονται από πάνω,
    εφαρμόζοντας ελέγχο σε ολόκληρο τον πίνακα.

    """
    global matrix
    length_array = len(matrix)
    for r in range(length_array):
        for c in range(length_array):
            make_column_fall(r, c)


def vertically_out_of_bounds(row: int, arr: List[List[int]]) -> bool:
    return True if row <= len(arr) - 4 else False


def win_vertically() -> Tuple[bool, list]:
    """
    Ελέγχει εάν ο παίκτης έχει συμπληρώσει τουλάχιστον 4 πιόνια κάθετα.
    @return: Tuple[bool, list]
    """
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
    """
    Ελέγχει εάν ο παίκτης έχει συμπληρώσει τουλάχιστον 4 πιόνια διαγώνια από την αριστερή κατεύθυνση.
    @return: Tuple[bool, list]

    """
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
    """
    Ελέγχει εάν ο παίκτης έχει συμπληρώσει τουλάχιστον 4 πιόνια διαγώνια από την δεξιά κατεύθυνση.
    @return: Tuple[bool, list]

    """
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


# Synthikes gia termatismo paixnidiou
def all_columns_are_taken(arr) -> bool:
    """
    Ελέγχει εάν δεν υπάρχουν διαθέσιμες θέσεις στον πίνακα.
    @param arr: list
    @return: bool
    """
    for row in arr:
        for cell in row:
            if cell == 0:
                return False
    return True


def conditions_to_stop(arr) -> bool:
    """
    Επιστρέφει 'True' εαν η ο πίνακας δεν έχει διαθέσιμες θέσεις.

    @param arr: list
    @return: bool
    """
    return all_columns_are_taken(arr)


# Eleghos olou tou pinaka


def winning_message(score_of_players) -> None:
    """
    Εμφανίζει μήνυμα με την ανακοίνωση του νικητή.
    @param score_of_players: int
    """
    if get_score_of_player_1(score_of_players) > get_score_of_player_2(score_of_players):
        print("Ο παίκτης 1 είναι νικητής!")
    if get_score_of_player_1(score_of_players) < get_score_of_player_2(score_of_players):
        print("Ο παίκτης 2 είναι νικητής!")
    else:
        print("Ισοπαλία!")


def ending_message():
    """
    Εμφανίζει μήνυμα με την ανακοίνωση του τέλους του προγράμματος.

    """
    print("τέλος προγράμματος")


def do_you_wanna_try_again():
    """
    Εμφανίζει μήνυμα και ελέγχει εάν ο παίκτης επιθυμεί να συνεχίσει το παιχνίδι.


    """
    global matrix
    global first_players_turn
    global continue_playing
    global try_again
    while True:
        response = input("θέλετε να παίξετε ξανά; y/n")
        if response in ["y", "Y", "υ", "Υ"]:
            matrix = matrix_based_on_user_input()
            first_players_turn = True
            continue_playing = True
            break
        elif response in ["n", "N", "ν", "Ν"]:
            try_again = False
            break
        else:
            print("Δοκίμαστε ξανά: ")


def save_matrix(arr, scores_arr, name, first_players_turn: bool) -> None:
    """
    Αποθήκευση του αρχείου ως αρχείο 'csv'.
    @param arr: list
    @param scores_arr: list
    @param name: str
    @param first_players_turn: bool
    """
    import csv

    with open(f'{name}', 'w') as f:
        write = csv.writer(f)
        write.writerows(arr)
        write.writerow(scores_arr)
        write.writerow([players_turn_to_number(first_players_turn)])

    print(f"Το παιχνίδι αποθηκεύτηκε με επιτυχία στο αρχείο {name}.csv")


def players_turn_to_number(first_players_turn: bool):
    """
    Μετατρέπει την σειρά του παίκτη σε αριθμό.
    @param first_players_turn: bool
    @return: int
    """
    if first_players_turn:
        return 1
    else:
        return 2


def players_turn_to_bool(first_players_turn: int):
    """
    Μετατρέπει την σειρά του παίκτη σε 'bool' .
    @param first_players_turn: int
    @return: bool
    """
    if first_players_turn == 1:
        return True
    else:
        return False


def load_matrix(name):
    """
    Φορτώνει το αρχείο με το παιχνίδι
    @param name: str

    """
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
        print(f"Η φόρτωση του παιχνιδιού έγινε με επιτυχία από το αρχείο{name}.csv: ")
        display_of_the_board(matrix)
    except FileNotFoundError:
        print(f"Το αρχείο με το όνομα {name}.csv δεν υπάρχει")


def ask_user_file_name() -> str:
    """

    @return: str
    """
    name_of_file = input("Παρακαλώ, εισάγετε το όνομα του αρχείου: ")
    return name_of_file


def load_matrix_from_file_using_name():
    """

    """
    print("Φόρτωση αρχείου..")
    name = ask_user_file_name()
    load_matrix(name)


def save_matrix_to_file_using_name():
    """

    """
    global matrix
    global scores_of_players
    global first_players_turn
    print("Αποθήκευση αρχείου.")
    name = ask_user_file_name()
    save_matrix(matrix, scores_of_players, name, first_players_turn)


def scores(score_player_1, score_player_2) -> list:
    """
    Επιστρέφει λίστα με βαθμολογίες των παίκτων
    @param score_player_1:int
    @param score_player_2: int
    @return: list

    """
    return [score_player_1, score_player_2]


def get_score_of_player_1(scores_arr):
    """
    Επιστρέφει την πρώτη θέση της λίστας, δηλαδή την βαθμολογία του παίκτη 1.
    @param scores_arr:
    @return:

    """
    return scores_arr[0]


def get_score_of_player_2(scores_arr):
    """
    Επιστρέφει την δεύτερη θέση της λίστας, δηλαδή την βαθμολογία του παίκτη 2.
    @param scores_arr:
    @return:

    """
    return scores_arr[1]


def end_the_program():
    """
    Εμφανίζει μήνυμα για τερματισμό προγράμματος.

    """
    print("Τερματισμός προγράμματος...")
    exit()


def game_loop():
    """
    Υποστηρίζει την διεξαγωγή πολλαπλών γύρων του παιχνιδιού.

    """
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
