class SecurityThroughObscurity:

    def __init__(self, instructions):
        """
        :param input_file_name: input.txt
        """
        self.result_string = "northpole"
        self.ord_val = ord('a')
        self.instructions = instructions

    def find_sector_id(self):
        """
        :return: finds sector_id of each line and takes mod of sector_id and iterates line these many times. Checks
        for result_string i.e. northpole and returns sector_id if matched.
        """
        for line in self.instructions:
            encrypted_name = line.strip().split("-")
            room = ''.join(encrypted_name[:-1])
            sector_id = int(encrypted_name[-1].split("[")[0])
            result_st = ''.join(''.join(chr(((sector_id + (ord(j) - self.ord_val)) % 26) + self.ord_val) for j in i
                                        ) for i in room)
            if self.result_string in result_st:
                return sector_id


if __name__ == "__main__":
    import sys

    input = sys.stdin.readlines()
    instructions = [w.strip() for w in input]
    obj = SecurityThroughObscurity(instructions)
    result = obj.find_sector_id()
    print(result)
