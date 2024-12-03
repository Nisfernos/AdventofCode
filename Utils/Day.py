class DayFormat():

    def __init__(self, year: int, day: int) -> None:
        day = f"{day:02d}"
        self.input = self.parse_input(f"{year}\\Input\\day{day}.txt")
        self.test_input = self.parse_input(f"{year}\\Input\\test.txt")
        self.part_one()
        self.part_two()

    def parse_input(self, text_file) -> None:
        with open(text_file) as txt:
            return txt.read().splitlines()

    def part_one(self):
        pass

    def part_two(self):
        pass
        