from connect import *
from read import *
import time

def deleteFilmflix():

    idField = input("Enter the filmID of the record to be deleted: ")
    cursor.execute(f"DELETE FROM tblfilms1 WHERE filmID = {idField} ")
    conn.commit()

    print(f"Record {idField} deleted in the tblfilms1 table")
    time.sleep(3)

    readFilmflix() # calling subroutine

if __name__ == "__main__":
    deleteFilmflix()    


