# N-Queens: A repo for studying the N-Queens problem

## The problem
I will not introduce the problem myself. You can read about it [here](https://en.wikipedia.org/wiki/Eight_queens_puzzle).

## This repo
There's currently 3 (three) files on this repo.

* **queens.py**: contains two implementations of searches for solutions to the N-queens problem.
  - *eightQueensRandom()*: works only for N=8 and assumes at least one solution exists. Would run forever if there's no solution. Returns a different solution on every run.
  - *nQueensLinear(n=8, initialState=[])*: solves for any N and returns blank board if no solution exists. Returns the same solution on every run, under the same parameters. Also includes a barebones implementation of an idea I'm currently working on - finding a solution (if it exists) given some queens already placed on the board. For now this only works if the initial state is of the form of K consecutive queens, starting from the first column and moving to the right.

## Further resources
I got the idea for this repo by following MIT's 6.S095 (**Programming for the Puzzled**) by Srini Devadas. This problem is tackled on the [fifth](https://www.youtube.com/watch?v=1_0WwiUUsTc&list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA&index=5) and [sixth lecture](https://www.youtube.com/watch?v=Pe1MBDbGfwc&list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA&index=6).
