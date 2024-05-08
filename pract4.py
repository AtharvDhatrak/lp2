def is_safe(queen_positions, row, col, n):
    """ Check if it's safe to place a queen at queen_positions[row][col]. """
    for i in range(row):
        if queen_positions[i] == col or \
           queen_positions[i] - i == col - row or \
           queen_positions[i] + i == col + row:
            return False
    return True

def print_solution(queen_positions, n):
    """ Print the board with queens placed. """
    for i in range(n):
        row = ['.'] * n
        row[queen_positions[i]] = 'Q'
        print(' '.join(row))
    print()

def backtracking_n_queens(row, queen_positions, n):
    """ Solve N-Queens problem and find all solutions using backtracking. """
    if row == n:
        print_solution(queen_positions, n)
        return  # Remove 'True' to avoid stopping after the first solution
    for col in range(n):
        if is_safe(queen_positions, row, col, n):
            queen_positions[row] = col
            backtracking_n_queens(row + 1, queen_positions, n)
            queen_positions[row] = -1


def branch_and_bound_n_queens(row, queen_positions, n):
    """ Solve N-Queens problem using branch and bound. """
    if row == n:
        print_solution(queen_positions, n)
        return True
    for col in range(n):
        if is_safe(queen_positions, row, col, n):
            queen_positions[row] = col
            branch_and_bound_n_queens(row + 1, queen_positions, n)
            queen_positions[row] = -1
    return False

def solve_n_queens(n, method='backtracking'):
    queen_positions = [-1] * n
    if method == 'backtracking':
        if not backtracking_n_queens(0, queen_positions, n):
            print("No solution found.")
    elif method == 'branch_and_bound':
        if not branch_and_bound_n_queens(0, queen_positions, n):
            print("No solution found.")

# Usage Example
n=int (input("enter no of queens"))# Number of queens and the size of the chessboard
print("Backtracking solution:")
solve_n_queens(n, method='backtracking')
print("Branch and Bound solution:")
solve_n_queens(n, method='branch_and_bound')

# def promising(row, col, n):
#     return (n - col) >= (n - row - 1)
