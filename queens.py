# ==================================
# THE N QUEENS PROBLEM - ALGORITHMS
# ==================================
# Contains two implementations of an 8-queens search algorithm.
# One makes random attempts until success. The other searches in an organized
#  manner until finding a solution, if it exists. Both work for any N.
# If run, it performs a single search (linear or random) and prints the result.

import argparse
from random import randint
from time import time


def nQueensRandom(n=8, initialState=[]):
	
	def setToList(mySet):
		L = len(mySet)*[-1]
		for elem in mySet:
			L[elem[1]] = elem[0]
		return L

	def knockOutCells(matrix, col, row):
		# take all the cells from this position's row/column
		for j in range(n):
			matrix[col][j] = 0
			matrix[j][row] = 0
		# and also from its diagonals,
		LD, UD = -min(col,row), (n-1)-max(col,row)
		for j in range(LD, UD+1):
			matrix[col+j][row+j] = 0
		LaD, UaD = -min((n-1)-col,row), (n-1)-max((n-1)-col,row)
		for j in range(LaD, UaD+1):
			matrix[col-j][row+j] = 0
		return matrix

	start = time()
	attempts = 1
	M = [n*[1] for _ in range(n)]	# valid positions for next queen
	Q = []							# position of queens already placed on board
	for row, col in enumerate(initialState):
		if col != -1 and M[col][row] == 1:
			M = knockOutCells(M, col, row)
			Q.append((col, row))
		else:
			print('ERROR: Invalid initial state')
			return [], 1, 0

	# While the board is still incomplete,
	while len(Q) < n and attempts < 1000:
		# generate a random position
		a, b = randint(0, n-1), randint(0, n-1)
		# (which hasn't been taken yet),
		while M[a][b]==0:
			a, b = randint(0, n-1), randint(0, n-1)
		# take all the cells from this position's row/column
		M = knockOutCells(M, a, b)
		# and append it to the list of queens.
		Q.append((a, b))
		# If all cells are taken but there's less than N queens,
		if sum([sum(m) for m in M])==0 and len(Q)<n:
			# restart everything.
			M = [n*[1] for _ in range(n)]
			Q = []
			for row, col in enumerate(initialState):
				if col != -1:
					M = knockOutCells(M, col, row)
					Q.append((col, row))
			attempts += 1
	
	# Either a solution was found and time ran out.
	# How long did it take?
	timeTaken = 1000 * (time() - start)

	if not Q:
		print("No solution found after 1000 attempts. Maybe there's no solution?")
	
	return setToList(Q), attempts, timeTaken



def nQueensLinear(n=8, initialState=[], verbose=True):
	
	def conflict(board, col, row):
		# Ignore placeholders
		if row == -1:
			return False
		# Two or more queens on the same row?
		if row in board:
			return True
		# Two or more queens on the same diagonal?
		for k in range(1, col+1):
			if abs(board[col-k] - row) == k:
				return True
		# All good!
		return False

	def checkBoard(initialBoard, board=n*[-1], col=0):
		
		# Terminate if board is complete.
		if col == n:
			return board
		
		# If this col is already defined in the initial state,
		# assign to it the corresponding value and carry on.
		if initialBoard[col] != -1:
			proposedBoard = board[::]
			proposedBoard[col] = initialBoard[col]
			newBoard = checkBoard(initialBoard, proposedBoard, col+1)
			if len(newBoard) == n and (-1 not in newBoard):
				return newBoard
		# Else, propose each possible row as candidate, one at a time.
		else:
			for row in range(n):
				if conflict(board, col, row):
					continue
				proposedBoard = board[::]
				proposedBoard[col] = row
				newBoard = checkBoard(initialBoard, proposedBoard, col+1)
				if len(newBoard) == n and (-1 not in newBoard):
					return newBoard
		
		return board

	start = time()
	Q = initialState

	# Check for conflict within the initial state
	if Q:
		for k in range(1, len(Q)):
			if conflict(Q[:k], k, Q[k]):
				timeTaken = 1000 * (time() - start)
				if verbose:
					print('WARNING: Initial state is invalid.')
				return [], timeTaken
	
	# Fill the "rest" of the initial state with -1
	Q = Q + (n-len(Q))*[-1]

	# Search for a solution (given initial state Q)
	board = checkBoard(Q)
	if -1 in board:
		if verbose:
			print('No solution exists for this setting.')
		board = []
	
	timeTaken = 1000 * (time() - start)

	return board, timeTaken



def showSolution(solution):
	N = len(solution)

	if N == 0:
		return 0

	board = N * [N*"|   " + "|"]
	boardJoints = N*"+---" + "+"

	for idx, q in enumerate(solution):
		board[q] = board[q][:4*idx + 2] + "Q" + board[q][4*idx + 3:]

	print(boardJoints)
	for i in range(N):
		print(board[i])
		print(boardJoints)

		



if __name__ == '__main__':

	# Initialize parser
	parser = argparse.ArgumentParser(
		description = "N-Queens Solver"
	)

	# Positional parameters
	parser.add_argument(
		'--n', help="N value (problem size)", 
		type=int, default=8
	)
	parser.add_argument(
		'--algo', help="Algorithm ('linear' or 'random')",
		default="linear"
	)
	parser.add_argument('--init', nargs='+', 
		help="Initial state"
	)

	# Parse the arguments
	args = parser.parse_args()

	if args.init:
		initialState = [int(x) for x in args.init]
	else:
		initialState = []

	if args.algo == 'linear':
		mySolution, myTimeTaken = nQueensLinear(n=args.n, initialState=initialState)
		print(f"Done! Took {round(myTimeTaken, 2)} milliseconds.")
	else:
		mySolution, myAttempts, myTimeTaken = nQueensRandom(n=args.n, initialState=initialState)
		print(f"Done! Took {myAttempts} attempts ({round(myTimeTaken, 2)} milliseconds).")
	
	print(mySolution)
	showSolution(mySolution)