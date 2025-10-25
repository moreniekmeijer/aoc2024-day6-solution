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

    while True:
        dx, dy = directions[dir_index]
        next_pos = (position[0] + dx, position[1] + dy)

        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
            break

        if next_pos in obstacles:
            dir_index = (dir_index + 1) % 4
        else:
            position = next_pos
            visited.add(position)

    return visited


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


def solve(data):
    width, height, obstacles, start = parse_map(data)
    visited = simulate_guard(width, height, obstacles, start)

    output_text = render_path(width, height, obstacles, start, visited)
    with open('output.txt', 'w') as f:
        f.write(output_text)

    print(f"Start: {start}")
    print(f"Obstacles: {len(obstacles)}")
    print(f"Visited: {len(visited)}")
    print("Output written to output.txt")


if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.read()
    solve(data)
