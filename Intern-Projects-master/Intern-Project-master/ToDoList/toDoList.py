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

    file_data = json.loads(file_read)

    temp = []
    for x in  file_data:
        temp.append(x)

    file.close()
    return temp

data = converter("data.json")


def AddTask():
    a=0
    num2=input("How many events will appended ?")
    while a<int(num2):

        task = input("Enter a task to Add")
        date = input("Set a task date (dd-mm-yyyy)")

        new = {
              "title" : task,
              "date" : date,

              "completed" : 0
              }
        data.append(new)
        a=a+1


def RemoveTask():
    a=0
    num1=input("How many events will removed ? ")
    while a < int(num1):
        task = input("Enter a task name to remove")
        for current in data:
            if (task == current.get("title")):
                print(current.get("title"))
                data.remove(current)
        else:
            pass
        a=a+1

def DoTask():
    a=0
    num3=input("How many events were completed ? ")
    while a<int(num3):
        task = input("Enter a task name to do it")
        for current in data:
            if (task == current.get("title")):
                current["completed"] = 1
                print(current.get("title") + "Done")
                tmp = current.get("title")
        a=a+1


def remandapp():
    number2 = input("Append events please press 1,delete events please press 2")
    if int(number2) == 1:
        AddTask()

    else:
        RemoveTask()
que=input("Do you want to append or remove events ? If you want,press 1 . If you dont,press 2...")
if int(que)==1:
    remandapp()
else:
    print("No remove and addition.")

comp=input("Did you complete any events? If you completed any events,press 1.If you didn't,press 2.")
if int(comp)==1:
    DoTask()
else:
    print("No completed. ")













print(data)
