from utils.file_ops import list_files
from utils.json_handler import load_books
from utils.csv_handler import load_members
from utils.logger import log_activity

def run_library():
    print("📚 Library System Started\n")

    # Show files in data directory
    print("📂 Files in 'data' directory:")
    list_files("data")
    print()

    # Load and display books
    books = load_books("data/books.json")
    print("📘 Books Available:")
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Available: {book['available']}")
    print()

    # Load and display members
    members = load_members("data/members.csv")
    print("👥 Members Registered:")
    for member in members[1:]:  # Skip header row
        print(f"ID: {member[0]} | Name: {member[1]} | Email: {member[2]}")
    print()

    # Display log file contents
    print("📝 Log Information:")
    with open("data/logs.txt", "r") as log_file:
        for line in log_file:
            print(line.strip())
    print()

    # Log system initialization
    log_activity("Library system initialized")

if __name__ == "__main__":
    run_library()
