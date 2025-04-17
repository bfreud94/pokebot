from fs import search_and_replace
from os import getenv

def get_db_file():
    db_file_path = getenv('DB_FILE_PATH')
    if db_file_path is None:
        raise ValueError("DB_FILE_PATH environment variable not set.")
    return db_file_path

def get_db_config():
    db_file_path = get_db_file()
    if db_file_path is not None:
        db_data = read_database(db_file_path)
        return db_data
    return None

def write_to_database(search_text, replace_text):
    db_path = get_db_file()
    search_and_replace(db_path, search_text, replace_text)

def read_database(file_path):
    data = {"total_encounters": 0, "last_shiny": 0}
    try:
        with open(file_path, "r") as file:
            for line in file:
                if line.startswith("total_encounters"):
                    data["total_encounters"] = int(line.split("=")[1].strip())
                elif line.startswith("last_shiny"):
                    data["last_shiny"] = int(line.split("=")[1].strip())
    except FileNotFoundError:
        print(f"Error: Database file '{file_path}' not found. Using default values.")
    except Exception as e:
        print(f"An error occurred while reading the database: {e}")
    return data