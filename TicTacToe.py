#!/usr/bin/env python
"""*******************************************************
TicTacToe.py
Andrew Vaz (andrewvaz.89@gmail.com)
October 1, 2019, modified May 27, 2020

Tic Tac Toe game with options for bigger game boards.
The bigger game boards are not as fun and easier to win/
harder to defend. This was to test my skills with 2D 
arrays and python in general. Very fun and will continue
to develop ways to make the larger game boards more
interesting. Hope you enjoy! :)

*******************************************************"""

import pygame, sys
from pygame.locals import *
from TicTacToeObj import TicTacToe

#Pygame and window initialization
pygame.init()
window_x,window_y= 400,300
DISPLAYSURF = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption('TicTacToe')

#variables
count = 0
button = []
board_size = 0
empty = True
has_won = False
text_board = []
size_button = []

#Fonts used in the game
myfont = pygame.font.SysFont('Comic Sans MS', 30)
mainFont = pygame.font.SysFont('arial', 50)
mainButFont = pygame.font.SysFont('calibri', 20, bold=True)
boardsizeFont = pygame.font.SysFont('calibri',25,bold=True)
winFont = pygame.font.SysFont('Comic Sans MS', 19, bold=True)

#Colors used in the game
BOARDCOLOR = (26,140,255)
GRAY = (128,128,128)
RED = (255,43,48)
GREEN = (88,209,116)
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (186,48,172)
DARKTEAL = (16,103,124)
WINNER_TEXT = (15,94,181)

#Creates games buttons for the given size of the gameboard.
#Takes size of board and button variable as arguments
#Stores buttons in 2D array
def init_buttons(size,array):
	for x in range(size):
		array_butt = []
		for y in range(size):
			array_butt.append(pygame.Rect(0,0,0,0))
		array.append(array_butt)

#Takes size of board and position of mouse click as arguments
#Determines which space was clicked
def game_buttons(play,size,pos):
	for row in range(size):
		for col in range(size):
			#makes buttons 
			button[row][col] = pygame.Rect(col*(window_x/size),row*(window_y/size),window_x/size,window_y/size)
			if button[row][col].collidepoint(pos):
				valid_play = play.not_empty(row,col)
				if valid_play == True:
					gamepiece = play.gameplay(row,col)
					draw_gamepiece(play,row,col,gamepiece)

def draw_gamepiece(play,x,y,turn):
	global count
	global board_size
	box_sizex = window_x/board_size
	box_sizey = window_y/board_size
	x_coor = int(y*(box_sizex))
	y_coor = int(x*(box_sizey))

	if turn == True:
		pygame.draw.line(DISPLAYSURF, RED, (x_coor+int(box_sizex/6),y_coor+int(box_sizey/6)), 
			(x_coor+int(box_sizex*(5/6)),y_coor+int(box_sizey*(5/6))), 5)
		pygame.draw.line(DISPLAYSURF, RED, (x_coor+int(box_sizex*(5/6)), y_coor+int(box_sizey/6)), 
			(x_coor+int(box_sizex/6), y_coor+int(box_sizey*(5/6))), 5)
		count+=1
	else:
		pygame.draw.circle(DISPLAYSURF, PURPLE, (x_coor+int(box_sizex/2) , y_coor+int(box_sizey/2)), 
			int(box_sizey/3), 5)
		count+=1
	pygame.display.update()

	has_won,player = play.winner_winner(x,y)
	if has_won == True:
		winner(play,player)
	elif has_won == False and count == (board_size*board_size):
		tie_game(play,player,board_size)

#If game results in tie, this function is called
#gives user choice to play again or not.
def tie_game(play,player,size):
	global count
	global window_x,window_y
	pygame.draw.rect(DISPLAYSURF, GRAY, ((window_x-280)/2, (window_y-100)/2, 280, 100), 0)

	text_tie = winFont.render('Stalemate! (WOMP WOMP)',True,WINNER_TEXT)
	text_playagain = winFont.render('Would you like to play again?', True, WINNER_TEXT)
	text_yes = winFont.render('Yes',True,BLACK)
	text_no = winFont.render('No',True,BLACK)
	text_rect_tie = text_tie.get_rect(center=(window_x/2,(window_y-60)/2))
	text_rect_playagain = text_playagain.get_rect(center=(window_x/2,window_y/2))
	text_rect_yes = text_yes.get_rect(center=((window_x-40)/2,(window_y+50)/2))
	text_rect_no = text_no.get_rect(center=((window_x+40)/2,(window_y+50)/2))
	DISPLAYSURF.blit(text_tie,text_rect_tie)
	DISPLAYSURF.blit(text_yes,text_rect_yes)
	DISPLAYSURF.blit(text_no, text_rect_no)
	DISPLAYSURF.blit(text_playagain,text_rect_playagain)
	pygame.display.update()
	count = 0
	winner_response(play,player,size,text_rect_yes,text_rect_no)

