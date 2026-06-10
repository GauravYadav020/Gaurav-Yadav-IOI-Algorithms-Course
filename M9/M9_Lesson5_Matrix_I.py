# ============================================================
#        MODULE 9 - LESSON 5: MATRIX I
# ============================================================
# Topics Covered:
#   - 2D matrix creation and display
#   - Matrix addition, subtraction, multiplication
#   - Transpose of a matrix
#   - Rotate matrix 90° clockwise/anti-clockwise
#   - Spiral order traversal
# ============================================================


# ──────────────────────────────────────────────────────────
#  ACTIVITY 1 — Matrix Operations (Add, Subtract, Multiply)
# ──────────────────────────────────────────────────────────
"""
Problem:
    Implement matrix operations from scratch:
      - matrix_add(A, B)
      - matrix_subtract(A, B)
      - matrix_multiply(A, B)   — standard O(n³) algorithm
    Also implement a pretty_print helper.
"""

print("=" * 60)
print("   ACTIVITY 1: Matrix Addition, Subtraction & Multiplication")
print("=" * 60)


def pretty_print(matrix, label="Matrix"):
    print(f"  {label}:")
    for row in matrix:
        print("   ", row)
    print()


def get_dimensions(matrix):
    return len(matrix), len(matrix[0])


def matrix_add(A, B):
    """Element-wise addition. Requires same dimensions."""
    rows, cols = get_dimensions(A)
    if get_dimensions(A) != get_dimensions(B):
        raise ValueError("Matrices must have same dimensions for addition.")
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]


def matrix_subtract(A, B):
    """Element-wise subtraction."""
    rows, cols = get_dimensions(A)
    if get_dimensions(A) != get_dimensions(B):
        raise ValueError("Matrices must have same dimensions for subtraction.")
    return [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]


def matrix_multiply(A, B):
    """
    Standard matrix multiplication.
    A is (m x n), B is (n x p) → result is (m x p).
    Time: O(m * n * p)
    """
    m, n = get_dimensions(A)
    n2, p = get_dimensions(B)
    if n != n2:
        raise ValueError(f"Cannot multiply ({m}x{n}) by ({n2}x{p}): inner dims must match.")
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


def scalar_multiply(A, scalar):
    """Multiply every element by a scalar."""
    rows, cols = get_dimensions(A)
    return [[A[i][j] * scalar for j in range(cols)] for i in range(rows)]


# ── Driver Code ──
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = [
    [1, 2],
    [3, 4],
    [5, 6]
]   # 3x2

D = [
    [7, 8],
    [9, 10],
    [11, 12]
]  # 3x2

print()
pretty_print(A, "Matrix A (3x3)")
pretty_print(B, "Matrix B (3x3)")

print("[+] A + B:")
pretty_print(matrix_add(A, B), "A + B")

print("[+] A - B:")
pretty_print(matrix_subtract(A, B), "A - B")

print("[+] A × B (3x3 × 3x3 → 3x3):")
pretty_print(matrix_multiply(A, B), "A × B")

# Non-square multiplication
E = [[1, 2, 3], [4, 5, 6]]    # 2x3
F = [[7, 8], [9, 10], [11, 12]]  # 3x2
print("[+] E (2x3) × F (3x2) → 2x2:")
pretty_print(matrix_multiply(E, F), "E × F")

print("[+] Scalar multiply A by 3:")
pretty_print(scalar_multiply(A, 3), "3 × A")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 2 — Transpose & Rotate Matrix
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Transpose a matrix (rows become columns) in-place for
        square matrices, or create new matrix for non-square.
    (b) Rotate a square matrix 90° clockwise in-place.
        Method: Transpose → Reverse each row.
    (c) Rotate a square matrix 90° anti-clockwise in-place.
        Method: Transpose → Reverse each column.
    (d) Rotate 180°.
