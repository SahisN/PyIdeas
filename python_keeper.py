import os
import pickle
from tabulate import tabulate


class Notes:
    folder = "./data"
    file = "./data/notes.pickle"

    def __init__(self):
        # if the folder exist. Check for file 'notes.pickle'

        if os.path.exists(self.folder):
            # if the file 'notes.pickle' exists then load it

            if os.path.isfile("./data/notes.pickle"):
                self.notes = self.read_saves()

            # if the file doesn't exist, create an empty dict

            else:
                self.notes = {}

        # if the folder 'data' does not exists. Make a new folder name 'data'

        else:
            os.mkdir("data")
            self.notes = {}

    def append_notes(self, title, description, isCompleted):
        # self.notes[title] = [title, description, isCompleted]
        self.notes.update({title: [title, description, isCompleted]})
        # self.write_saves(self.notes)

    def list_notes(self):
        # get title, description, isCompleted from dictonary
        data = []
        for title, description in zip(self.notes.keys(), self.notes.values()):
            data += [[title, description[1], description[2]]]

        # import the data to tabulate and display the table
        headers = ["Title", "Description", "isCompleted"]
        table = tabulate(data, headers, tablefmt="presto")
        print(table)

    @staticmethod
    def display_notes(data):
        return tabulate(
            data, headers=["Title", "Description", "isCompleted"], tablefmt="presto"
        )

    def delete_notes(self, key):
        if self.notes.get(key) != None:
            self.notes.pop(key)
            return f"entry '{key}' is deleted"

        else:
            return f"entry '{key}' does not exist"

    def edit_notes():
        pass

    def read_saves(self):
        try:
            with open("./data/notes.pickle", "rb") as file:
                notes = pickle.load(file)
                return notes

        except:
            print("Unable to open notes.picke. Check if folder 'data' exists")

    def write_saves(self):
        try:
            with open("./data/notes.pickle", "wb") as file:
                pickle.dump(self.notes, file)

        except:
            print("Unable to save notes. Check if folder 'data' exists")
