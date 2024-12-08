from datetime import datetime
from utils import write_data_to_json, ensure_task_file_exists
from dataStructure import TaskID, TaskInfo

task_id = 1

def task_action(action, task):
    global task_id
    TaskID[str(task_id)] = TaskInfo().__dict__
    
    if action == 'add':
        TaskID[str(task_id)]['id'] = task_id
        TaskID[str(task_id)]['description'] = task
        TaskID[str(task_id)]['status'] = 'todo'
        TaskID[str(task_id)]['createdAt'] = TaskID[str(task_id)]['updatedAt'] = datetime.now().isoformat()

        write_data_to_json(action, TaskID)
        task_id += 1
    else:
        write_data_to_json(action, task)

def main():
    # 確保 JSON 文件存在
    ensure_task_file_exists()

    while True:
        user_input = input()
         # 將輸入以空格為分隔符拆分
        if "update" in user_input:
            parts = user_input.split(' ', 2)
            action = parts[0]
            id = parts[1]
            task = parts[2]
        else:
            parts = user_input.split(' ', 1)
            action = parts[0]
            task = parts[1]

        
        if action == 'add':
            task_action(action, task)
        elif action == 'delete':
            task_action(action, task)
        elif action == 'update':
            update_task(action, id, task)
        elif action == 'mark-in-progress' or action == 'mark-todo' or action == 'mark-done':
            task_action(action, task)
        elif action == 'list':
            task_action(action, task)




if __name__ == "__main__":
    main()