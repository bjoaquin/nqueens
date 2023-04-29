# ==================================
# THE 8 QUEENS PROBLEM - ALGORITHMS
# ==================================
# Contains two implementations of an 8-queens search algorithm.
# One makes random attempts until success (not yet generalized for any N,
#  would run forever if no solution).
# The other searches in an organized manner until finding a solution, 
#  if it exists. Works for any N.
# If run, it performs a single search (linear or random) and prints the result.

from random import randint
from time import time

def eightQueensRandom():
	
	def setToList(mySet):
		L = len(mySet)*[-1]
		for elem in mySet:
			L[elem[1]] = elem[0]
		return L

	start = time()
	M = [8*[1] for _ in range(8)]	# valid positions for next queen
	Q = []							# position of queens already placed on board
	attempts = 1

	# While the board is still incomplete,
	while len(Q) < 8:
		# generate a random position
		a, b = randint(0, 7), randint(0, 7)
		# (which hasn't been taken yet),
		while M[a][b]==0:
			a, b = randint(0, 7), randint(0, 7)
		# take all the cells from this position's row/column
		for j in range(8):
			M[a][j] = 0 # j-th elem of a-th list
			M[j][b] = 0 # b-th elem of j-th list
		# and also from its diagonals,
		lower_diag, upper_diag = -min(a,b), 7-max(a,b)
		lower_anti_diag, upper_anti_diag = -min(7-a,b), 7-max(7-a,b)
		for j in range(lower_diag, upper_diag+1):
			M[a+j][b+j] = 0
		for j in range(lower_anti_diag, upper_anti_diag+1):
			M[a-j][b+j] = 0
		# and append it to the list of queens.
		Q.append((a, b))
		# If all cells are taken but there's less than N queens,
		if sum([sum(m) for m in M])==0 and len(Q)<8:
			# restart everything.
			M = [8*[1] for _ in range(8)]
			Q = []
			attempts += 1
	# If you reach this then a solution has been found.
	# How long did it take to reach it?
	timeTaken = 1000 * (time() - start)
	
	return setToList(Q), attempts, timeTaken


def nQueensLinear(n=8, initialState=[]):
	
	def conflict(board, col, row):
		# Ignore placeholders (WORK IN PROGRESS!!!)
		if row == -1:
			return False
		# Two or more queens on the same row?
		if row in board:
			return True
		# Two or more queens on the same diagonal?
		for k in range(1, col+1):
			if board[col-k] in [row+k, row-k]:
				return True
		# All good!
		return False

	def checkBoard(board):
		col = len(board)
		if col == n:
			return board
		for row in range(n):
			if conflict(board, col, row):
				continue
			newBoard = checkBoard(board+[row])
			if len(newBoard) == n:
				return newBoard
		return board

	start = time()
	Q = initialState

	if Q:
		for k in range(1, len(Q)):
			if conflict(Q[:k], k, Q[k]):
				timeTaken = 1000 * (time() - start)
				print('WARNING: Initial state is invalid.')
				return [], timeTaken
	
	board = checkBoard(Q)
	if len(board) < n:
		print('No solution exists for this setting.')
		board = []
	
	timeTaken = 1000 * (time() - start)

	return board, timeTaken


def showSolution(solution):
	N = len(solution)

	board = N * [N*"|   " + "|"]
	boardJoints = N*"+---" + "+"

	for idx, q in enumerate(solution):
		board[q] = board[q][:4*idx + 2] + "Q" + board[q][4*idx + 3:]

	print(boardJoints)
	for i in range(N):
		print(board[i])
		print(boardJoints)

		



if __name__ == '__main__':

	mySolution, myTimeTaken = nQueensLinear(n=4)
	print(f"Done! Took {round(myTimeTaken, 2)} milliseconds.")
	
	#mySolution, myAttempts, myTimeTaken = eightQueensRandom()
	#print(f"Done! Took {myAttempts} attempts ({round(myTimeTaken, 2)} milliseconds).")
	
	print(mySolution)
	showSolution(mySolution)