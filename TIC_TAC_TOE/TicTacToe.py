
check=' '
board=[]
for row in range(3):
    box = [check for col in range(3)]
    board.append(box)

def display_board(board):
    print('+-------+-------+-------+')
    for i in range(len(board)):
        for j in range(len(board[i])):
            print('|  ',board[i][j], end='   ') # The function accepts one parameter containing the board's current status
        print('|\n+-------+-------+-------+')
    return board          # and prints it out to the console.

def enter_move(board):
    
    new_move=int(input('Enter your move:   '))
    if 0 <= new_move < 9 and new_move != 4:
        row = new_move // 3  # the function accepts the board's current status, asks the user about their move,
        col = new_move % 3
        board[row][col] = "O"
    else:
        print('Invalid move\n')
        enter_move(board)
        
def make_list_of_free_fields(board):
	free = []	# the list is empty initially
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in ['O','X']: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free                  #the list consists of tuples, while each tuple is a pair of row and column numbers. 

def victory_for(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            return 'You WIN!'
        elif board[0][i] == board[1][i] == board[2][i] == 'O':
            return 'You WIN!'
        elif board[0][0] == board[1][1] == board[2][2] == 'O':
            return 'You WIN!'
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            return 'You WIN!'
        elif board[i][0] == board[i][1] == board[i][2] == 'X':
            return 'You LOSE!'
        elif board[0][i] == board[1][i] == board[2][i] == 'X':
            return 'You LOSE!'
        elif board[0][0] == board[1][1] == board[2][2] == 'X':
            return 'You LOSE!'
        elif board[0][2] == board[1][1] == board[2][0] == 'X':
            return 'You LOSE!'
    # Check for draw
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'It\'s a DRAW!!!!'
    return False
    
def draw_move(board):
    import random
    comp_move = random.randint(0,8)
    row = comp_move // 3
    col = comp_move % 3
    if board[row][col] == " ":
        board[row][col] = "X"
    else:
        draw_move(board)               
    return board

print("\n\t\tWelcome to Tic Tac Toe game:" )
print("You will enter your move starting from 0  and ending at 8")
print("0 being the first entry on the board and 8 being the last")
print("Enter 1 to play game: " )
get_move=int(input('=> '))
if get_move == 1:
    board[1][1]='X'
else:
    print("\n\t\tWelcome to Tic Tac Toe game: \n \tEnter 1 to play game: " )
    get_move = int(input('\t=>'))
    board[1][1] = 'X'
display_board(board)

while make_list_of_free_fields(board) != []:
    enter_move(board)
    # display_board(board)
    result = victory_for(board)
    if result:
        print("Game Over",result)
        break
    draw_move(board)
    display_board(board)
    result = victory_for(board)
    if result:
        print("Game Over",result)
        break
    