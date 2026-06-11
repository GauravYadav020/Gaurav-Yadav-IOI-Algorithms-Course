# Module 15 Lesson 5: After-Class Project
# Project Name: Spatial Multi-Dimensional Grid Coordinate Island Topology Resolver

class SpatialIslandsEngine:
    def calculate_islands_count(self, topology_grid_matrix):
        if not topology_grid_matrix: return 0
        rows, cols = len(topology_grid_matrix), len(topology_grid_matrix[0])
        total_islands_counter = 0
        
        def purge_island_dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or topology_grid_matrix[r][c] == '0': return
            topology_grid_matrix[r][c] = '0' # Sink element state to eliminate repeat processing triggers
            purge_island_dfs(r+1, c); purge_island_dfs(r-1, c)
            purge_island_dfs(r, c+1); purge_island_dfs(r, c-1)
            
        for r in range(rows):
            for c in range(cols):
                if topology_grid_matrix[r][c] == '1':
                    total_islands_counter += 1
                    purge_island_dfs(r, c)
        return total_islands_counter

if __name__ == "__main__":
    engine = SpatialIslandsEngine()
    grid = [['1', '1', '0'], ['0', '1', '0'], ['0', '0', '1']]
    print(f"Total separate continuous clusters maps tracked: {engine.calculate_islands_count(grid)}")