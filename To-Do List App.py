listOfTasks = []
user_input = input("Add A Task.\n: ")
listOfTasks.append(".",user_input)
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
    listOfTasks.append(".",user_input)
elif checkForMore == "del":
    print(listOfTasks)
    enterNumber = int(input("Tell me which one to delete. "))
    listOfTasks.pop(enterNumber-1)
elif checkForMore == "save":
    with open("ToDOList.txt","w") as fyou:
        fyou.writelines(listOfTasks)
        fyou.close()
elif checkForMore == "stetp":
    with open("ToDOList.txt","w") as fyou:
        fyou.writelines(listOfTasks)
        fyou.close()
    print(listOfTasks)    
    exit()
