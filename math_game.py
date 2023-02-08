from random import randint


class MathGame:
    """Blueprint for a game.
    Game has 4 mode addition, subtraction, division, multiplication
    """

    def __init__(self, mode, level = "easy", max_num=50, games=20):
        self.mode = mode
        self.level = level
        self.games = games
        self.correct_answer = 0
        self.counter = 1
        self.max_num = max_num

    def set_level(self, level):
        self.level = level
        if self.level == "hard":
            self.games = 50
            self.max_num = 100


    def play_game(self):
        """Play a game of the specified mode type."""
        for _ in range(self.games):
            num1, num2 = self.generate_numbers()
            for _ in range(3):
                try:
                    answer = int(
                        input(f"Question {self.counter}: {num1} {self.mode} {num2} = ")
                    )
                    if self.check_answer(answer, num1, num2):
                        print("Correct!")
                        self.correct_answer += 1
                        break
                    else:
                        print("Incorrect!")
                except ValueError:
                    print("Incorrect input! Please enter a valid number.")
            self.counter += 1
        print(f"{self.correct_answer} / {self.games}")

    def generate_numbers(self):
        """Generate two random numbers for the specified mode."""
        if self.mode == "+":
            while True:
                num1 = randint(1, self.max_num)
                num2 = randint(1, self.max_num)
                if (num1 + num2) <= self.max_num:
                    break
        elif self.mode == "-":
            while True:
                num1 = randint(1, self.max_num)
                num2 = randint(1, self.max_num)
                if num1 > num2:
                    break
        elif self.mode == "/":
            while True:
                num1 = randint(1, self.max_num)
                num2 = randint(1, 10)
                if (num1 > num2) and (num1 % num2 == 0) and ((num1 / num2) <= 10):
                    break
        elif self.mode == "*":
            num1 = randint(1, 10)
            num2 = randint(1, 10)
        return num1, num2

    def check_answer(self, answer, num1, num2):
        """Check if the answer is correct for the specified mode."""
        if self.mode == "+":
            return answer == (num1 + num2)
        elif self.mode == "-":
            return answer == (num1 - num2)
        elif self.mode == "/":
            return answer == (num1 / num2)
        elif self.mode == "*":
            return answer == (num1 * num2)
