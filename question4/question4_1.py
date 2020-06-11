from collections import Counter
import os


class SecurityThroughObscurity:

    def __init__(self, instructions):
        """
        :param input_file_name: input.txt
        """
        self.result_sum = 0
        self.input_file_lst = []
        self.instructions = instructions

    def calculate_sum_for_real_rooms(self):
        """
        :return: calculates result_sum and retuns
        """
        for line in self.instructions:
            encrypted_name = line.strip().split("-")
            room = ''.join(encrypted_name[:-1])
            sector_id = int(encrypted_name[-1].split("[")[0])
            checksum = encrypted_name[-1].split("[")[1].replace("]", "")
            rooms = ''.join([st[0] for st in sorted(Counter(room).most_common(),
                                                    key=lambda x: (-x[1], x[0]))])[0:5]
            if rooms == checksum:
                self.result_sum += sector_id

        return self.result_sum


if __name__ == "__main__":
    import sys

    input = sys.stdin.readlines()
    instructions = [w.strip() for w in input]
    obj = SecurityThroughObscurity(instructions)
    result = obj.calculate_sum_for_real_rooms()
    print(result)
