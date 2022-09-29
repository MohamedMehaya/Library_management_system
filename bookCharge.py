import sqlite3
from datetime import date


def bookCharge():
    """ return cost of lending the book for days over the available period i.e 7/28 days
    """

    db = sqlite3.connect('Library.db')
    # print("Opened database successfully")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    d1 = "'" + d1 + "'"

    cursor = db.execute("SELECT Checkout_Date, Return_Date from Second_Table")
    total = 0

    for row in cursor:
        row = str(row)
        row = row.replace("(", "")
        row = row.replace(")", "")
        # print(row)

        a, b = row.split(",")
        a = a.replace("'", "")
        c, d, e = a.split("/")

        # print("b is " + b)
        if b[2] is "_":
            b = d1
        # print("b is " + b)
        b = b.replace("'", "")
        f, g, h = b.split("/")
        po = 0.25 * (dso(c, d, f, g) - 28)
        total += po

    db.commit()

    # Close Database
    db.close()

    return "The total amount that has to be paid to the Library is £" + str(total) + "    "
    # msg_label['text'] = "The total amount that has to be paid to the Library is £" + str(total)


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

# bookCharge()
