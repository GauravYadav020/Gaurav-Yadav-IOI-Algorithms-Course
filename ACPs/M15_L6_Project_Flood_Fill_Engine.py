# Module 15 Lesson 6: After-Class Project
# Project Name: Canvas Graphics In-Memory Grid Pixel Cluster Manipulation Engine

def execute_flood_fill(image_grid, source_row, source_col, targeting_new_color):
    base_color = image_grid[source_row][source_col]
    if base_color == targeting_new_color: return image_grid
    rows, cols = len(image_grid), len(image_grid[0])
    
    def fill_dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image_grid[r][c] != base_color: return
        image_grid[r][c] = targeting_new_color
        fill_dfs(r+1, c); fill_dfs(r-1, c); fill_dfs(r, c+1); fill_dfs(r, c-1)
        
    fill_dfs(source_row, source_col)
    return image_grid

if __name__ == "__main__":
    canvas = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(f"Mutated pixel colors canvas orientation results maps: {execute_flood_fill(canvas, 1, 1, 2)}")