def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)

        # Demande à l'utilisateur d'entrer une ligne et une colonne
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Vérification que les entrées sont dans la bonne plage
            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be between 0 and 2. Try again.")
                continue

            # Vérification si la case est déjà occupée
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place le symbole du joueur dans la case
            board[row][col] = player

            # Change de joueur
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

    # Affichage final du tableau
    print_board(board)

    # Annonce du gagnant
    winner = "O" if player == "X" else "X"
    print(f"Player {winner} wins!")

tic_tac_toe()
