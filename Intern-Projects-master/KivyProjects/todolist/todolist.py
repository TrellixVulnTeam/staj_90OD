import json
from datetime import date
def converter(path):
    try:
        file = open(path)
    except FileNotFoundError:
        print("File not found")
    except (ValueError,TypeError):
        print("JSON format error")
    file_read = file.read()
    #print(type(file_read))
    file_data = json.loads(file_read)
    #print(file_data)
    #print(type(file_data[0]))
    temp = []
    for x in  file_data:
        temp.append(x)

    file.close()
    return temp

data = converter("data.json")


def AddTask():
    task = input("Enter a task to Add")
    date = input("Set a task date (dd-mm-yyyy)")

    new = {
          "title" : task,
          "date" : date,
          "completed" : 0
          }
    data.append(new)

def RemoveTask():
    task = input("Enter a task name to remove")
    for current in data:
        if (task == current.get("title")):
            print(current.get("title"))
            data.remove(current)
    else:
        pass

def DoTask():
    task = input("Enter a task name to do it")
    for current in data:
        if (task == current.get("title")):
            current["completed"] = 1
            print(current.get("title") + "Done")
            tmp = current.get("title")













AddTask()
print(data)
RemoveTask()
print(data)
DoTask()
print(data)
AddTask()
print(data)
RemoveTask()



print(data)
