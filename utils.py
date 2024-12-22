import json
import os
from dataStructure import TaskID

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = BASE_DIR + "/task.json"

def write_data_to_json(tag, id, new_data):
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
            if isinstance(existing_data, dict) and int(id) in existing_data[id].values():
                existing_data[id]['description'] = new_data[id]['description']
                existing_data[id]['updatedAt'] = new_data[id]['updatedAt']
        elif tag == 'mark-in-progress':
            if isinstance(existing_data, dict):
                existing_data[id]['status'] = 'in-progress'
                existing_data[id]['updatedAt'] = new_data[id]['updatedAt']
        elif tag == 'mark-todo':
            if isinstance(existing_data, dict):
                existing_data[id]['status'] = 'todo'
                existing_data[id]['updatedAt'] = new_data[id]['updatedAt']
        elif tag == 'mark-done':
            if isinstance(existing_data, dict):
                existing_data[id]['status'] = 'done'
                existing_data[id]['updatedAt'] = new_data[id]['updatedAt']
        else:
            raise ValueError(f"錯誤：{e}。請重新輸入正確的選項！")
        
        # Write the updated data back to the file
        with open(TASK_FILE, 'w') as file:
            json.dump(existing_data, file, indent=4)
        
        print("Data successfully written to data.json")
    
    except ValueError as e:
        print(f"錯誤：{e}。請重新輸入正確的選項！")
        


def displayList(action, TaskDict , task):
    for key, value in TaskDict.items():
        if (value['status'] == task or task == None) and value['id'] is not None:
            print(TaskDict[key])
       


def ensure_task_file_exists():
    data = TaskID
    """檢查 JSON 文件是否存在，如果不存在則創建一個空文件。"""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump({}, f)
        print(f"文件 {TASK_FILE} 已創建。")
    else:
        with open('task.json') as f:
            data = json.load(f)
    return data

