# ===================================================
# THE N QUEENS PROBLEM - DISTINCT SOLUTIONS (RANDOM)
# ===================================================
# Tries to find (through simulation) the number of distinct solutions
#  to the N-queens problem, using the random algorithm.

import argparse
from time import time
from queens import nQueensRandom, showSolution

def clockwiseRotate(solution):
	rotated = len(solution)*[-1]
	for col, row in enumerate(solution):
		rotated[(N-1)-row] = col
	return rotated

def verticalReflect(solution):
	return [(N-1)-row for row in solution]



if __name__ == '__main__':

	# Initialize parser
	parser = argparse.ArgumentParser(
		description = "N-Queens: Distinct Solutions Finder (Random)"
	)

	# Positional parameters
	parser.add_argument('--n', help="N value (problem size)", type=int, default=8)
	parser.add_argument('--k', help="Number of generated solutions", type=int, default=1000)

	# Parse the arguments
	args = parser.parse_args()

	N = args.n
	N_SOLUTIONS = args.k

	solutionSet = set()
	start = time()

	for i in range(N_SOLUTIONS):
		sol, attempts, timeTaken = nQueensRandom(n=N)
		solutionIsNew = True

		if not sol:
			solutionIsNew = False
		
		solCopy = sol[::]
		for j in range(4):
			rotated = clockwiseRotate(solCopy)
			reflected = verticalReflect(solCopy)
			if (tuple(rotated) in solutionSet) or (tuple(reflected) in solutionSet):
				solutionIsNew = False
				break
			solCopy = rotated[::]

		if solutionIsNew:
			solutionSet.add(tuple(sol))
			#showSolution(sol)

	totalTime = round(time() - start, 3)

	print(f"Found {len(solutionSet)} distinct solutions for the {N}-queens problem, in {totalTime} seconds.")
