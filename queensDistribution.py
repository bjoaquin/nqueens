#===============================================
# THE 8 QUEENS PROBLEM - SOLUTIONS DISTRIBUTION
#===============================================
# Exploratory analysis on how the random algorithm behaves.
# Counts how many attempts it takes it to find a solution and how long.
# Prints four plots in a same image - three histograms and a scatterplot.

from time import time
from numpy import log
import matplotlib.pyplot as plt
from queens import eightQueensRandom

N_points = 10**3
n_bins = 20

attemptsList, timesList = [], []

start = time()

for i in range(N_points):
	sol, attempts, times = eightQueensRandom()
	attemptsList.append(attempts)
	timesList.append(times)

simTime = round(time() - start, 2)
print(f"Generated {N_points} points in {simTime} seconds.")

logAttemptsList = log(attemptsList)

fig, axs = plt.subplots(2, 2)

axs[0, 0].hist(attemptsList, bins=n_bins)		# distribution of attempts
axs[0, 1].hist(timesList, bins=n_bins)			# distribution of times taken
axs[1, 0].plot(attemptsList, timesList, 'o')	# scatter: times vs attempts
axs[1, 1].hist(logAttemptsList, bins=n_bins)	# distribution of log attempts

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