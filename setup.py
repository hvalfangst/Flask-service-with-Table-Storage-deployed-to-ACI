import json

key = ""

# Attempt to read existing list of json contained in file 'result.json'
try:
    with open("result.json", "r") as result_file:
        list_of_two_json = json.load(result_file)
        first_json = list_of_two_json[0]
        key = first_json["value"]

except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")
except FileNotFoundError:
    print("File 'result.json' not found.")
except IndexError:
    print("Index error: The list is empty or doesn't have an element at index 0.")
except KeyError as e:
    print(f"KeyError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Directly update the connection_string in the config.json file
try:
    with open("python/config.json", "r+") as config_file:
        config_data = json.load(config_file)
        config_data["credential"]["key"] = key
        config_file.seek(0)  # Move the file cursor to the beginning
        json.dump(config_data, config_file, indent=2)
        config_file.truncate()  # Truncate the file to remove any remaining content (if shorter)
        print("Updated config.json with the new key.")
except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")
except FileNotFoundError:
    print("File 'config.json' not found.")
except KeyError as e:
    print(f"KeyError: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")