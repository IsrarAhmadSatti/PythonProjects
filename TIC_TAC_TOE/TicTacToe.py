#  TIC TAC TOE GAME
print("\n\t\tWelcome to Tic Tac Toe game:" )
print("\tYou will enter your move starting from 1  and ending at 9")
print("\t1 being the first entry on the board and 9 being the last\n")

check=' '
board=[]
for row in range(3):
    box = [check for col in range(3)]
    board.append(box)

def display_board(board):
    # The function accepts one parameter containing the board's current status
    print('+-------+-------+-------+')
    for i in range(len(board)):
        for j in range(len(board[i])):
            print('|  ',board[i][j], end='   ') 
        print('|\n+-------+-------+-------+')
    return board          # and prints it out to the console.

def enter_move(board):
    # the function accepts the board's current status, asks the user about their move,
    new_move=int(input('Enter your move:   '))
    if 1 <= new_move <= 9:
        new_move -= 1 # as our array starts from 0 and end at 8 so 1 less then the user input
        row = new_move // 3  # determining row
        col = new_move % 3   #determinig column
        if board[row][col] == " ": #updating the board if it has empty field selected by user
            board[row][col] = "O"
        else:
            print('Invalid move\n') # if user chooses invalid field ask again
            enter_move(board)
    else:
        print('Invalid move\n')
        enter_move(board)

def draw_move(board):
    import random
    comp_move = random.randint(0,8) #generating random number for computers move
    row = comp_move // 3
    col = comp_move % 3
    if board[row][col] == " ": # if the field is empty at the location
        board[row][col] = "X"  # updated with computer move
    else:                      # else regenrate the number
        draw_move(board)               
    return board

def make_list_of_free_fields(board):
	free = []	# the list is empty initially
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in ['O','X']: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free #the list consists of tuples, while each tuple is a pair of row and column numbers. 

def victory_for(board):
    for i in range(3):
        #horizontal Check
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            return 'You WIN!'
        elif board[i][0] == board[i][1] == board[i][2] == 'X':
            return 'You LOSE!'
        #vertical Check
        elif board[0][i] == board[1][i] == board[2][i] == 'O':
            return 'You WIN!'
        elif board[0][i] == board[1][i] == board[2][i] == 'X':
            return 'You LOSE!'
        #diagnol checks
        elif board[0][0] == board[1][1] == board[2][2] == 'O':
            return 'You WIN!'
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            return 'You WIN!'
        elif board[0][0] == board[1][1] == board[2][2] == 'X':
            return 'You LOSE!'
        elif board[0][2] == board[1][1] == board[2][0] == 'X':
            return 'You LOSE!'
    # Check for draw
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'It\'s a DRAW!!!!'
    return False

while make_list_of_free_fields(board) != []:# looping until someone wins or fields are occupied
    draw_move(board)    # getting move from computer
    display_board(board)
    result = victory_for(board) # Checking for victory
    if result:
        print("Game Over",result)
        break
    enter_move(board)               # Getting move from user
    result = victory_for(board)     # Checking for victory
    if result:
        display_board(board)
        print("Game Over",result)   #displaying result
        break  