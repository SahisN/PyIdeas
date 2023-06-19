import os
from python_keeper import Notes


def clear():
    os.system("cls")


def create_note(notes):
    title = input("Title: ")
    description = input("Description: ")
    completed = input("Completed?: ")
    print("\n" + Notes.display_notes([[title, description, completed]]) + "\n")

    confirm = input("Do you want to save this? (Y/n)?: ").lower()

    if confirm == "y" or confirm == "yes":
        notes.append_notes(title, description, completed)


def delete_note(notes):
    print(notes)


def run():
    notes = Notes()

    while True:
        key = input("Python Keep > ")

        if key == "exit" or key == "q":
            print("Saving...")
            notes.write_saves()
            break

        elif key == "list" or key == "ls":
            print("\n")
            notes.list_notes()
            print("\n")

        # adding notes from dictonary
        elif key == "create":
            clear()
            create_note(notes)

        # deleting notes from dictonary
        elif key.split()[0] == "delete":
            if len(key.split()) == 2:
                print(notes.delete_notes(key.split()[1]) + "\n")

            elif len(key.split()) > 2:
                print("Delete only accepts a single parameter {key} \n")

            else:
                print("missing 'key' entry name \n")

        elif key == "cls" or key == "clear":
            clear()

        else:
            print(f"'{key}' is not recognized as an internal or external command \n")


if __name__ == "__main__":
    run()
