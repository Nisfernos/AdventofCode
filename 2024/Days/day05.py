from Utils.Day import DayFormat


class Day(DayFormat):

    def __init__(self) -> None:
        super().__init__(2024, 5)

    def part_one(self):
        rules = []
        is_rule = True
        updates = []
        for line in self.input:
            if line == "":
                is_rule = False
                continue
            if is_rule:
                a,b = line.split("|")
                rules.append((int(a),int(b)))
            else:
                updates.append([int(x) for x in line.split(",")])
        result = 0
        for page in updates:
            if all([page.index(rule[0]) < page.index(rule[1]) for rule in rules if all([number in page for number in rule])]):
                result += page[len(page)//2]
        print(result)


    def part_two(self):
        rules = []
        is_rule = True
        updates = []
        for line in self.input:
            if line == "":
                is_rule = False
                continue
            if is_rule:
                a,b = line.split("|")
                rules.append((int(a),int(b)))
            else:
                updates.append([int(x) for x in line.split(",")])
        result = 0
        for page in updates:
            if not all([page.index(rule[0]) < page.index(rule[1]) for rule in rules if all([number in page for number in rule])]):
                # print(page, 0)
                begin = 0
                i = begin + 1
                while begin < len(page)-1:
                    # print(0, begin, i, len(page))
                    if (page[i], page[begin]) in rules:
                        page[begin],page[i] = page[i],page[begin]
                        i = begin + 1
                        continue
                    i += 1
                    # print(1, begin, i, len(page))
                    if i == len(page):
                        begin += 1
                        i = begin + 1
                result += page[len(page)//2]
        print(result)


Day()