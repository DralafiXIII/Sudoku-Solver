import numpy as np

def possible(grid,x,y,n):
	for i in range(0,9):
		if grid[x][i] == n:
			return False
		if grid[i][y] == n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if grid[x0+i][y0+j] == n:
				return False
	return True

def solve(grid):
	for x in range(9):
		for y in range(9):
			if grid[x][y] == 0:
				for n in range(1,10):
					if possible(grid,x,y,n):
						grid[x][y] = n
						solve(grid)
						grid[x][y] = 0
				return
	print(np.matrix(grid))
	input("Press any key for more solutions (will display nothing if no further solutions)")

# create object of 9x9 2D array with each element consisting of 0 - 9. 0 is utilized to represent a blank.
# Example:

example = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
print(np.matrix(example))

solve(example)

# Returning no results indicates that that sudoku puzzle is unsolveable.