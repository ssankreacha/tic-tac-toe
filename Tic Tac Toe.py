import random

row_1 = [" ", " ", " "]; row_2 = [" ", " ", " "]; row_3 = [" ", " ", " "]


# Function - Presents Current Game Grid
def current_grid():
    print(row_1), print(row_2), print(row_3)


def is_draw():
    return all(cell != " " for row in [row_1, row_2, row_3] for cell in row)

# Game Begins
the_game_is_on = True

# While the_game_is_on...
while the_game_is_on:
    user_choice = input("\n⚠️ The Game Will Now Begin!\n What Do You Choose 'x' or 'o' ?:  ").upper()

    # Any Letter Except 'X' and 'O' Sends An Error Message!
    if user_choice != "X" and user_choice != "O":
        print("⛔ You chose incorrectly! Please Try Again! ")

    # USER CHOOSES ✖️ ---- PART 1️
    elif user_choice == "X":
        computer_choice = "O"
        print("Computer Chooses: " + computer_choice)

        # Choose Row & Column ---- User & Computer
        while True:
            # User Chooses Row & Column...
            user_row_number = int(input("Please Choose A Row Number Between 1 - 3: ")) - 1
            user_column_number = int(input("Please Choose A Column Between 1 - 3: ")) - 1

            # Numbers Must Be Between 0 and 2 (1 - 3)
            if user_row_number < 0 or user_row_number > 2 or user_column_number < 0 or user_column_number > 2:
                print("⛔ No Such Row or Column Exists, Please Try Again! ")

            # Otherwise, Game Continues...
            else:
                # USER ---- Add 'X' To A Position On The Grid
                if user_row_number == 0 and row_1[user_column_number] == " ": row_1[user_column_number] = user_choice
                elif user_row_number == 1 and row_2[user_column_number] == " ": row_2[user_column_number] = user_choice
                elif user_row_number == 2 and row_3[user_column_number] == " ": row_3[user_column_number] = user_choice
                else:
                    print("⛔ Space Is Allocated, Try Again! "); continue

                # COMPUTER ---- Add 'O' To A Position On The Grid
                while True:
                    computer_row_number = random.randint(0, 2); computer_column_number = random.randint(0, 2)

                    if computer_row_number == 0 and row_1[computer_column_number] == " ":
                        row_1[computer_column_number] = computer_choice
                        break
                    elif computer_row_number == 1 and row_2[computer_column_number] == " ":
                        row_2[computer_column_number] = computer_choice
                        break
                    elif computer_row_number == 2 and row_3[computer_column_number] == " ":
                        row_3[computer_column_number] = computer_choice
                        break

                # Show current_grid()
                current_grid()

                # Check Horizontal Wins
                winner_found = False
                for row in [row_1, row_2, row_3]:
                    if row.count(user_choice) == 3: print("User Has Won!"); winner_found = True; exit()
                    elif row.count(computer_choice) == 3: print("Computer Has Won!"); winner_found = True; exit()

                # Check Vertical Wins using zip
                for col in zip(row_1, row_2, row_3):  # zip groups columns together
                    if list(col).count(user_choice) == 3: print("User Has Won! "); exit()
                    elif list(col).count(computer_choice) == 3: print("Computer Has Won! "); exit()

                # Diagonal Checks
                if row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X": print("User Wins! "); exit()
                if row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X": print("User Wins! "); exit()
                elif row_1[0] == "O" and row_2[1] == "O" and row_3[2] == "O": print("Computer Wins! "); exit()
                elif row_1[2] == "O" and row_2[1] == "O" and row_3[0] == "O": print("Computer Wins! "); exit()

                # Check For Draw
                if is_draw(): print("The Game Ended In A Draw!"); exit()

    # USER CHOOSES O ---- PART 2
    elif user_choice == "O":
        computer_choice = "X"
        print("Computer Chooses: " + computer_choice)

        # Choose Row & Column ---- User & Computer
        while True:
            # User Chooses Row & Column...
            user_row_number = int(input("Please Choose A Row Number Between 1 - 3: ")) - 1
            user_column_number = int(input("Please Choose A Column Between 1 - 3: ")) - 1

            # Numbers Must Be Between 0 and 2 (1 - 3)
            if user_row_number < 0 or user_row_number > 2 or user_column_number < 0 or user_column_number > 2:
                print("⛔ No Such Row or Column Exists, Please Try Again! ")

            # Otherwise, Game Continues...
            else:
                # USER ---- Add 'X' To A Position On The Grid
                if user_row_number == 0 and row_1[user_column_number] == " ": row_1[user_column_number] = user_choice
                elif user_row_number == 1 and row_2[user_column_number] == " ": row_2[user_column_number] = user_choice
                elif user_row_number == 2 and row_3[user_column_number] == " ": row_3[user_column_number] = user_choice
                else:
                    print("⛔ Space Is Allocated, Try Again! "); continue

                # COMPUTER ---- Add 'O' To A Position On The Grid
                while True:
                    computer_row_number = random.randint(0, 2); computer_column_number = random.randint(0, 2)

                    if computer_row_number == 0 and row_1[computer_column_number] == " ":
                        row_1[computer_column_number] = computer_choice
                        break
                    elif computer_row_number == 1 and row_2[computer_column_number] == " ":
                        row_2[computer_column_number] = computer_choice
                        break
                    elif computer_row_number == 2 and row_3[computer_column_number] == " ":
                        row_3[computer_column_number] = computer_choice
                        break

                # Show current_grid()
                current_grid()

                # Check Horizontal Wins
                winner_found = False
                for row in [row_1, row_2, row_3]:
                    if row.count(user_choice) == 3: print("User Has Won!"); winner_found = True; exit()
                    elif row.count(computer_choice) == 3: print("Computer Has Won!"); winner_found = True; exit()

                # Check Vertical Wins using zip
                for col in zip(row_1, row_2, row_3):  # zip groups columns together
                    if list(col).count(user_choice) == 3: print("User Has Won! "); exit()
                    elif list(col).count(computer_choice) == 3: print("Computer Has Won! "); exit()

                # Diagonal Checks
                if row_1[0] == "O" and row_2[1] == "O" and row_3[2] == "O": print("User Wins! "); exit()
                if row_1[2] == "O" and row_2[1] == "O" and row_3[0] == "O": print("User Wins! "); exit()
                elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X": print("Computer Wins! "); exit()
                elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X": print("Computer Wins! "); exit()

                # Check For Draw
                if is_draw(): print("The Game Ended In A Draw!"); exit()
