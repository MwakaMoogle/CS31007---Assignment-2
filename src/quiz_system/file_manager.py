import json

class FileManager:
    def load_from_file(self, filename):
        file_json = json.load(filename)