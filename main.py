from math_game import MathGame
import sys
def main():
    print("Welcome to the MathGame")
    print("A place where you can practise math")
    print("by doing some additon, subtraction, division, multiplication exercises")
    while True:
        print("""Plese choose one of the following:
          Press 1 for addition game,
          Press 2 for subtraction game,
          Press 3 for division game,
          Press 4 for subtraction game,
          Press 5 to QUIT game.""")
        game = input()
        if game in ("1","2","3","4"):
            x = MathGame("+-/*"[int(game) - 1])
            while True:
                print("Please select difficulty: type in easy or hard: ")
                mode = input().lower()
                if mode == "hard" or mode.startswith("h"):
                    x.set_level("hard")
                    break
                elif mode == "easy" or mode.startswith("e"):
                    break
                else:
                    print("Incorrect input!")
            x.play_game()
        elif game == "5":
            sys.exit("Thank you for playing!")
        while True:
            print("Would you like to play again? ")
            choice = input("Please type in YES/NO: ").lower()
            if choice.startswith("y"):
                break
            elif choice.startswith("n"):
                sys.exit("Thank you for playing, see you next time!")

if __name__ == "__main__":
    main()
