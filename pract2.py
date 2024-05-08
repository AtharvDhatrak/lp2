from heapq import heappop, heappush

class Puzzle:
    def __init__(self, start):
        self.size = 3
        self.start = start

    def goal_state(self):
        return (1, 2, 3, 4, 0, 5, 6, 7, 8)

    def print_state(self, state):
        for i in range(0, len(state), self.size):
            print(state[i:i+self.size])
        print()

    def manhattan_distance(self, state):
        distance = 0
        goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2), 
                          4: (1, 0), 5: (1, 2), 6: (2, 0), 
                          7: (2, 1), 8: (2, 2), 0: (1, 1)}
        for i in range(self.size**2):
            if state[i] == 0:
                continue
            x, y = divmod(i, self.size)
            gx, gy = goal_positions[state[i]]
            distance += abs(x - gx) + abs(y - gy)
        return distance

    def get_neighbors(self, state):
        zero_index = state.index(0)
        x, y = divmod(zero_index, self.size)
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                n_index = nx * self.size + ny
                new_state = list(state)
                new_state[zero_index], new_state[n_index] = new_state[n_index], new_state[zero_index]
                neighbors.append(tuple(new_state))
        return neighbors

    def solve(self):
        pq = []
        heappush(pq, (self.manhattan_distance(self.start), 0, self.start))
        visited = set()
        visited.add(self.start)
        parents = {self.start: None}
        while pq:
            _, cost, current = heappop(pq)
            if current == self.goal_state():
                return self.reconstruct_path(current, parents)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parents[neighbor] = current
                    heappush(pq, (cost + 1 + self.manhattan_distance(neighbor), cost + 1, neighbor))
        return None

    def reconstruct_path(self, node, parents):
        path = []
        while node:
            path.append(node)
            node = parents[node]
        return path[::-1]

# Input processing
def input_state():
    print("Enter the initial state row by row, using 0 for the blank. Use space-separated format for each row:")
    state = []
    for i in range(3):
        row = input(f"Enter row {i+1}: ")
        state.extend(map(int, row.split()))
    return tuple(state)

# Example Usage
start_state = input_state()
puzzle = Puzzle(start_state)
print("Initial state:")
puzzle.print_state(start_state)
solution = puzzle.solve()
if solution:
    print("Solution path:")
    for step in solution:
        puzzle.print_state(step)
else:
    print("No solution found")

goal = puzzle.goal_state()
print("Goal state:")
puzzle.print_state(goal)
