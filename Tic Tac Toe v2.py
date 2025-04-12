import random

row_1 = [" ", " ", " "]; row_2 = [" ", " ", " "]; row_3 = [" ", " ", " "]


def current_grid():
    print(row_1); print(row_2); print(row_3)


def check_winner():
    # Horizontal check
    for row in [row_1, row_2, row_3]:
        if row.count("X") == 3:
            return "User"
        elif row.count("O") == 3:
            return "Computer"

    # Vertical check
    for col in zip(row_1, row_2, row_3):
        if list(col).count("X") == 3:
            return "User"
        elif list(col).count("O") == 3:
            return "Computer"

    # Diagonal check
    if row_1[0] == row_2[1] == row_3[2] != " ":
        return "User" if row_1[0] == "X" else "Computer"
    if row_1[2] == row_2[1] == row_3[0] != " ":
        return "User" if row_1[2] == "X" else "Computer"

    return None

def is_draw():
    return all(cell != " " for row in [row_1, row_2, row_3] for cell in row)

the_game_is_on = True
print("\n⚠️ Please Choose A Letter. You CANNOT Change This Letter.\n\nThe Game Will Then Begin!\n ")

while the_game_is_on:
    user_choice = input("What Do You Choose 'x' or 'o' ?:  ").upper()
    if user_choice not in ["X", "O"]:
        print("⛔ You chose incorrectly! Please Try Again! ")
        continue

    computer_choice = "O" if user_choice == "X" else "X"
    print("Computer Chooses: " + computer_choice)

    while True:
        current_grid()

        # USER TURN
        while True:
            try:
                user_row_number = int(input("Please Choose A Row Number Between 1 - 3: ")) - 1
                user_column_number = int(input("Please Choose A Column Between 1 - 3: ")) - 1
                if not (0 <= user_row_number <= 2 and 0 <= user_column_number <= 2):
                    print("⛔ Invalid input. Try again!")
                    continue

                if [row_1, row_2, row_3][user_row_number][user_column_number] == " ":
                    [row_1, row_2, row_3][user_row_number][user_column_number] = user_choice
                    break
                else:
                    print("⛔ That space is already taken. Try again!")
            except ValueError:
                print("⛔ Please enter valid numbers!")

        # CHECK WINNER / DRAW AFTER USER TURN
        winner = check_winner()
        if winner:
            current_grid()
            print(f"{winner} has won the game!")
            the_game_is_on = False
            break
        elif is_draw():
            current_grid()
            print("The game ended in a draw!")
            the_game_is_on = False
            break

        # COMPUTER TURN
        while True:
            comp_row = random.randint(0, 2)
            comp_col = random.randint(0, 2)
            if [row_1, row_2, row_3][comp_row][comp_col] == " ":
                [row_1, row_2, row_3][comp_row][comp_col] = computer_choice
                print(f"Computer placed {computer_choice} at ({comp_row + 1}, {comp_col + 1})")
                break

        # CHECK WINNER / DRAW AFTER COMPUTER TURN
        winner = check_winner()
        if winner:
            current_grid()
            print(f"{winner} has won the game!")
            the_game_is_on = False
            break
        elif is_draw():
            current_grid()
            print("The game ended in a draw!")
            the_game_is_on = False
            break

    break  # Remove if you want to allow repeated games
