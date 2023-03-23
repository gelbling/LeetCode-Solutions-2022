# LeetCode 200

# TimeComplexity: O(n^2*4^n)
class Solution:
    def numIslands(self, grid) -> int:
    
        def dfs(x, y):
            
            # base case out of bounds 
            if x >= len(grid) or x < 0:
                return

            # base case out of bounds 
            if y >= len(grid[0]) or y < 0:
                return

            # base case out of bounds 
            if grid[x][y] != '1':
                return

            # mark the node as visited
            grid[x][y] = 'x'

            # mark all other nodes that are touching as visited
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        # island counter
        numIslands = 0

        # loop through 2d array
        for i in range(len(grid)):
            for ii in range(len(grid[0])):
                # if land is found, mark all connecting lands as visited, determining islands
                # increment island count if found
                if grid[i][ii] == '1':
                    dfs(i, ii)
                    numIslands += 1

        return numIslands