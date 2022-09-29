import sqlite3
from datetime import date


def bookCheckout(x, y):
    """ update the database with the book withdrawn
    x is the borrower’s member-ID
    y is the bookID
    """
    db = sqlite3.connect('Library.db')
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    # print("Opened database successfully")

    cursor = db.execute("SELECT Book_ID from Second_Table")
    flag = False
    for row in cursor:
        z = str(row)
        z = z.replace("(", "")
        z = z.replace(")", "")
        z = z.replace(",", "")
        if z == y:
            flag = True

    if flag:
        return "Sorry, the book is already taken"

    cursor = db.execute("SELECT Member_ID, Loan_Period, ID from First_Table")
    my_list = cursor.fetchall()
    loaned = False  # flag to check whether the borrower has lent before
    length = len(my_list)
    a, b, c = 3, 3, 3  # initiating variables
    for i in range(length):
        z = str(my_list[i])
        z = z.replace("(", "")
        z = z.replace(")", "")
        # a is Member_ID, b is Loan_Period, c is ID
        a, b, c = z.split(",")

        a = a.replace("'", "")
        if a == x:
            loaned = True
    if not loaned:
        # insert into first table
        query = """UPDATE First_Table set Member_ID = ?  where ID = ?"""
        tuple1 = (x, y)
        cursor.execute(query, tuple1)
        # insert into second table
        sqlite_insert = """INSERT INTO Second_Table 
                (Transaction_ID,Book_ID,Checkout_Date,Return_Date) VALUES 
                (?,?,?,?)"""
        tuple1 = (101, y, d1, '___')
        cursor.execute(sqlite_insert, tuple1)
        return "Book has been withdrawn"

    # Now we will check whether the borrower has borrowed a book for more than the available period
    query = """SELECT Checkout_Date,Return_Date from Second_Table Where Book_ID=?"""
    input3 = c
    cursor.execute(query, input3)
    row = cursor.fetchone()
    z = str(row)
    z = z.replace("(", "")
    z = z.replace(")", "")
    d1, d2 = z.split(",")
    d1 = d1.replace("'", "")
    d2 = d2.replace("'", "")
    a1, a2, a3 = d1.split("/")
    d2 = str(d2)
    if d2[2] == '_':
        d2 = 25 / 10 / 2021
    b1, b2, b3 = d2.split("/")
    nod = dso(a1, a2, b1, b2)
    if nod > b:
        return "sorry, the student has a book that should be returned"
    else:
        # insert into first table
        query = """UPDATE First_Table set Member_ID = ?  where ID = ?"""
        tuple1 = (x, y)
        cursor.execute(query, tuple1)
        # insert into second table
        sqlite_insert = """INSERT INTO Second_Table 
                        (Transaction_ID,Book_ID,Checkout_Date,Return_Date) VALUES 
                        (?,?,?,?)"""
        tuple1 = (101, y, d1, '___')
        cursor.execute(sqlite_insert, tuple1)

        db.commit()

        # Close Database
        db.close()

        return "Book has been withdrawn"


def dso(c, d, f, g):
    """
        return number of days between two dates
        c: first day
        d: first month
        f: second day
        g: second month
    """
    z = rtd(d) - int(c)
    z += int(f)
    for i in range(int(d), int(g)):
        z += rtd(i)
    return z


def rtd(x):
    """
    return number of days in a month
    """

    if x == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        return 31
    if x == (4 or 6 or 9 or 11):
        return 30
    return 28


# r = bookCheckout(1, "bmni")
# print(r)

#     x is the borrower’s member-ID
#     y is the bookID
