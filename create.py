from connect import *
from read import *
import time 

# subroutine
def insertFilmflix():
    # create empty list
    tblfilms1 = []
    # ask for user input for the fields 

    Title = input("Enter film Title: ")
    YearReleased = int(input("Enter released year: "))
    Rating = input("Enter rating for film: ")
    Duration = int(input("Enter the duration of a film: "))
    Genre = input("Enter the film genre: ")

    # append data to do list called film

    tblfilms1.append(Title)
    tblfilms1.append(YearReleased)
    tblfilms1.append(Rating)
    tblfilms1.append(Duration)
    tblfilms1.append(Genre)

    cursor.execute("INSERT INTO tblfilms1 VALUES (NULL, ?, ?, ?, ?, ?)", tblfilms1)
    # commit to the tblfilms1 table in the database 
    conn.commit()
    print(f"Title {Title} added to the tblfilms1 table")
    time.sleep(3)

    readFilmflix()
    # cursor.execute("SELECT * FROM tblfilms1")

    # row = cursor.fetchall()
    # for record in row:
    #   print(record)
if __name__ == "__main__":

    insertFilmflix()     
       

       



