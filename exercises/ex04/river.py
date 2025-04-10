"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        count = 0
        while count <= amount and len(self.fish) > 0:
            self.fish.pop(0)
            count += 1

    def check_ages(self):
        surviving_fish = [fish for fish in self.fish if fish.age <= 3]
        self.fish = surviving_fish
        surviving_bears = [bear for bear in self.bears if bear.age <= 3]
        self.bears = surviving_bears

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:  # checking for atleast 5 fish
                self.remove_fish(3)  # remove 3 fish from the river
                bear.eat(3)  # bear eats 3 fish

    def check_hunger(self):
        surviving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears

    def repopulate_fish(self):
        new_fish = (len(self.fish) // 2) * 4  # each pair of fish produces 4 offspring
        for _ in range(new_fish):
            self.fish.append(Fish())  # append each new fish one by one

    def repopulate_bears(self):
        new_bears = len(self.bears) // 2  # each pair of bears produces 1 cub
        for _ in range(new_bears):
            self.bears.append(Bear())  # append each new bear one by one

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
