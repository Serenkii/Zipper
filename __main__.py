from renamer import Renamer
import inputmanager
from inputmanager import Decision
import zipper


def zip_dir():
    folder = inputmanager.ask_for_directory("What directory should be zipped?")
    if isinstance(folder, bool) and not folder:
        return
    zipper.easy_zip(folder)


def zip_dir_conditions():
    print("Not implemented yet.")
    pass


def rename_files_in_dir():
    directory = inputmanager.ask_for_directory("In what directory should the files be renamed?")
    if isinstance(directory, bool) and not directory:
        return
    renamer = Renamer(directory)
    renamer.rename_files(inputmanager.ask_for_renaming_action())
    pass


def unzip():
    print("Not implemented yet.")
    pass


def unzip_to_dir():
    print("Not implemented yet.")
    pass


def exit_program():
    if inputmanager.ask_yes_no("Are you sure you want to exit the program?"):
        exit(0)


if __name__ == '__main__':
    while True:
        decision = inputmanager.decide_action()
        match decision:
            case Decision.ZIP_DIR:
                zip_dir()
                pass
            case Decision.ZIP_DIR_COND:
                zip_dir_conditions()
                pass
            case Decision.RENAME:
                rename_files_in_dir()
                pass
            case Decision.UNZIP:
                unzip()
                pass
            case Decision.UNZIP_TO_DIR:
                unzip_to_dir()
                pass
            case Decision.EXIT:
                exit_program()
                pass
