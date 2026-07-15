import json

def load_books(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
