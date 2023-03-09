import create
import read
import update
import delete


# create a function
def menuOptions():
    options = 0  # flag variable
    # while 0 not in this list ["1","2","3","4","5"]:
    while options not in ["1", "2", "3", "4", "5"]:
        print(
            " Tblfilms1 Menu Options\nEnter:\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Exit"
        )
        # re-assign the value for options variable
        # the default datatype for input is string
        options = input("Enter an option from the menu above: ")
        print(type(options))
        print(options)
        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice")
    return options

# menuOptions()
mainProgram = True  # assign the mainProgram a value with a boolean datatype of True
while mainProgram:  # same as while True
    mainMenu = menuOptions()
    if mainMenu == "1":
        read.readFilmflix()
    elif mainMenu == "2":
        create.insertFilmflix()
    elif mainMenu == "3":
        update.updateFilmflix()
    elif mainMenu == "4":
        delete.deleteFilmflix()
    else:  # re-assign the mainProgram a value with a boolean datatype of False
        mainProgram = False
input("Press enter to quit/exit the application")
