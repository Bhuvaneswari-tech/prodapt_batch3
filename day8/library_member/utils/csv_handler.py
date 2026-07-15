import csv

def load_members(file_path):
    with open(file_path, newline="") as f:
        reader = csv.reader(f)
        return list(reader)
