#========================================
# THE N QUEENS PROBLEM - SEARCH RUN TIME
#========================================
# Empirical study on how the puzzle size influences the run time for the linear algorithm.
# Iterates from N=1 to N=upperLimit and looks for a solution for each N.
# Repeats each step many times with a random starting value for the first column,
#  since runtime appears to be heavily dependant on this.
# Records average runtime of every step and stores it in a list.
# Prints a scatterplot of runtime versus size (N).

import argparse
from time import time
import matplotlib.pyplot as plt
from queens import nQueensLinear
from random import randint
from statistics import mean

if __name__ == '__main__':

	# Initialize parser
	parser = argparse.ArgumentParser(
		description = "N-Queens: Distribution EDA (Random)"
	)

	# Positional parameters
	parser.add_argument('--ul', help="Upper limit for N", type=int, default=15)
	parser.add_argument('--k', help="Number of replicates for each size", type=int, default=5)

	# Parse the arguments
	args = parser.parse_args()

	UPPER_LIMIT = args.ul
	N_REPLICATES = args.k

	sizesList = [x for x in range(1, UPPER_LIMIT+1)]
	runtimesList = []

	start = time()

	for N in sizesList:
		runtimes = []
		for k in range(N_REPLICATES):
			sol, runtime = nQueensLinear(n=N, initialState=[randint(0, N-1)], verbose=False)
			runtimes.append(runtime)
		runtimesList.append(mean(runtimes))

	totalTime = round(time() - start, 2)
	print(f"Solved {N_REPLICATES*UPPER_LIMIT} puzzles in {totalTime} seconds.")

	plt.plot(sizesList, runtimesList, '-o', color="orange")

	plt.title('Runtime of nQueensLinear for different values of N')
	plt.xlabel('Problem size')
	plt.ylabel('Runtime (milliseconds)')

	plt.show()