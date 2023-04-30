# N-Queens: A repo for studying the N-Queens problem

## The problem
I will not introduce the problem myself. You can read about it [here](https://en.wikipedia.org/wiki/Eight_queens_puzzle).

## This repo
Here's a list with the current files on this repo.

* **queens.py**: contains two implementations of searches for solutions to the N-queens problem.
  - `nQueensRandom(n=8, initialState=[])`: Tries random combinations of queens placing, up to 1000 attempts. Returns a different solution on every run.
  - `nQueensLinear(n=8, initialState=[], verbose=True)`: solves for any N and returns blank board if no solution exists. Starts by placing queen on the leftmost column and works its way to the rightmost column. Returns the same solution on every run, under the same parameters.
  For both algorithms, the board is stored as a list, where each value is an integer between 0 and `N-1`. Users can set an initial state for the board, which must be written as a list of size N (or less), with -1 for empty columns (except for the rightmost columns, which can be omitted if they are all equal to -1).
* **queensDistinctRandom.py**: uses simulation to find all distinct solutions to the N-queens problem, through the *nQueensRandom* function. The term "distinct" means that the algorithm considers reflected and rotated solutions to be the same as the original. There are only 12 distinct solutions. In the future I could add an argument which allows users to turn on and off the distinction between reflected/rotated solutions - it should be pretty straightforward.
* **queensDistribution.py**: EDA on the behavior of the `nQueensRandom` algorithm. In particular, it studies the number of random "attempts" until finding a correct solution and the time taken to do so. Returns a single figure with four plots - three histograms and a scatterplot.
* **queensRuntimeLinear.py**: solves puzzles of increasing size (1 to `UPPER_LIMIT`) using `nQueensLinear`, and records runtimes. Each size is solved multiple times, each time with a different starting point for the first column (since runtimes are heavily dependant on the initial state). Returns a scatterplot of average runtime versus size.

## How to use
Download the scripts, open a terminal in the corresponding directory and type `python <scriptname.py> -h` to see instructions.

## Further resources
I got the idea for this repo by following MIT's 6.S095 (**Programming for the Puzzled**) by Srini Devadas. This problem is tackled on the [fifth](https://www.youtube.com/watch?v=1_0WwiUUsTc&list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA&index=5) and [sixth lectures](https://www.youtube.com/watch?v=Pe1MBDbGfwc&list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA&index=6).
