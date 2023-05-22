import json

class JsonReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path) as file:
            data = json.load(file)
        return data
