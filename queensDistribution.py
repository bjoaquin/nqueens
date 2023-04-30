#===============================================
# THE N QUEENS PROBLEM - SOLUTIONS DISTRIBUTION
#===============================================
# Exploratory analysis on how the random algorithm behaves.
# Counts how many attempts it takes it to find a solution and how long.
# Prints four plots in a same image - three histograms and a scatterplot.

import argparse
from time import time
from numpy import log
import matplotlib.pyplot as plt
from queens import nQueensRandom


if __name__ == '__main__':

	# Initialize parser
	parser = argparse.ArgumentParser(
		description = "N-Queens: Distribution EDA (Random)"
	)

	# Positional parameters
	parser.add_argument('--n', help="N value (problem size)", type=int, default=8)
	parser.add_argument('--k', help="Number of generated solutions", type=int, default=1000)
	parser.add_argument('--bins', help="Number of bins (histogram)", type=int, default=20)

	# Parse the arguments
	args = parser.parse_args()

	N = args.n
	N_POINTS = args.k
	N_BINS = args.bins

	attemptsList, timesList = [], []

	start = time()

	for i in range(N_POINTS):
		sol, attempts, times = nQueensRandom(n=N)
		attemptsList.append(attempts)
		timesList.append(times)

	simTime = round(time() - start, 2)
	print(f"Generated {N_POINTS} solutions in {simTime} seconds.")

	logAttemptsList = log(attemptsList)

	fig, axs = plt.subplots(2, 2)

	axs[0, 0].hist(attemptsList, bins=N_BINS)		# distribution of attempts
	axs[0, 1].hist(timesList, bins=N_BINS)			# distribution of times taken
	axs[1, 0].plot(attemptsList, timesList, 'o')	# scatter: times vs attempts
	axs[1, 1].hist(logAttemptsList, bins=N_BINS)	# distribution of log attempts

	fig.suptitle('Efficiency of eightQueensSolver()', fontsize=16)
	axs[0, 0].set_xlabel('# of attempts')
	axs[0, 0].set_ylabel('Frequency')
	axs[0, 1].set_xlabel('Time taken (milliseconds)')
	axs[0, 1].set_ylabel('Frequency')
	axs[1, 0].set_xlabel('# of attempts')
	axs[1, 0].set_ylabel('Time taken (milliseconds)')
	axs[1, 1].set_xlabel('log(# of attempts)')
	axs[1, 1].set_ylabel('Frequency')

	plt.show()