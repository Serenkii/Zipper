import os.path
from enum import Enum

import renamer


def ask_yes_no(prompt: str) -> bool:
    if not prompt.endswith("(y/n)") or not prompt.endswith("(n/y)"):
        prompt = prompt.strip() + " (y/n)"
    user_input = input(f"{prompt}\n")
    user_input = user_input.strip().lower()
    if user_input == "yes" or user_input == "true" or user_input == "y":
        return True
    if user_input == "no" or user_input == "false" or user_input == "n":
        return False
    print("Your argument was not valid!")
    return ask_yes_no(prompt)


def ask_for_directory(prompt: str):
    user_input = input(f"{prompt}\n")
    user_input = user_input.strip()
    if user_input.lower() == "exit" or user_input.lower() == "quit" \
            or user_input.lower() == "nvm" or user_input.lower() == "back":
        return False
    if not os.path.exists(user_input):
        print(f"The specified path does not exist! (\"{user_input}\")")
        return ask_for_directory(prompt)
    if not os.path.isdir(user_input):
        print(f"The specified path is no directory! (\"{user_input}\")")
        return ask_for_directory(prompt)
    return user_input


def ask_for_string(prompt: str, new_line=True):
    print(f"{prompt}", end="")
    if new_line:
        print()
    user_input = input()
    user_input = user_input.strip()
    if user_input.lower() == "exit" or user_input.lower() == "quit" \
            or user_input.lower() == "nvm" or user_input.lower() == "back":
        return False
    return user_input


class Decision(Enum):
    ZIP_DIR = 1
    ZIP_DIR_COND = 2
    RENAME = 3
    UNZIP = 4
    UNZIP_TO_DIR = 5
    EXIT = 6


def decide_action():
    print("\nWhat do you want to do?\n"
          "1) Zip a directory\n"
          "2) Zip a directory with custom conditions\n"
          "3) Rename all files in a directory according to a rule\n"
          "4) Unzip a zip-file\n"
          "5) Unzip a zip-file to a specified folder\n"
          "6) Exit the program")
    user_input = input("What do you want to do? [1-6]\n")
    user_input = user_input.strip()
    if not user_input.isdecimal():
        print("Your choice is not a number.")
        return decide_action()
    user_input = int(user_input)
    if not 1 <= user_input <= 6:
        print("Your choice (number) is not between 1 and 6!")
        return decide_action()
    return Decision(user_input)


def ask_for_renaming_action():
    print("\nWhat renaming action do you want to perform?\n"
          "1) Only allow ASCII-characters\n"
          "2) Make all file names lower case\n"
          "3) Make all file names upper case\n"
          "4) Remove all whitespace\n"
          "5) Replace all whitespace with underscore (\"_\")\n"
          "6) Remove all leading and trailing whitespace\n"
          "7) Formulate a custom rule. (Python lambda)")
    user_input = input("What do you want to do? [1-7]\n")
    user_input = user_input.strip()
    if not user_input.isdecimal():
        print("Your choice is not a number.")
        return decide_action()
    user_input = int(user_input)
    if not 1 <= user_input <= 7:
        print("Your choice (number) is not between 1 and 7!")
        return decide_action()
    return renamer.Rule(user_input)

# TODO: Make dictionaries with these lambdas as keys and possibilities as values, so one method can be used for both
#  of those methods
