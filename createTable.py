from connect import *

# Table name tblfilms 
# filmID(integer), title(text), yearReleased(integer),rating(text),
# duration(integer),genre(text) 


cursor.execute(
    """
    CREATE TABLE "tblfilms1" (
        "FilmID" INTEGER NOT NULL UNIQUE,
        "Title" TEXT,
        "YearReleased" INTEGER,
        "Rating" TEXT,
        "Duration" INTEGER,
        "Genre" TEXT,
        PRIMARY KEY("FilmID" AUTOINCREMENT)
)
    """
)
