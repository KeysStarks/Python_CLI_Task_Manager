tasks = []


def display_menu(): 
    print("\n===== TO-DO-LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5: Quit")
    

def add_task():
    task = input("Enter a task:  ").strip()
    
    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append({"title": task, "completed": False})
        print(f"Task added: {task}")
        
def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks to view.")
    else:
        print("\nCurrent Tasks:")
        
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task["completed"] else "Pending"
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
        
    except ValueError:
        print("Invalid input.  Please enter a number.")
        
    except IndexError:
        print("That task does not exist.")
        
    else:
        removed_task = tasks.pop(task_number - 1)
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
        print("Task marked complete!")

    finally:
        print("Returning to menu...")
        
def main():
        
        print("Welcome to the Python To-Do List App!")
        
        while True:
            
            try:
                display_menu()
                
                choice = input("Choose and option (1-5): ").strip()
                
                if  choice == "1":
                    add_task()
                    
                elif choice == "2":
                    view_tasks()
                    
                elif choice == "3":
                    delete_task()
                    
                elif choice == "4":
                    mark_task_complete()
                    
                elif choice == "5":
                    print("Goodbye!")
                    break
                
                else:
                    raise ValueError
            
            except ValueError:
                print("Invalid menu option.  Please choose 1, 2, 3, or 4.")
                
            finally:
                print("Action complete. ")
                
main()
                