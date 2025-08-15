from util.print_fns import print_with_time

def search_and_replace(file_path, search_text, replace_text):
    try:
        # Read the file content
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the text
        updated_content = content.replace(search_text, replace_text)

        # Write the updated content back to the file
        with open(file_path, "w") as file:
            file.write(updated_content)

        print_with_time(f"Replaced '{search_text}' with '{replace_text}' in {file_path}.")
    except FileNotFoundError:
        print_with_time(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print_with_time(f"An error occurred: {e}")