# ===================================================
# THE 8 QUEENS PROBLEM - DISTINCT SOLUTIONS (RANDOM)
# ===================================================
# Tries to find (through simulation) the number of distinct solutions
#  to the 8 queens problem, using the random algorithm.
# Has an error! Reports more solutions than it should.

from time import time
from queens import eightQueensRandom, showSolution

N_solutions = 10**3

solutionSet = set()

def clockwiseRotate(solution):
	rotated = len(solution)*[-1]
	for col, row in enumerate(solution):
		rotated[7-row] = col
	return rotated

def verticalReflect(solution):
	return [7-row for row in solution]

start = time()

for i in range(N_solutions):
	sol, attempts, timeTaken = eightQueensRandom()
	solutionIsNew = True
	
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
		showSolution(sol)
		print()

totalTime = round(time() - start, 3)

print(f"Gathered {len(solutionSet)} distinct solutions in {totalTime} seconds.")
