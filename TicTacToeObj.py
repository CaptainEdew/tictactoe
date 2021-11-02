'''
This code is the backend side of the TicTacToe game. It creates a 2-D array
of game size 3 (regular tictactoe) with an empty space. When a user clicks
to make a move on the game board, this code checks to make sure the space has 
not yet been played, then stores the move in the array. 

This code, specifically the check_win() module, has been written to be
adaptable to larger game boards. So it is possible to make larger game boards
work with minor tweaks to the code. 
'''

class TicTacToe(object):
	def __init__(self,size):
		self.col = []
		self.x_turn = True
		self.empty = True
		self.has_won = False
		self.board_size = size

	#initializes NxN gameboard where N = board_size
	#Stores blank space in each cell
	def game_board(self):
		for num in range(self.board_size):
			#array variable to make 2D array
			array = []
			for i in range(self.board_size):
				array.append(" ")
			self.col.append(array)

	def delete_board(self):
		self.col = []
		print(self.col)

	#Resets gameboard from application via user prompt
	def reset(self,quit):
		self.has_won = False
		for col_reset in range(self.board_size):
			for row_reset in range(self.board_size):
				self.col[col_reset][row_reset] = " "
		if quit == False:
			self.x_turn = not self.x_turn
		elif quit == True:
			self.x_turn = True

	#checks if space played is empty or not
	def not_empty(self,row,column):
		if self.col[row][column] != " ":
			self.empty = False
		else:
			self.empty = True
		return self.empty

	#Gameplay: provides user input field for row and col to be played then
	#places X or O in position of user's choice. Checks for invalid input
	#and gives error if necessary.
	#Note: draw_gamepiece in the elif statement has to be the first line.
	#For some reason it does not run if it is not first. 
	def gameplay(self,x,y):

		if self.x_turn == True:
			self.col[x][y] = 'X'
			self.x_turn = False
			return (not self.x_turn)
		elif self.x_turn == False:
			self.col[x][y] = 'O'
			self.x_turn = True
			return (not self.x_turn)

	#determines the amount needed to win
	#based on the size of game board
	def winner_winner(self,x,y):
		spaces_to_win = 3
		if self.board_size < 4:
			spaces_to_win = self.board_size
		elif 4 < self.board_size < 7:
			spaces_to_win = self.board_size-1
		elif self.board_size >= 7:
			spaces_to_win = 5

		self.check_win(x,y,self.x_turn,spaces_to_win)
		return(self.has_won,self.x_turn)

	#Checks for a winner in every direction possible 
	#starting with the last move that was made by user. 
	def check_win(self,num1,num2,turn,spaces):
		winner = 1
		count = 0
		index = self.board_size-1
		spaces_down = index - num1
		spaces_up = index - spaces_down
		spaces_right = index - num2
		spaces_left = index - spaces_right

	#Checks backslash diagonal winner
		while spaces_up > 0 and spaces_left > 0:
			if self.col[num1][num2] == self.col[num1-1][num2-1]:
				winner += 1
			else:
				break
			num1 -= 1
			num2 -= 1
			count += 1
			spaces_up -= 1
			spaces_left -= 1

		if count > 0:
			num1 += count
			num2 += count
			spaces_up += count
			spaces_left += count
			count = 0

		while spaces_down > 0  and spaces_right > 0:
			if self.col[num1][num2] == self.col[num1+1][num2+1]:
				winner += 1
			else:
				break
			num1 += 1
			num2 += 1
			count += 1
			spaces_down -= 1
			spaces_right -= 1

		if count > 0:
			num1 -= count
			num2 -= count
			spaces_down += count
			spaces_right += count
			count = 0

		if winner >= spaces:
			self.has_won = True
			return self.has_won
		else:
			winner = 1

	#Checks vertical line winner
		while spaces_up > 0:
			if self.col[num1][num2] == self.col[num1-1][num2]:
				winner += 1
			else:
				break
			num1 -= 1
			spaces_up -= 1
			count += 1

		if count > 0:
			num1 += count 
			spaces_up += count
			count = 0

		while spaces_down > 0:
			if self.col[num1][num2] == self.col[num1+1][num2]:
				winner += 1
			else:
				break
			num1 += 1
			spaces_down -= 1
			count += 1

		if count > 0:
			num1 -= count
			spaces_down += count
			count = 0

		if winner >= spaces:
			self.has_won = True
			return self.has_won
		else:
			winner = 1

	#Checks forward slash diagonal line winner
		while spaces_up > 0 and spaces_right > 0:
			if self.col[num1][num2] == self.col[num1-1][num2+1]:
				winner += 1
			else:
				break
			num1 -= 1
			num2 += 1
			spaces_up -= 1
			spaces_right -= 1
			count += 1

		if count > 0:
			num1 += count
			num2 -= count
			spaces_up += count
			spaces_right += count
			count = 0

		while spaces_down > 0 and spaces_left > 0:
			if self.col[num1][num2] == self.col[num1+1][num2-1]:
				winner += 1
			else:
				break
			num1 += 1
			num2 -= 1
			spaces_down -= 1
			spaces_left -= 1
			count += 1

		if count > 0:
			num1 -= count
			num2 += count
			spaces_down += count
			spaces_left += count
			count = 0

		if winner >= spaces:
			self.has_won = True
			return self.has_won
		else:
			winner = 1

	#Checks horizontal winner
		while spaces_left > 0:
			if self.col[num1][num2] == self.col[num1][num2-1]:
				winner += 1
			else:
				break
			num2 -= 1
			spaces_left -= 1
			count += 1

		if count > 0:
			num2 += count
			spaces_left += count
			count = 0

		while spaces_right > 0:
			if self.col[num1][num2] == self.col[num1][num2+1]:
				winner += 1
			else:
				break
			num2 += 1
			spaces_right -= 1
			count += 1

		if count > 0:
			num2 -= count
			spaces_right += count
			count = 0

		if winner >= spaces:
			self.has_won = True
			return self.has_won
		else:
			winner = 1