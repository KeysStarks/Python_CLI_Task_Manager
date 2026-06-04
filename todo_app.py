import json
TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the tasks.json file."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
def save_tasks():
    """Save tasks to the tasks.json file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
tasks = load_tasks()


def display_menu(): 
    print("\n===== TO-DO-LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5. View Completed Tasks")
    print("6. Quit")
    

def add_task():
    task = input("Enter a task:  ").strip()
    
    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append({"title": task, "completed": False})
        save_tasks()
        print(f"Task added: {task}")
        
def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks to view.")
    else:
        print("\nCurrent Tasks:")
        
        for index, task in enumerate(tasks, start=1):
            status = "✅ Complete" if task["completed"] else "⏳ Pending"
            print(f"{index}. {task['title']} - {status}")
            
def delete_task():
    try:
        if len(tasks) == 0:
            print("There are no tasks to delete.")
            return
        
        view_tasks()
        
        task_number = int(input("Enter the task number to delete: "))
        
        if task_number < 1 or task_number > len(tasks):
            raise IndexError
        
        confirm = input("Are you sure you want to delete this task? (yes/no): ").lower()
        
        if confirm != "yes":
            print("Delete canceled.")
            return
        
    except ValueError:
        print("Invalid input.  Please enter a number.")
        
    except IndexError:
        print("That task does not exist.")
        
    else:
        removed_task = tasks.pop(task_number - 1)
        save_tasks()
        print(f"Deleted task: {removed_task}")
        
    finally:
        print("Returning to menu...")
        
def mark_task_complete():
    try:

        if len(tasks) == 0:
            print("There are no tasks to mark complete.")
            return

        view_tasks()

        task_number = int(
            input("Enter task number to mark complete: ")
        )

        if task_number < 1 or task_number > len(tasks):
            raise IndexError
        

    except ValueError:
        print("Invalid input. Please enter a number.")

    except IndexError:
        print("That task does not exist.")

    else:
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task marked complete!")

    finally:
        print("Returning to menu...")
        
def view_completed_tasks():
    
    completed_found = False
    for index, task in enumerate(tasks, start=1):
        
        if task["completed"]:
            
            print(f"{index}. {task['title']}")
            
            completed_found = True
        
    if not completed_found:
        print("No completed tasks found.")
        
def main():
        
        print("Welcome to the Python To-Do List App!")
        
        while True:
            
            try:
                display_menu()
                
                choice = input("Choose and option (1-6): ").strip()
                
                if  choice == "1":
                    add_task()
                    
                elif choice == "2":
                    view_tasks()
                    
                elif choice == "3":
                    delete_task()
                    
                elif choice == "4":
                    mark_task_complete()
                    
                elif choice == "5":
                    view_completed_tasks()
                    
                elif choice == "6":
                    print("Goodbye!")
                    break
                
                else:
                    raise ValueError
            
            except ValueError:
                print("Invalid menu option.  Please choose 1, 2, 3, 4, 5, or 6.")
                
            finally:
                print("Action complete. ")
                
main()

                