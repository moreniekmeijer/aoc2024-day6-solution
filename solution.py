def parse_map(data):
    lines = data.splitlines()
    height = len(lines)
    width = len(lines[0])

    obstacles = set()
    start = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '^':
                start = (x, y)
            elif char == '#':
                obstacles.add((x, y))

    return width, height, obstacles, start


def simulate_guard(width, height, obstacles, start):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_index = 0
    position = start

    visited = set()
    visited.add(start)

    visited_states = set()

    while True:
        state = (position[0], position[1], dir_index)
        if state in visited_states:
            return visited, True
        visited_states.add(state)

        dx, dy = directions[dir_index]
        next_pos = (position[0] + dx, position[1] + dy)

        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
            return visited, False

        if next_pos in obstacles:
            dir_index = (dir_index + 1) % 4
        else:
            position = next_pos
            visited.add(position)


# optional: function to render the path for visualization to a text file
def render_path(width, height, obstacles, start, visited):
    output_lines = []
    for y in range(height):
        row = []
        for x in range(width):
            pos = (x, y)
            if pos == start:
                row.append('S')
            elif pos in obstacles:
                row.append('#')
            elif pos in visited:
                row.append('X')
            else:
                row.append('.')
        output_lines.append(''.join(row))
    return '\n'.join(output_lines)


def find_loops(width, height, obstacles, start):
    visited, _ = simulate_guard(width, height, obstacles, start)
    possible_loops = 0

    for pos in visited:
        if pos == start:
            continue

        new_obstacles = set(obstacles)
        new_obstacles.add(pos)

        _, loop_detected = simulate_guard(width, height, new_obstacles, start)
        if loop_detected:
            possible_loops += 1

    return possible_loops


def solve(data):
    width, height, obstacles, start = parse_map(data)
    visited, _ = simulate_guard(width, height, obstacles, start)

    output_text = render_path(width, height, obstacles, start, visited)
    with open('output.txt', 'w') as f:
        f.write(output_text)

    print(f"Visited positions (part 1): {len(visited)}")

    possible_loops = find_loops(width, height, obstacles, start)
    print(f"Possible loops (part 2): {possible_loops}")


if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.read()
    solve(data)
