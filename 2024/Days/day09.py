from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 9)

    def part_one(self):
        self.input = self.test_input
        self.input = [int(char) for line in self.input for char in line]

        cid = 0
        memory = []
        length = 0
        for i, num in enumerate(self.input):
            if i % 2 == 0:
                memory.extend([cid for _ in range(num)])
                cid += 1
                length += num
            elif i % 2 == 1:
                memory.extend(["." for _ in range(num)])

        cindex = len(memory)-1
        while memory.index(".") < cindex:
            if not str(memory[cindex]).isdigit():
                cindex -= 1
                continue
            ipoint = memory.index(".")
            memory[ipoint], memory[cindex] = memory[cindex], memory[ipoint]
        
        result = 0
        # Checksum
        for i, num in enumerate(memory):
            if num == ".":
                break
            result += i * num
            
        print(result)

    def part_two(self):
        self.input = self.restore
        # self.input = self.test_input
        self.input = [int(char) for line in self.input for char in line]
        self.input = self.input if len(self.input) % 2 == 1 else self.input.pop()

        # Make filesystem
        cid = 0
        memory = []
        for i, num in enumerate(self.input):
            if i % 2 == 0:
                memory.extend([cid for _ in range(num)])
                cid += 1
            elif i % 2 == 1:
                memory.extend(["." for _ in range(num)])

        # Move
        cid -= 1
        inum = -1
        while cid > 0:
            cnt = self.input[inum]
            icid = memory.index(cid)
            string_rep =  "".join(str(char)[0] for char in memory)
            if "." * cnt in string_rep:
                empty = string_rep.find("." * cnt)
                if empty < icid:
                    memory[icid:icid+cnt] = ["." for _ in range(cnt)]
                    memory[empty:empty+cnt] = [cid for _ in range(cnt)]
            # print(cid, inum, cnt, icid, empty, memory[:100])
            cid -= 1
            inum -= 2
        
        result = 0
        # Checksum
        for i, num in enumerate(memory):
            if num == ".":
                continue
            result += i * num
            
        print(result)

    def part_two2(self):
        self.input = self.restore
        # self.input = self.test_input
        self.input = [int(char) for line in self.input for char in line]
        self.input = self.input if len(self.input) % 2 == 1 else self.input.pop()

        # Make filesystem
        cid = 0
        memory = ""
        for i, num in enumerate(self.input):
            if i % 2 == 0:
                memory += f"{cid}" * num
                cid += 1
            elif i % 2 == 1:
                memory += "." * num

        # Move
        # Problem 99*2 is also 9999*1
        cid -= 1
        inum = -1
        while cid > 0:
            cnt = self.input[inum]
            icid = memory.index(f"{cid}")
            if "." * cnt in memory:
                empty = memory.index("." * cnt)
                if empty < icid:
                    memory = memory[:icid] + memory[icid:].replace(f"{cid}", ".", cnt)
                    memory = memory[:empty] + memory[empty:].replace(".", f"{cid}", cnt)
            cid -= 1
            inum -= 2
            
            # print(memory[:100])
            # exit()
        
        result = 0
        # Checksum
        for i, num in enumerate(memory):
            if num == ".":
                continue
            result += i * int(num)
            
        print(result)


Day()