class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = set()
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            side = count = 0
            for dr, dc in directions:
                nrow , ncol = row + dr, col + dc
                # for adding the perimetrs of this cell
                # if it is out of Boundary) or if it is a water add one to the perimenter
                if not in_bound(nrow, ncol) or grid[nrow][ncol] == 0:
                    side += 1
                    continue

                new_state = State(nrow, ncol)
                # if the direction have not been traveled
                if new_state not in  seen:
                    seen.add(new_state)
                    count += dfs(nrow, ncol)
            return side + count
        
        # find one cell which is island
        for row in range(n):
            for col in range(m):
                # Find an island & is not in seen
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add(State(row, col))
                    return dfs(row, col)
        return 0

        
class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, __o: object):
        return isinstance(__o, State) and self.x == __o.x and self.y == __o.y

    def __hash__(self):
        return hash(f'{self.x} {self.y}')   
