#This is a game
print("\tWELCOME TO TICTACTOE GAME")
print("\tYou Are Playing against computer")
print("\tEnter a number between 1 to 9 for your move\n")

board = []
check = ' '
for i in range(3):
    row = [check for i in range(3)]
    board.append(row) # making 3 x 3 board
    
def display_board(board):
    print("+---+---+---+")
    for i in range(len(board)):
        for j in range(len(board[i])):      
            print("|",board[i][j],end = ' ')
        print("|\n+---+---+---+")
           
def enter_move(board):
    try:
        move = int(input("\tEnter your move: "))
        if 1 < move >9:
            print("Enter number between 1 and 9: ")
            enter_move(board)
        else:
            move = move - 1
            row = move // 3
            col = move % 3
            if board[row][col] == ' ':
                board[row][col] = 'O'
            else:
                print("Invalid Move!!!!")
                enter_move(board)
    except ValueError:
        print("Invalid option try again")
        enter_move(board)
    return board

def draw_move(board):
    import random
    move = 0
    for i in range(3):
        if move < 1:
            if board[i][0] == board[i][1] == "O" and board[i][2] == " ":
                board[i][2] = "X"
                move += 1
            elif board[i][0] == board[i][2] == "O" and board[i][1] == " ":
                board[i][1] = "X"
                move += 1
            elif board[i][1] == board[i][2] == "O" and board[i][0] == " ":
                board[i][0] = "X"
                move += 1
            elif board[0][i] == board[1][i] == "O" and board[2][i] == " ":
                board[2][i] = "X"
                move += 1
            elif board[0][i] == board[2][i] == "O" and board[1][i] == " ":
                board[1][i] = "X"
                move += 1
            elif board[2][i] == board[1][i] == "O" and board[0][i] == " ":
                board[0][i] = "X"
                move += 1
                
            elif board[0][0] == board[1][1] == "X" and board[2][2] == " ":
                board[2][2] = "X"
                move += 1
            elif board[0][0] == board[2][2] == "X" and board[1][1] == " ":
                board[1][1] = "X"
                move += 1
            elif board[2][2] == board[1][1] == "X" and board[0][0] == " ":
                board[0][0] = "X"
                move += 1
            elif board[0][2] == board[1][1] == "X" and board[2][0] == " ":
                board[2][0] = "X"
                move += 1
            elif board[2][0] == board[1][1] == "X" and board[0][2] == " ":
                board[0][2] = "X"
                move += 1
            elif board[2][0] == board[0][2] == "X" and board[1][1] == " ":
                board[1][1] = "X"
                move += 1

    if move < 1:
        move = random.randint(1,9)
        move = move - 1
        row = move // 3
        col = move % 3
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            draw_move(board)
    return board

def victory_for(board):
    for i in range(3):
        #horizontal checks           
        if board[i][0] == board[i][1] == board[i][2] == "O":
            return "You WIN"
        elif board[i][0] == board[i][1] == board[i][2] == "X":
            return "You LOSE"
        #vertical checks
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return "You WIN"
        elif board[0][i] == board[1][i] == board[2][i] == "X":
            return "You LOSE"
        #Diagonal Checks
        elif board[0][0] == board[1][1] == board[2][2] == "O":
            return "You WIN"
        elif board[0][2] == board[1][1] == board[2][0] == "O":
            return "You WIN"
        elif board[0][0] == board[1][1] == board[2][2] == "X":
            return "You LOSE"
        elif board[0][2] == board[1][1] == board[2][0] == "X":
            return "You LOSE"
        elif list_free_fields(board) == []:
            return "DRAW!!!"
    return False

def list_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O","X"]: #checking if a field is empty
                free.append((row,col))  #appending free fields in free array
    return free

def restart(board): #restarts the board by clearing all the fields 
    for i in range(3):
        for j in range(3):
            board[i][j] = " " #replacing allthe "X" and "O" with spaces
    return board
            
def main():
    
    board[1][1] = "X" #initializing board with a computer move
    display_board(board)
    while list_free_fields(board) != []: #iterating until there are no free fields left
        enter_move(board)
        result = victory_for(board) #checking if victory fields are filled
        if result:
            display_board(board)
            print("\tGame over!!!", result)
            break
        draw_move(board)
        display_board(board)
        result = victory_for(board)
        if result:
            print("\tGame over!!!", result)
            break
        
main()
while True:
    cont = input("\nPlay Again---> Yes[y] or No[n]: ")
    if cont in ["Y","y","yes","YES"]:
        restart(board)
        main()
    else:
        break

print("\n\tThank you for playing Tic Tac Toe")

