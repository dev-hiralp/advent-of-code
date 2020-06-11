class NoTaxicab:
    def __init__(self, instructions):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.turn = {'R': lambda x: (x + 1) % 4, 'L': lambda x: (x - 1) % 4}
        self.instructions = instructions

    def block_dist_slover(self):
        """
        :Calculates the number of blocks away from the first location

        Returns:
            int: Number of blocks
        """
        current_dir = 0  # facing north
        current_loc = (0, 0)  # origin
        for turn in self.instructions:
            l_r, dist = turn[0], int(turn[1:])
            current_dir = self.turn[l_r](current_dir)
            current_loc = (current_loc[0] + self.directions[current_dir][0] * dist,
                           current_loc[1] + self.directions[current_dir][1] * dist)
        return abs(current_loc[0]) + abs(current_loc[1])


if __name__ == "__main__":
    input = input()
    instructions = [w.strip() for w in input.split(',')]
    obj = NoTaxicab(instructions)
    result = obj.block_dist_slover()
    print(result)
