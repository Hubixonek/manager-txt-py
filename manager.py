import os
from pick import pick

def fileSelector():
    files = []
    for file in os.listdir('.'):
        if file.endswith('.txt'):
            files.append(file)
    # If the files exist, display the selection
    if files:
        title = 'Please select a file to open'
        option, index = pick(files, title)
        print(option, index)
    else:
        print('Files not exists')
def createNotes():
    text = input('Do u want to create a new file? (Y/N)\n')
    if text.lower() == "y":
        inputText = input('Name your .txt file...\n') + ".txt"
        if os.path.isfile(inputText):
            print('Is already Exist')
        else:
            createdFile = open(inputText, 'a')
            someText = input("Put text in your text file...\n")
            createdFile.write(someText)
            createdFile.close()
    elif text.lower() == "n":
        useExistingFile = input("Do u want to use existing file? (Y/N) \n")
        if useExistingFile.lower() == "y":
            fileSelector()
        elif useExistingFile.lower() == "n":
            print('Goodbye!')
        else:
            print("Wrong answer, try again!")
    else:
        print("Wrong answer, try again!")
        return createNotes()

createNotes()