"""

print("\n" + "=" * 60)
print("   ACTIVITY 2: Transpose & Rotate Matrix")
print("=" * 60)


def transpose(matrix):
    """
    Returns a new transposed matrix (works for any m×n).
    For square matrix: element at [i][j] moves to [j][i].
    """
    m, n = get_dimensions(matrix)
    return [[matrix[i][j] for i in range(m)] for j in range(n)]


def rotate_90_clockwise(matrix):
    """
    In-place rotation for square matrix.
    Step 1: Transpose
    Step 2: Reverse each row (mirror horizontally)
    """
    import copy
    mat = copy.deepcopy(matrix)
    n = len(mat)

    # Transpose in-place
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each row
    for row in mat:
        row.reverse()

    return mat


def rotate_90_anticlockwise(matrix):
    """
    In-place anti-clockwise rotation for square matrix.
    Step 1: Transpose
    Step 2: Reverse each column (mirror vertically)
    """
    import copy
    mat = copy.deepcopy(matrix)
    n = len(mat)

    # Transpose in-place
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each column
    for col in range(n):
        top, bot = 0, n - 1
        while top < bot:
            mat[top][col], mat[bot][col] = mat[bot][col], mat[top][col]
            top += 1
            bot -= 1

    return mat


def rotate_180(matrix):
    """Rotate 180° = apply 90° clockwise twice."""
    return rotate_90_clockwise(rotate_90_clockwise(matrix))


# ── Driver Code ──
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print()
pretty_print(M, "Original (3x3)")

T = transpose(M)
pretty_print(T, "Transposed")

r_cw = rotate_90_clockwise(M)
pretty_print(r_cw, "Rotated 90° Clockwise")

r_acw = rotate_90_anticlockwise(M)
pretty_print(r_acw, "Rotated 90° Anti-Clockwise")

r_180 = rotate_180(M)
pretty_print(r_180, "Rotated 180°")

# Non-square transpose
NS = [[1, 2, 3, 4], [5, 6, 7, 8]]   # 2×4
print("[+] Non-square transpose (2×4 → 4×2):")
pretty_print(NS, "Original 2×4")
pretty_print(transpose(NS), "Transposed 4×2")


# ──────────────────────────────────────────────────────────
#  ACTIVITY 3 — Spiral Order Traversal + Diagonal Sum
# ──────────────────────────────────────────────────────────
"""
Problem:
    (a) Traverse an m×n matrix in spiral order (layer by layer).
        Return elements as a flat list.
    (b) Find the sum of primary diagonal (top-left → bottom-right)
        and secondary diagonal (top-right → bottom-left).
    (c) Search for a value in a row-wise and column-wise
        sorted matrix using staircase search — O(m+n).
"""

print("\n" + "=" * 60)
print("   ACTIVITY 3: Spiral Traversal, Diagonal Sum & Staircase Search")
print("=" * 60)


def spiral_order(matrix):
    """
    Traverse matrix in spiral: right → down → left → up → repeat.
    Uses four boundary pointers: top, bottom, left, right.
    Time: O(m*n)  Space: O(1) extra (output list aside)
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right across top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse left across bottom row (if rows remain)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse up left column (if cols remain)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def diagonal_sums(matrix):
    """
    Primary diagonal:   matrix[i][i]
    Secondary diagonal: matrix[i][n-1-i]
    For non-square, only square part is considered.
    """
    n = min(len(matrix), len(matrix[0]))
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    return primary, secondary


def staircase_search(matrix, target):
    """
    Search in a matrix where each row and column is sorted.
    Start from top-right corner:
      - If current == target → found
      - If current > target  → move left
      - If current < target  → move down
    Time: O(m + n)
    """
    if not matrix or not matrix[0]:
        return (-1, -1)

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return (-1, -1)


# ── Driver Code ──
spiral_mat = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

print()
pretty_print(spiral_mat, "Matrix (4x4)")

spiral = spiral_order(spiral_mat)
print(f"  Spiral Order: {spiral}")
print(f"  Expected:     [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]")

p_sum, s_sum = diagonal_sums(spiral_mat)
print(f"\n  Primary Diagonal Sum   (1+6+11+16): {p_sum}")
print(f"  Secondary Diagonal Sum (4+7+10+13): {s_sum}")

# Staircase search
sorted_mat = [
    [ 1,  4,  7, 11],
    [ 2,  5,  8, 12],
    [ 3,  6,  9, 16],
    [10, 13, 14, 17]
]
pretty_print(sorted_mat, "\nSorted Matrix (row & col sorted)")

for target in [5, 9, 100, 1, 17]:
    pos = staircase_search(sorted_mat, target)
    found = f"Found at row={pos[0]}, col={pos[1]}" if pos != (-1,-1) else "Not found"
    print(f"  Search {target:3d}: {found}")

# Edge: 1×1 matrix
tiny = [[42]]
print(f"\n  Spiral of [[42]]: {spiral_order(tiny)}")
print(f"  Search 42 in [[42]]: {staircase_search(tiny, 42)}")
