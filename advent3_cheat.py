with open(r'aoc_19_03.txt', 'r') as f:
    raw_input = f.read()

def traverse_wire(wire):
    wire_info = {}
    x, y, count = 0, 0, 0
    directions =  {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    for part in wire:
        for _ in range(int(part[1:])):
            offset = directions[part[0]]
            x += offset[0]
            y += offset[1]
            count += 1
            wire_info[(x, y)] = count
    return wire_info

def solutions(raw_input):
    wires = [x.split(',') for x in raw_input.strip().split('\n')]

    wire_one = traverse_wire(wires[0])
    wire_two = traverse_wire(wires[1])

    crossings = wire_one.keys() & wire_two.keys()

    fewest_steps = min(crossings, key=lambda x: wire_one[x] + wire_two[x])
    steps = wire_one[fewest_steps] + wire_two[fewest_steps]

    closest = min([intersection for intersection in crossings], key=lambda x: abs(x[0]) + abs(x[1]))
    distance = abs(closest[0]) + abs(closest[1])

    return ('day one', distance, 'day two', steps)

print(solutions(raw_input))