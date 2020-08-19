import numpy as np
def minTotalDistance(grid: list) -> int: 
	if ROW == 0 or COL == 0: 
		return 0
	vertical = [] 
	horizontal = [] 
	for i in range(ROW): 
		for j in range(COL): 
			if grid[i][j] == 1: 
				vertical.append(i) 
				horizontal.append(j) 
	vertical.sort() 
	horizontal.sort() 
	size = len(vertical) // 2
	x = vertical[size] 
	y = horizontal[size] 
	distance = 0
	for i in range(ROW): 
		for j in range(COL): 
			if grid[i][j] == 1: 
				distance += abs(x - i) + abs(y - j) 
	return distance 
if __name__ == "__main__": 
  ROW,COL = map(int,input().split())
  nums=list(map(int,input().split()))
  grid=np.array(nums).reshape(ROW,COL)
  print(minTotalDistance(grid)) 
