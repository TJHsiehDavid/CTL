from datetime import datetime
from utils import write_data_to_json, ensure_task_file_exists, displayList
from dataStructure import TaskID, TaskInfo

task_id = 1

def task_action(action, id, task, TaskID):
    global task_id
    
    if action == 'add':
        TaskID[str(task_id)] = TaskInfo().__dict__

        TaskID[str(task_id)]['id'] = task_id
        TaskID[str(task_id)]['description'] = task
        TaskID[str(task_id)]['status'] = 'todo'
        TaskID[str(task_id)]['createdAt'] = TaskID[str(task_id)]['updatedAt'] = datetime.now().isoformat()

        write_data_to_json(action, id, TaskID)
        task_id += 1
    elif action == 'list':
        # 確保 JSON 文件存在
        data = ensure_task_file_exists()
        if data is not None:
            displayList(action, data, task)
        else:
            print("無法讀取 task.json。")
    else:
        if action == 'update':
            TaskID[id]['description'] = task
            TaskID[id]['updatedAt'] = datetime.now().isoformat()
        else:
            TaskID[id]['updatedAt'] = datetime.now().isoformat()


        write_data_to_json(action, id, TaskID)




def main():
    global task_id
    try:
        # 確保 JSON 文件存在
        data = ensure_task_file_exists()
        if data is not None:
            orginal_file_data = data
            task_id = len(data) + 1
        id = None

        while True:
            user_input = input()
            # 將輸入以空格為分隔符拆分
            if "update" in user_input:
                parts = user_input.split(' ', 2)
                action = parts[0]
                id = parts[1]
                task = parts[2]
            elif "list" in user_input:
                parts = user_input.split(' ', 1)
                if len(parts) > 1:
                    action = parts[0]
                    id = None
                    task = parts[1]
                else:
                    action = parts[0]
                    id = None
                    task = None
            elif "mark" in user_input:
                parts = user_input.split(' ', 1)
                action = parts[0]
                id = parts[1]
                task = None
            else:
                parts = user_input.split(' ', 1)
                action = parts[0]
                task = parts[1]

            
            if action == 'add':
                task_action(action, id, task, orginal_file_data)
            elif action == 'delete':
                task_action(action, id, task, orginal_file_data)
            elif action == 'update':
                task_action(action, id, task, orginal_file_data)
            elif action == 'mark-in-progress' or action == 'mark-todo' or action == 'mark-done':
                task_action(action, id, task, orginal_file_data)
            elif action == 'list':
                task_action(action, id, task, orginal_file_data)
    except ValueError as e:
            print(f"錯誤：{e}。請重新輸入正確的選項！")


if __name__ == "__main__":
    main()