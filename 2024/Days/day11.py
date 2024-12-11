from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 11)

    def part_one(self):
        # self.input = self.test_input
        self.input = [int(char) for line in self.input for char in line.split(" ")]

        result = 0
        for stone in self.input:
            # result += self.blink(25, 0, stone)
            result += self.blink(25, 0, stone)

        print(result)

    def blink(self, max_blinks, blinks, stone):
        if blinks == max_blinks:
            return 1
        else:
            if stone == 0:
                return self.blink(max_blinks, blinks+1, 1)
            elif len(str(stone)) % 2 == 0:
                halflen_stone = len(str(stone)) // 2
                stone_left = stone // 10**halflen_stone
                stone_right = stone % 10**halflen_stone
                # stone_left = int(str(stone)[:halflen_stone])
                # stone_right = int(str(stone)[halflen_stone:])
                return self.blink(max_blinks, blinks+1, stone_left) + self.blink(max_blinks, blinks+1, stone_right)
            else:
                return self.blink(max_blinks, blinks+1, stone*2024)

    def part_two(self):
        self.input = self.restore
        # self.input = self.test_input
        self.input = [int(char) for line in self.input for char in line.split(" ")]

        dict = {}
        big_stones = self.input
        for blink in range(75):
            # print(big_stones, dict)
            new_dict = {}
            new_stones = []
            for stone in big_stones:
                if stone < 10:
                    dict[stone] = dict.get(stone,0)+1
                else:
                    if len(str(stone)) % 2 == 0:
                        halflen_stone = len(str(stone)) // 2
                        new_stones.append(stone // 10**halflen_stone)
                        new_stones.append(stone % 10**halflen_stone)
                    else:
                        new_stones.append(stone*2024)
            big_stones = new_stones

            for key, value in dict.items():
                if key == 0:
                    new_dict[1] = new_dict.get(key+1,0)+value
                elif len(str(key)) % 2 == 0:
                    halflen_stone = len(str(key)) // 2
                    new_dict[key // 10**halflen_stone] = new_dict.get(key // 10**halflen_stone,0)+value
                    new_dict[key % 10**halflen_stone] = new_dict.get(key % 10**halflen_stone,0)+value
                else:
                    new_dict[key*2024] = new_dict.get(key*2024,0)+value
            dict = new_dict
            
        result = sum(dict.values()) + len(big_stones)

        print(result)

Day()