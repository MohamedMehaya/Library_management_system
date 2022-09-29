import sqlite3
from datetime import date


def bookRecommend():
    """ recommend books to each reader according to the genre he reads
    """
    db = sqlite3.connect('Library.db')
    # cursor = db.cursor()
    # print("Connected to Database successfully")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    d1 = "'" + d1 + "'"
    # print(d1)

    cursor = db.execute("SELECT Member_ID from First_Table")
    r_list = []  # readers_list
    for row in cursor.fetchall():
        h = str(row)
        h = h.replace("(", "")
        h = h.replace(")", "")
        h = h.replace(",", "")
        h = h.replace("'", "")
        # print(h)
        if h != "0":
            # print(h)
            r_list.append(h)

    # print(r_list)

    g_list = []

    rstring = ""

    # for each reader
    for x in r_list:
        query = """SELECT Genre from First_Table Where Member_ID = ?"""
        cursor = db.cursor()
        cursor.execute(query, (x,))
        # for each line
        a = b = c = d = e = 0
        for row in cursor:
            h = str(row)
            h = h.replace("(", "")
            h = h.replace(")", "")
            h = h.replace(",", "")
            h = h.replace("'", "")
            if h == 'fiction':
                a += 1
            if h == 'Comedy':
                b += 1
            if h == 'Action':
                c += 1
            if h == 'Horror':
                d += 1
            if h == 'Detective and Mystery':
                e += 1
        h2 = str(a) + str(b) + str(c) + str(d) + str(e)
        g_list.append(h2)

    # for each reader
    for i in range(len(r_list)):
        k = r_list[i]  # reader name
        # print(" ")
        # print("reader is " + k)
        fs = g_list[i]  # reader's frequency string
        # print("l is " + fs)

        # finding the 2 highest read genres
        # for each letter in frequency string
        max1 = max2 = 0
        h3 = h4 = 0
        # lc = -1

        for j in range(len(fs)):
            # print("j is "+fs[j])
            num = int(fs[j])
            if num > h3:
                h3 = j

        for j in range(len(fs)):
            # print("x is "+x)
            num = int(fs[j])
            if h4 < num <= h3:
                h4 = j

        # print("h3 is", h3)
        # print("h4 is", h4)

        h5 = h6 = 'some genre'
        if h3 == 0:
            h5 = 'fiction'
        if h3 == 1:
            h5 = 'Comedy'
        if h3 == 2:
            h5 = 'Action'
        if h3 == 3:
            h5 = 'Horror'
        if h3 == 4:
            h5 = 'Detective and Mystery'

        if h4 == 0:
            h6 = 'fiction'
        if h4 == 1:
            h6 = 'Comedy'
        if h4 == 2:
            h6 = 'Action'
        if h4 == 3:
            h6 = 'Horror'
        if h4 == 4:
            h6 = 'Detective and Mystery'

        # print("h3 is ", h3)
        # print("h4 is ", h4)
        query = """SELECT Title from First_Table Where Genre = ?"""
        cursor = db.cursor()
        cursor.execute(query, (h5,))

        b_list = []

        rstring += "We recommend for " + k
        rstring += "\n"

        for row in cursor:
            h = str(row)
            h = h.replace("(", "")
            h = h.replace(")", "")
            h = h.replace(",", "")
            h = h.replace("'", "")
            b_list.append(h)
            rstring += h
            rstring += "\n"

        rstring += "\n"
    return rstring


bookRecommend()