#If it has been determined there is a winner, this function is called.
#player = false means X won, though the variable passed as player is x_turn
#and x_turn = true if it is X turn. This is because in the function ttt_gameplay(),
#it negates x_turn before winner() is called.  
def winner(play,player):
	global count
	global board_size
	global window_x,window_y
	pygame.draw.rect(DISPLAYSURF, GRAY, ((window_x-280)/2, (window_y-100)/2, 280, 100), 0)
	
	#Checks to see which player won, displays graphic.
	if player == False:
		text_winner = winFont.render('Congratulations Player \'X\'!', True, WINNER_TEXT)
		text_rect_winner = text_winner.get_rect(center=(window_x/2, (window_y-60)/2))
		DISPLAYSURF.blit(text_winner, text_rect_winner)
	else:
		text_winner = winFont.render('Congratulations Player \'O\'!', True, WINNER_TEXT)
		text_rect_winner = text_winner.get_rect(center=(window_x/2, (window_y-60)/2))
		DISPLAYSURF.blit(text_winner, text_rect_winner)

	#This continues with the graphic	
	text_playagain = winFont.render('Would you like to play again?', True, WINNER_TEXT)
	text_yes = winFont.render('Yes', True, BLACK)
	text_no = winFont.render('No', True, BLACK)
	text_rect_playagain = text_playagain.get_rect(center=(window_x/2,window_y/2))
	text_rect_yes = text_yes.get_rect(center=((window_x-40)/2,(window_y+50)/2))
	text_rect_no = text_no.get_rect(center=((window_x+40)/2,(window_y+50)/2))
	DISPLAYSURF.blit(text_playagain, text_rect_playagain)
	DISPLAYSURF.blit(text_yes, text_rect_yes)
	DISPLAYSURF.blit(text_no, text_rect_no)
	pygame.display.update()
	
	count = 0
	winner_response(play,player,board_size,text_rect_yes,text_rect_no)


def winner_response(play,player,size,yes,no):
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if yes.collidepoint(pos):
					fill_screen()
					draw_board(size)
					play.reset(False)
					gameplay(play,size)
				elif no.collidepoint(pos):
					fill_screen()
					play.reset(True)
					delete_buttons()
					reset_display_size()
					main()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

#Deletes the button array
def delete_buttons():
	global button
	button = []

#Resets display to original size
def reset_display_size():
	window_x,window_y= 400,300
	DISPLAYSURF = pygame.display.set_mode((window_x,window_y))

#Fills in the display black
def fill_screen():
	DISPLAYSURF.fill(BLACK)
	pygame.display.update()

#Draws game board depending on size
def draw_board(size):
	fill_screen()
	global window_x,window_y
	#Sets window size based on size of gameboard
	if size >=7:
		window_x = 800
		window_y = 700
	else:
		window_x = 400+((size-3)*100)
		window_y = 300+((size-3)*100)

	DISPLAYSURF = pygame.display.set_mode((window_x,window_y))

	#draws gameboard based on size of window
	#two separate for loops (one for columns and one for rows)
	for col in range(size-1):
		pygame.draw.line(DISPLAYSURF,BOARDCOLOR,(window_x/(size/(col+1)),0),(window_x/(size/(col+1)),window_y),5)
	for row in range(size-1):
		pygame.draw.line(DISPLAYSURF,BOARDCOLOR,(0,window_y/(size/(row+1))),(window_x,window_y/(size/(row+1))),5)
	pygame.display.update()

#this function is an infinite loop that takes a
#pygame mouseclick event, gets the position of
#the click, and calls the game_buttons() function,
#sending size of board and position as parameters
def gameplay(play,size):
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				game_buttons(play,size,pos)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()

#The menu you see if you want to play a 
#gameboard larger than the normal size of 3
def choose_menu():
	global board_size
	#variable for size of gameboard
	#increments by 2 each loop
	game_mode = 5

	#variable to increment the text_board array correctly
	array_increment = 5

	text_alternatives = myfont.render('Game Mode Alternatives',False,BOARDCOLOR)

	#loop to print text of game size and make clickable buttons
	while game_mode < 14:
		text_board.append(boardsizeFont.render('{}x{}'.format(game_mode,game_mode),False,RED))
		DISPLAYSURF.blit(text_board[game_mode-array_increment],(180,65+(game_mode-array_increment)*35))
		size_button.append(pygame.Rect(180,65+(game_mode-array_increment)*35,40,18))
		game_mode+=2
		array_increment+=1

	DISPLAYSURF.blit(text_alternatives,(33,5))
	pygame.display.update()
	
	#infinite choose_menu() loop
	#Calls appropriate functions depending on which button was clicked
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for x in range(5):
					if size_button[x].collidepoint(pos):
						board_size = (2*x)+5
						fill_screen()
						draw_board((2*x)+5)
						init_buttons((2*x)+5,button)
						play = TicTacToe((2*x)+5)
						play.game_board()
						gameplay(play,(2*x)+5)
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

def main():
	global board_size
	#graphics for the main menu
	maintext = mainFont.render('TicTacToe', False, BOARDCOLOR)
	DISPLAYSURF.blit(maintext,(85,30))
	text1 = mainButFont.render('Standard', True, RED)
	DISPLAYSURF.blit(text1,(155, 175))
	text2 = mainButFont.render('Choose Size', True, RED)
	DISPLAYSURF.blit(text2,(145, 200))
	stdBut = pygame.Rect(155,175,75,20)
	chBut = pygame.Rect(145,200,100,20)

	pygame.display.update()

	#infinite loop for the game that only ends when user exits
	while True:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:

				#variable for where mouse was clicked 
				pos = pygame.mouse.get_pos()

				#starts game or goes to choose_menu()
				#depending on what the user clicked
				if stdBut.collidepoint(pos):
					board_size = 3
					fill_screen()
					init_buttons(3,button)
					draw_board(3)
					#creates a game called play
					play = TicTacToe(3)
					play.game_board()
					gameplay(play,3)
				elif chBut.collidepoint(pos):
					fill_screen()
					choose_menu()

			if event.type == QUIT:
				pygame.quit()
				sys.exit()

if __name__ == '__main__':
	main()