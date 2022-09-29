import sqlite3


def initiate_db():
    db = sqlite3.connect('Library.db')
    # print("Opened Database successfully")

    # ID, Genre, Title, Author, Loan_Period, Purchase_Date, Member_Id

    with db:
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS First_Table(ID INT,Genre TEXT,Title TEXT,Author TEXT,"
                    "Loan_Period INT,Purchase_Date TEXT,Member_Id TEXT)")
        f1 = open("file1.txt", "r")
        for line in f1:
            ID, Genre, Title, Author, Loan_Period, Purchase_Date, Member_Id = line.strip().split(",")
            cur.execute("INSERT INTO First_Table VALUES(" + ID + "," + Genre + "," + Title + "," + Author
                        + "," + Loan_Period + "," + Purchase_Date + "," + Member_Id + ")")

        # Transaction_ID, Book_ID, Checkout_Date, Return_Date

        cur.execute("CREATE TABLE IF NOT EXISTS Second_Table(Transaction_ID INT,Book_ID INT,Checkout_Date TEXT,"
                    "Return_Date TEXT)")
        f2 = open("file2.txt", "r")
        for line in f2:
            Transaction_ID, Book_ID, Checkout_Date, Return_Date = line.strip().split(",")
            cur.execute("INSERT INTO Second_Table VALUES(" + Transaction_ID + "," + Book_ID + "," + Checkout_Date
                        + "," + Return_Date + ")")

    print("Database Library has been created successfully")

    db.commit()

    # Close Database
    db.close()


initiate_db()
