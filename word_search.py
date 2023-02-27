# LeetCode 79

# w = board rows
# m = board cols
# n = word length
# Time Complexity: O(w * m * 4^n)

class Solution:
    def exist(self, board, word: str) -> bool:

        # get dimensions
        rows, cols = len(board), len(board[0])
        # initialize visited path set
        visited = set()

        # dfs recursive function
        def dfs(x, y, i):

            # if index reaches end of word, word is found
            if i == len(word):
                return True
            
            # base cases
            if (x >= rows or x < 0 or 
               y >= cols or y < 0 or 
               (x,y) in visited or 
               word[i] != board[x][y]):
               return False

            # add visited node
            visited.add((x,y))

            # recursive call
            output = (dfs(x+1,y,i+1) or 
                      dfs(x-1,y,i+1) or
                      dfs(x,y+1,i+1) or 
                      dfs(x,y-1,i+1))

            # remove node from visited path
            visited.remove((x,y))
            
            return output

        # call fucntion for each node on board
        for x in range(rows):
            for y in range(cols):
                if dfs(x,y,0):
                    return True
        
        return False