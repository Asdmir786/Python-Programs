listOfTasks = []
user_input = input("Add A Task.\n: ")
listOfTasks.append("1.",user_input)
print("WHat do you want to do?")
print('''
        1.Add More = add
        2. Delete A Task = del
        3. Save Tasks = save
        3. Save Tasks and Exit The Program = stetp 
      ''')
checkForMore = input() 
if checkForMore == "add":
    user_input = input("Add A Task.\n: ")
    listOfTasks.append("1.",user_input)
elif checkForMore == "del":
    pass
elif checkForMore == "save":
    pass
elif checkForMore == "stetp":
    pass
