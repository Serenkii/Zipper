import os
import os.path
import re
from enum import Enum
from pathlib import Path

import inputmanager


class Rule(Enum):
    ONLY_ASCII = 1
    TO_LOWER = 2
    TO_UPPER = 3
    REMOVE_WHITESPACE = 4
    REPLACE_WHITESPACE = 5
    REMOVE_LEADING_TRAILING_WHITESPACE = 6
    CUSTOM_LAMBDA = 7


class Renamer:
    def __init__(self, path: str):
        if not os.path.exists(path):
            raise Exception(f"The path does not exist! (\"{path}\")")
        if not os.path.isdir(path):
            raise Exception(f"The named path is no directory! (\"{path}\")")
        self.__root = Path(path)

    @property
    def root(self):
        return self.__root

    def rename_files(self, rule=Rule.ONLY_ASCII):
        match rule:
            case Rule.ONLY_ASCII:
                self.__rename_all(lambda file_name: re.sub(r"[^ -~]", "_", file_name))  # https://fckaf.de/nM6

            case Rule.TO_LOWER:
                self.__rename_all(lambda file_name: str(file_name).lower())

            case Rule.TO_UPPER:
                self.__rename_all(lambda file_name: str(file_name).upper())

            case Rule.REMOVE_WHITESPACE:
                self.__rename_all(lambda file_name: "".join(substring.strip() for substring in str(file_name).split()))

            case Rule.REPLACE_WHITESPACE:
                self.__rename_all(lambda file_name: re.sub(r"\s+", "_", file_name))

            case Rule.REMOVE_LEADING_TRAILING_WHITESPACE:
                self.__rename_all(lambda file_name: str(file_name).strip())

            case Rule.CUSTOM_LAMBDA:
                prefix = "lambda file_name: "
                user_input = inputmanager.ask_for_string(
                    f"Type in your lambda expression. (lambda file_name: file_name.lower()) e.g.)\n$ {prefix}",
                    new_line=False)

                if isinstance(user_input, bool) and not user_input:
                    return
                try:
                    self.__rename_all(eval(f"{prefix}{user_input}"))
                except (SyntaxError, NameError, TypeError):
                    print("No valid lambda expression!")
                    self.rename_files(Rule.CUSTOM_LAMBDA)
        print("ok")

    def __rename_all(self, rule):
        for directory_path, dirs, files in os.walk(self.__root):
            for file in files:
                if True:
                    Renamer.__rename_file(directory_path, file, all_files_in_dir=files, function=rule)

    @staticmethod
    def __rename_file(directory_path, file_name: str, all_files_in_dir: list, function):
        other_files_in_dir = all_files_in_dir.copy()  # lists are mutable!
        other_files_in_dir.remove(file_name)

        new_name = file_name  # strings are immutable

        new_name = new_name.strip()
        new_name = function(new_name)

        if new_name in other_files_in_dir:
            new_name = f"{new_name}_0"
            while new_name in other_files_in_dir:
                counter = 0
                new_name = new_name.removesuffix(f"_{counter}")
                counter += 1
                new_name = f"{new_name}_{counter}"

        if file_name != new_name:
            complete_file_path = os.path.join(directory_path, file_name)
            complete_file_path_new = os.path.join(directory_path, new_name)

            os.rename(complete_file_path, complete_file_path_new)


