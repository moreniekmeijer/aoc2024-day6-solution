

filename = 'input.txt'


with open(filename) as f:
    data = f.read()


def solve(data):
    lines = data.splitlines()
    height = len(lines)
    width = len(lines[0])

    # obstacle/start mapping
    obstacles = set()
    start = None
    for y in range(height):
        for x in range(width):
            if lines[y][x] == '^':
                start = (x, y)
            elif lines[y][x] == '#':
                obstacles.add((x, y))

    print(f"Start: {start}")
    print(f"Obstacles: {len(obstacles)} found")

    # directions: up, right, down, left (follows path turning right)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_index = 0

    position = start
    visited = set()
    visited.add(position)

    while True:
        dx, dy = directions[dir_index]
        next_pos = (position[0] + dx, position[1] + dy)

        # Check if next position is outside the grid
        if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
            break

        # Check if obstacle ahead
        if next_pos in obstacles:
            # turn right
            dir_index = (dir_index + 1) % 4
        else:
            # move forward
            position = next_pos
            visited.add(position)

    print(f"Visited {len(visited)} positions.")

    # Create new map with path
    output_grid = []
    for y in range(height):
        row = ""
        for x in range(width):
            pos = (x, y)
            if pos == start:
                row += "S"
            elif pos in obstacles:
                row += "#"
            elif pos in visited:
                row += "X"
            else:
                row += "."
        output_grid.append(row)

    output_text = "\n".join(output_grid)

    with open('output.txt', 'w') as f:
        f.write(output_text)

    return len(visited)


solve(data)
