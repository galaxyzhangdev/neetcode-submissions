class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])
        # Set to keep track of the cells visited in the current path
        path = set()

        # Define the depth-first search (DFS) function
        def dfs(r, c, i):
            # Base case: if we have matched the entire word
            if i == len(word):
                return True
            
            # Check if the current cell is out of bounds, doesn't match the current character,
            # or has already been visited
            if (min(r, c) < 0 or  # Out of bounds check for negative indices
                r >= ROWS or c >= COLS or  # Out of bounds check for rows and columns
                word[i] != board[r][c] or  # Character mismatch check
                (r, c) in path):  # Check if the cell has already been visited
                return False

            # Add the current cell to the path to mark it as visited
            path.add((r, c))
            
            # Recursively call dfs in all four directions (down, up, right, left)
            res = (dfs(r + 1, c, i + 1) or  # Move down
                   dfs(r - 1, c, i + 1) or  # Move up
                   dfs(r, c + 1, i + 1) or  # Move right
                   dfs(r, c - 1, i + 1))    # Move left

            # Remove the current cell from the path after exploring all directions (backtracking)
            path.remove((r, c))
            return res

        # Iterate through each cell in the board to find the starting point of the word
        for r in range(ROWS):
            for c in range(COLS):
                # If dfs returns True, the word exists in the board
                if dfs(r, c, 0):
                    return True
        
        # If no valid path is found, return False
        return False

