def to_string(grid):
    """
    Convert the grid to a string.
    """
    return "\n".join(
        " ".join(str(i) for i in row)
        for row in zip(*[iter(grid)] * size)
    )


def count_ships(seq, directions=(1, 2)):
    """
    Count the number of ships in the sequence given.
    """
    count = 0
    last = None
    for item in seq:
        if item in directions and item != last:
            count += 1
        last = item
    return count


def last_consecutive(seq, search=0):
    """
    Returns the length of the run of `search` from the end of the sequence.

    (i.e. how many `search`es it ends with)
    """
    count = 0
    for elem in seq[::-1]:
        if elem != search:
            break
        count += 1
    return count


def max_consecutive(seq, search=0):
    """
    Returns the maximum number of consecutive `search`es there are in the sequence.
    """
    count = 0
    hi = 0
    for item in seq:
        if item == search:
            count += 1
        else:
            count = 0
        if count > hi:
            hi = count
    return hi


def generate(board, size, ship_min, ship_max, col_info, row_info):
    """
    Generate valid result boards given the initial configuration info.

    board is a flat list containing the current board row by row
    0 = no ship
    1 = horizontal ship
    2 = vertical ship
    """

    if len(board) == size * size:
        yield board
        return

    rowi, coli = divmod(len(board), size)
    row = board[rowi * size : rowi * size + size]
    col = board[coli::size]

    # Number of occupied squares.
    row_occ_aim = row_info[0][rowi]
    col_occ_aim = col_info[0][coli]
    row_occ = row.count(1) + row.count(2)
    col_occ = col.count(1) + col.count(2)

    # Number of ships (or parts of ships).
    row_ships_aim = row_info[1][rowi]
    col_ships_aim = col_info[1][coli]
    row_ships = count_ships(row)
    col_ships = count_ships(col)

    # Maximum consecutive empty spaces.
    row_consec_aim = row_info[2][rowi]
    col_consec_aim = col_info[2][coli]
    row_consec = last_consecutive(row)
    col_consec = last_consecutive(col)

    # Check if placing any ship piece could be valid.
    if (
        # Ensure this placement wont go over the maximum occupation placements
        row_occ < row_occ_aim and
        col_occ < col_occ_aim
    ):
        # Check if placing a horizontal ship (1) would be valid.
        if (
            # Ensure this placement wont be adjacent to another ship
            (rowi == 0 or col[rowi - 1] == 0) and

            # Ensure this placement wont go over the maximum ship length
            last_consecutive(row, 1) < ship_max and

            # Ensure this placement wont go over the maximum ship placements
            (row_ships <= row_ships_aim or last_consecutive(row, 1) != 0)
        ):
            yield from generate(
                [*board, 1], size, ship_min, ship_max, col_info, row_info
            )

        # Check if placing a vertical ship (2) would be valid.
        if (
            # Ensure this placement wont be adjacent to another ship
            (coli == 0 or row[coli - 1] == 0) and

            # Ensure this placement wont go over the maximum ship length
            last_consecutive(col, 2) < ship_max and

            # Ensure this placement wont go over the maximum ship placements
            (col_ships <= col_ships_aim or last_consecutive(col, 1) != 0)
        ):
            yield from generate(
                [*board, 2], size, ship_min, ship_max, col_info, row_info
            )

    # Check if placing no ship (0) would be valid.
    if (
        # Ensure this placement wont make a ship that is under the minimum ship length
        (0 == last_consecutive(row, 1) or last_consecutive(row, 1) >= ship_min) and
        (0 == last_consecutive(col, 2) or last_consecutive(col, 2) >= ship_min) and

        # Ensure this placement wont mean there isn't enough space for the ships needed
        row_ships + (size - len(row)) > row_ships_aim and
        col_ships + (size - len(col)) > col_ships_aim and

        # Ensure this placement wont mean there isn't enough space for the occupied spaces needed
        row_occ + (size - len(row)) > row_occ_aim and
        col_occ + (size - len(col)) > col_occ_aim and

        # Ensure this placement doesn't go over the maximum number of consecutive spaces
        row_consec < row_consec_aim and 
        col_consec < col_consec_aim and

        # Ensure this placement doesn't mean there isn't enough space for the max consecutive spaces
        max(max_consecutive(row, 0), row_consec + (size - len(row))) >= row_consec_aim and
        max(max_consecutive(col, 0), col_consec + (size - len(col))) >= col_consec_aim
    ):
        yield from generate([*board, 0], size, ship_min, ship_max, col_info, row_info)


inp = open("5input.txt")
out = open("5output.txt", "w")

cases = int(inp.readline())

for case_number in range(cases):
    size, ship_min, ship_max = [int(i) for i in inp.readline().split()]

    col_info = [[int(i) for i in inp.readline().split()] for _ in range(3)]
    row_info = [[int(i) for i in inp.readline().split()] for _ in range(3)]

    gen = generate([], size, ship_min, ship_max, col_info, row_info)

    res = next(gen)

    for i in gen:
        print("broken")

    s = f"Case #{case_number+1}:\n{to_string(res).replace('2', '1')}\n"
    out.write(s)
    print(s)