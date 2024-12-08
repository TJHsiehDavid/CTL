import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = BASE_DIR + "/task.json"

def write_data_to_json(tag, new_data):
    """
    Write a dictionary to a JSON file.
    
    Args:
        new_data (dict): The dictionary to be written to the JSON file.
    """
    try:
        # Try to read existing data (if the file exists)
        try:
            with open(TASK_FILE, 'r') as file:
                # Load existing data
                existing_data = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, start with an empty dictionary
            existing_data = {}
        print(existing_data)
        if tag == 'add':
            # If existing_data is a dictionary, update it
            if isinstance(existing_data, dict):
                existing_data.update(new_data)
        elif tag == 'delete':
            # If existing_data is a dictionary, remove the specified task
            if isinstance(existing_data, dict) and new_data in existing_data:
                del existing_data[new_data]
        elif tag == 'update':
            # If existing_data is a dictionary, update the specified task
            if isinstance(existing_data, dict) and new_data in existing_data:
                existing_data[new_data].update(new_data)
        elif tag == 'mark-in-progress':
            if isinstance(existing_data, dict) and new_data in existing_data:
                existing_data[new_data]['status'] = 'in-progress'
        elif tag == 'mark-todo':
            if isinstance(existing_data, dict) and new_data in existing_data:
                existing_data[new_data]['status'] = 'todo'
        elif tag == 'mark-done':
            if isinstance(existing_data, dict) and new_data in existing_data:
                existing_data[new_data]['status'] = 'done'
        
        # Write the updated data back to the file
        with open(TASK_FILE, 'w') as file:
            json.dump(existing_data, file, indent=4)
        
        print("Data successfully written to data.json")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def ensure_task_file_exists():
    """檢查 JSON 文件是否存在，如果不存在則創建一個空文件。"""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump({}, f)
        print(f"文件 {TASK_FILE} 已創建。")

