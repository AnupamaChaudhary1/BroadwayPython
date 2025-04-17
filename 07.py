# tasks=[]
# while True:  #run the loop until it is exited use while true
#     print('##Welcome to the Task Manager!')
#     print('1. Add task')
#     print('2. Remove task')
#     print('3. View task')
#     print('4. Clear Tasks')
#     print('5. Exit')
#     choice=input('Enter your choice:')
    
#     if choice=='1':
#         task=input('Enter the task:')
#         if task:
#             tasks.append(task.strip())
#             print('Task added')
#         else:
#             print('Task cannot be empty')
#     elif choice=='5':
#         print('Thanks....')
#         break #exit the program
    

#     elif choice == '2':
#         taskIndex = input('Enter the task index to remove: ')
#         if taskIndex.isdigit():
#             taskIndex = int(taskIndex)
#             if 1 <= taskIndex <= len(tasks):  # Check if the index is valid
#                 removed_task = tasks.pop(taskIndex - 1)  # Remove the task at the index
#                 print(f'Task "{removed_task}" removed successfully!')
#             else:
#                 print("Invalid index! Please enter a valid task number.")
#         else:
#                 print("Please enter a valid index number.")
#         # taskIndex =int(input('Enter the task to remove: '))
#         # # if taskIndex.isdigit():
#         # if taskIndex>len(tasks) or taskIndex<=0:
#         #       print("Invalid task number")
#         #     # tasks.remove(task.strip())
#         #     # print('Task removed successfully!')
#         # else:
#         #       tasks.pop(taskIndex - 1)
#         #       print('Task removed')

    
        
#     elif choice == '3':
#         if tasks:
#          for i, tasks in enumerate(tasks,start=1):
#           print(f"{i}.{tasks}")
#         #print('Tasks:', tasks if tasks else "No tasks available.")
    
#     #elif choice=='4': #to remove the tasks
        
#     elif choice=='4':
#         tasks.clear()
#         print('task cleared')
#     else:
#         print('Invalid choice! Please enter a number between 1 and 5.')

#     input("\n Press any key to continue!")  

    



tasks = []
while True:
    print('## Welcome to the Task Manager! ##')
    print('1. Add task')
    print('2. Remove task')
    print('3. View tasks')
    print('4. Clear tasks')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        task = input('Enter the task: ')
        if task:
            tasks.append(task.strip())  # Add task to the list
            print('Task added!')
        else:
            print('Task cannot be empty!')

    elif choice == '2':
        if not tasks:
            print("No tasks available to remove.")
        else:
            taskIndex = input('Enter the task index to remove: ')
            if taskIndex.isdigit():  # Check if input is a valid number
                taskIndex = int(taskIndex)  # Convert the input to an integer
                if 1 <= taskIndex <= len(tasks):  # Check if the index is valid
                    removed_task = tasks.pop(taskIndex - 1)  # Remove the task at the index
                    print(f'Task "{removed_task}" removed successfully!')
                else:
                    print("Invalid index! Please enter a valid task number.")
            else:
                print("Invalid input! Please enter a valid index number.")

    elif choice == '3':
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")

    elif choice == '4':
        tasks.clear()  # Clear all tasks
        print('All tasks cleared.')

    elif choice == '5':
        print('Thanks for using the Task Manager!')
        break  # Exit the program

    else:
        print('Invalid choice! Please select a valid option.')

    input("\nPress any key to continue!")  # Wait before continuing
