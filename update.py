from connect import *
from read import *
import time

def updateFilmflix():
     
    idField = input("Enter the filmID of the record to be updated: ")
    fieldName = input("Which field would you like to update (Title/YearReleased/Rating/Duration/Genre)?: ")

    newFieldValue = input(f"Enter the new value for: {fieldName}: ")
    newFieldValue = "'" + newFieldValue + "'"

    cursor.execute(f"UPDATE tblfilms1 SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")
    conn.commit()

    print(f"Record {idField} updated in the tblfilms1 table")
    time.sleep(3)

    readFilmflix() # call readSongs subroutine
if __name__ == "__main__":
    updateFilmflix() 
