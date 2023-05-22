import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        with open(self.file_path) as file:
            data = json.load(file)
        return data
