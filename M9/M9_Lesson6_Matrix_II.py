# ============================================================
#        MODULE 9 - LESSON 6: MATRIX II
# ============================================================
# Topics Covered:
#   - Set matrix zeroes (in-place)
#   - Pascal's Triangle generation
#   - Matrix chain multiplication (DP)
#   - Flood Fill algorithm
#   - Sudoku Validator
# ============================================================


# ──────────────────────────────────────────────────────────
#  ACTIVITY 1 — Set Matrix Zeroes + Pascal's Triangle
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Given an m×n matrix, if any element is 0, set its
        entire row and column to 0 — in-place, O(1) extra space
        using first row/column as markers.

    (b) Generate the first N rows of Pascal's Triangle and
        return as a 2D list. Also extract the k-th row directly
        using the mathematical formula in O(k) time.
"""

print("=" * 60)
print("   ACTIVITY 1: Set Matrix Zeroes + Pascal's Triangle")
print("=" * 60)


def pretty_print(matrix, label="Matrix"):
    print(f"  {label}:")
    col_w = max(len(str(x)) for row in matrix for x in row) + 2
    for row in matrix:
        print("  ", "".join(str(x).rjust(col_w) for x in row))
    print()


def set_matrix_zeroes(matrix):
    """
    In-place zero-setting.
    Step 1: Use first row & col as flags.
    Step 2: Mark rows/cols that contain zero.
    Step 3: Use flags to zero out cells.
    Step 4: Zero first row/col if needed.
    Time: O(m*n)  Space: O(1)
    """
    import copy
    mat = copy.deepcopy(matrix)
    m, n = len(mat), len(mat[0])

    first_row_zero = any(mat[0][j] == 0 for j in range(n))
    first_col_zero = any(mat[i][0] == 0 for i in range(m))

    # Use first row and col as markers
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 0:
                mat[i][0] = 0   # mark row
                mat[0][j] = 0   # mark col

    # Zero out marked rows and cols
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    # Handle first row
    if first_row_zero:
        for j in range(n):
            mat[0][j] = 0

    # Handle first col
    if first_col_zero:
        for i in range(m):
            mat[i][0] = 0

    return mat


def pascal_triangle(n):
    """
    Generate first n rows of Pascal's Triangle.
    Each row[j] = prev_row[j-1] + prev_row[j]
    Time: O(n²)
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


def pascal_kth_row(k):
    """
    Get k-th row (0-indexed) using C(k,0), C(k,1), ..., C(k,k).
    C(k,r) = C(k, r-1) * (k - r + 1) / r
    Time: O(k)  Space: O(k)
    """
    row = [1] * (k + 1)
    for r in range(1, k + 1):
        row[r] = row[r-1] * (k - r + 1) // r
    return row


# ── Driver Code ──
mat = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

print()
pretty_print(mat, "Original Matrix")
zeroed = set_matrix_zeroes(mat)
pretty_print(zeroed, "After Set Zeroes")

print("[+] Pascal's Triangle (first 6 rows):")
pt = pascal_triangle(6)
for i, row in enumerate(pt):
    print(f"  Row {i}: {row}")

print(f"\n[+] Pascal's Triangle row 7 (index=7): {pascal_kth_row(7)}")
print(f"[+] Pascal's Triangle row 0 (index=0): {pascal_kth_row(0)}")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 2 — Matrix Chain Multiplication (DP)
# ──────────────────────────────────────────────────────────
"""
Problem:
    Given dimensions of a sequence of matrices, find the
    minimum number of scalar multiplications needed to
    compute their product using dynamic programming.

    Input: dims array where matrix[i] has size dims[i] x dims[i+1]
    Output: minimum cost and optimal parenthesization

    Time: O(n³)  Space: O(n²)
"""

print("\n" + "=" * 60)
print("   ACTIVITY 2: Matrix Chain Multiplication (DP)")
print("=" * 60)


def matrix_chain_order(dims):
    """
    dims[i] = rows of matrix i, dims[i+1] = cols of matrix i
    n = number of matrices = len(dims) - 1
    dp[i][j] = min cost to multiply matrices i through j
    split[i][j] = optimal split point
    """
    n = len(dims) - 1          # number of matrices
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    # l = chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


def get_optimal_parens(split, i, j):
    """Reconstruct optimal parenthesization string."""
    if i == j:
        return f"M{i+1}"
    k = split[i][j]
    left = get_optimal_parens(split, i, k)
    right = get_optimal_parens(split, k+1, j)
    return f"({left} × {right})"


# ── Driver Code ──
print()
dims_examples = [
    ([10, 30, 5, 60],        "3 matrices: 10×30, 30×5, 5×60"),
    ([40, 20, 30, 10, 30],   "4 matrices: 40×20, 20×30, 30×10, 10×30"),
    ([10, 20, 30, 40, 30],   "4 matrices: 10×20, 20×30, 30×40, 40×30"),
]

