import sqlite3
from datetime import date


def bookReturn(x):
    """ return Book(s) lent by student and updating records accordingly
    """
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    # print("Opened Database successfully")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    d1 = "'" + d1 + "'"

    query = """SELECT Member_ID from First_Table Where ID = ?"""
    # input1 = (x)
    cursor.execute(query, (x,))
    rid = str(cursor.fetchone())

    rid = rid.replace("(", "")
    rid = rid.replace(")", "")
    rid = rid.replace("'", "")
    rid = rid.replace(",", "")
    # print(rid)
    if rid == '0':
        db.commit()

        # Close Database
        db.close()

        return "This book is not taken"
    else:
        query = """Update First_Table set Member_ID = ? Where ID = ?"""
        input2 = ('0', x)
        cursor.execute(query, input2)

        query = """Update Second_Table set Return_Date = ? Where Book_ID = ?"""
        input3 = (d1, x)
        cursor.execute(query, input3)

        db.commit()

        # Close Database
        db.close()

        return "Thank you, The book has been returned"


# bookReturn(10)
