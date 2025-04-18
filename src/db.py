from fs import search_and_replace
from os import getenv

from json import dumps, loads

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

def update_database_value(search_text, replace_text):
    db_path = get_db_file()
    search_and_replace(db_path, search_text, replace_text)

def add_shiny_entry(shiny_entry):
    db_path = get_db_file()
    try:
        # Read the entire file as a single string
        with open(db_path, "r") as file:
            db_content = file.read()

        # Find the 'shinies_found' key in the string
        if "shinies_found=" in db_content:
            # Extract the existing array
            start_index = db_content.index("shinies_found=") + len("shinies_found=")
            end_index = db_content.find("]", start_index) + 1  # Include the closing bracket
            existing_array_str = db_content[start_index:end_index].strip()

            # Remove the closing bracket to append the new entry
            existing_array_str = existing_array_str[:-1].strip()
            if existing_array_str.endswith(","):
                existing_array_str = existing_array_str[:-1].strip()

            # Add the new entry
            new_entry_str = f"{existing_array_str},\n\t{shiny_entry}\n]"

            # Replace the old array with the updated array in the string
            db_content = db_content[:start_index] + new_entry_str + db_content[end_index:]
        else:
            # If 'shinies_found' key is not found, add it to the end of the file
            new_entry_str = f"shinies_found=[{shiny_entry}]\n"
            db_content += new_entry_str

        # Write the updated content back to the file
        with open(db_path, "w") as file:
            file.write(db_content)

        print(f"Added shiny entry: {shiny_entry}")
    except FileNotFoundError:
        print(f"Error: Database file '{db_path}' not found.")
    except Exception as e:
        print(f"An error occurred while adding the shiny entry: {e}")

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