for dims, desc in dims_examples:
    dp, split = matrix_chain_order(dims)
    n = len(dims) - 1
    min_cost = dp[0][n-1]
    optimal = get_optimal_parens(split, 0, n-1)
    print(f"[+] {desc}")
    print(f"    Min multiplications: {min_cost}")
    print(f"    Optimal order: {optimal}")

    # Show DP table
    print("    DP Cost Table:")
    for i in range(n):
        row_str = ""
        for j in range(n):
            if j >= i:
                row_str += f"{dp[i][j]:8d}"
            else:
                row_str += "        "
        print("   ", row_str)
    print()


# ──────────────────────────────────────────────────────────
#  ACTIVITY 3 — Flood Fill + Sudoku Validator
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Flood Fill: Given an image (2D grid), a start cell,
        and a new color, fill the connected region of the
        same original color with the new color using BFS.
        (Like paint bucket tool in image editors)

    (b) Sudoku Validator: Given a 9×9 board (0 = empty),
        check if the filled cells are valid per Sudoku rules:
          - Each row has no duplicate 1-9
          - Each column has no duplicate 1-9
          - Each 3×3 box has no duplicate 1-9
"""

print("=" * 60)
print("   ACTIVITY 3: Flood Fill + Sudoku Validator")
print("=" * 60)


# ── (a) Flood Fill using BFS ──

def flood_fill_bfs(image, sr, sc, new_color):
    """
    BFS flood fill from (sr, sc).
    Fills all 4-directionally connected cells with
    the same original color as image[sr][sc].
    Time: O(m*n)  Space: O(m*n) for queue
    """
    import copy
    from collections import deque

    img = copy.deepcopy(image)
    orig_color = img[sr][sc]

    if orig_color == new_color:
        return img   # already the target color

    m, n = len(img), len(img[0])
    queue = deque([(sr, sc)])
    img[sr][sc] = new_color
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and img[nr][nc] == orig_color:
                img[nr][nc] = new_color
                queue.append((nr, nc))

    return img


def print_image(img, label="Image"):
    print(f"  {label}:")
    for row in img:
        print("   ", row)
    print()


print()
image = [
    [1, 1, 1, 0, 0],
    [1, 1, 0, 0, 2],
    [1, 0, 0, 2, 2],
    [0, 0, 2, 2, 2],
    [0, 2, 2, 2, 0]
]

print_image(image, "Original Image")
filled = flood_fill_bfs(image, 0, 0, 9)
print_image(filled, "After Flood Fill from (0,0) with color 9")

# Edge: fill already same color
img2 = [[1, 2], [3, 4]]
print_image(flood_fill_bfs(img2, 0, 0, 1), "Fill (0,0) with same color (no change)")


# ── (b) Sudoku Validator ──

def is_valid_sudoku(board):
    """
    Validate a 9×9 Sudoku board (0 = empty cell).
    Check rows, columns, and 3×3 boxes.
    Time: O(81) = O(1)
    """
    def has_duplicates(cells):
        nums = [c for c in cells if c != 0]
        return len(nums) != len(set(nums))

    # Check rows
    for row in range(9):
        if has_duplicates(board[row]):
            return False, f"Duplicate in row {row}"

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if has_duplicates(column):
            return False, f"Duplicate in column {col}"

    # Check 3×3 boxes
    for box_r in range(3):
        for box_c in range(3):
            box = []
            for r in range(box_r * 3, box_r * 3 + 3):
                for c in range(box_c * 3, box_c * 3 + 3):
                    box.append(board[r][c])
            if has_duplicates(box):
                return False, f"Duplicate in box ({box_r},{box_c})"

    return True, "Valid Sudoku board!"


print("[b] Sudoku Validator:")

valid_board = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],

    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],

    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9],
]

invalid_board = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],

    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],

    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [5, 0, 0,  0, 8, 0,  0, 7, 9],   # 5 repeated in column 0
]

def print_sudoku(board, label="Board"):
    print(f"\n  {label}:")
    for i, row in enumerate(board):
        r_str = ""
        for j, val in enumerate(row):
            r_str += (str(val) if val != 0 else ".") + " "
            if j in [2, 5]:
                r_str += "| "
        print(f"  {r_str}")
        if i in [2, 5]:
            print("  " + "-" * 22)

print_sudoku(valid_board, "Valid Board")
is_v, msg_v = is_valid_sudoku(valid_board)
print(f"  Result: {'✓' if is_v else '✗'} {msg_v}")

print_sudoku(invalid_board, "Invalid Board (col 0 has two 5s)")
is_i, msg_i = is_valid_sudoku(invalid_board)
print(f"  Result: {'✗' if not is_i else '✓'} {msg_i}")
