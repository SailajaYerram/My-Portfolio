from connect import *
from read import *

def readFilmflix():
    cursor.execute("SELECT * FROM tblfilms1")
    row = cursor.fetchall()
    for record in row:
        print(record)

if __name__ == "__main__":
  readFilmflix()        
