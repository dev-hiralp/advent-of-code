from collections import defaultdict
import os


class BalanceBots:
    def __init__(self, instructions):
        """
        :param file_name: input.txt
        """
        self.microchips_value = [17, 61]
        self.bots_lst = defaultdict(list)
        self.instructions = instructions

    def is_proceed(self, temp_bot: str):
        """
        :param temp_bot: bot number
        :return: return 1 if bot procured 2 microchips, else 0
        """
        if len(self.bots_lst[temp_bot]) == 2:
            return 1
        else:
            return 0

    def is_done(self, temp_bot: str):
        """
        :param temp_bot: bot number
        :return: return 1 if bot microchips match with microchips_value
        """
        if self.bots_lst[temp_bot] == self.microchips_value:
            return 1

    def handle_robot(self):
        """
        :param input_string: list of puzzle input
        :return: list of bots and their respective chips
        """
        for string in self.instructions:
            keys = string.split()
            if keys[0] == 'value':
                val, bot = int(keys[1]), keys[-1]
                self.bots_lst[bot].append(val)
                self.bots_lst[bot].sort()
                if self.bots_lst[bot] == self.microchips_value:
                    break

            elif keys[0] == 'bot':
                bot = keys[1]
                if self.is_proceed(bot):
                    if keys[5] == 'bot':
                        self.bots_lst[keys[6]].append(self.bots_lst[bot][0])
                        self.bots_lst[keys[6]].sort()
                        if self.is_done(bot):
                            break

                    if keys[-2] == 'bot':
                        self.bots_lst[keys[-1]].append(self.bots_lst[bot][1])
                        self.bots_lst[keys[-1]].sort()
                        if self.is_done(bot):
                            break
                else:
                    self.instructions.append(string)

            else:
                raise Exception("Invalid input")

        for b in self.bots_lst:
            if self.bots_lst[b] == self.microchips_value:
                return int(b)
        return 0


if __name__ == "__main__":
    import sys

    input = sys.stdin.readlines()
    instructions = [w.strip() for w in input]
    obj = BalanceBots(instructions)
    result = obj.handle_robot()
    print(result)
