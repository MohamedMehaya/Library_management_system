from random import randint


def First_Table_Generator():
    for i in range(1, 11):
        a = randint(97, 123)
        b = randint(97, 123)
        c = randint(97, 123)
        d = randint(97, 123)

        e = randint(0, 1)
        if e:
            mid = str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d))
        else:
            mid = '0'

        print(i, ", 'fiction', 'Harry Potter and the Sorcerer’s Stone', 'J.K Rowling', '28', '20-5-2008'," +
              mid)

    for i in range(11, 21):
        a = randint(97, 123)
        b = randint(97, 123)
        c = randint(97, 123)
        d = randint(97, 123)

        e = randint(0, 1)
        if e:
            mid = str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d))
        else:
            mid = '0'

        print(i, 'fiction', 'Asterix and Obelix', 'Gosciny', '28', '20-7-2009' +
        mid)

    for i in range(21, 31):
        a = randint(97, 123)
        b = randint(97, 123)
        c = randint(97, 123)
        d = randint(97, 123)

        e = randint(0, 1)
        if e:
            mid = str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d))
        else:
            mid = '0'

        print(i , 'Comedy', 'A Confederacy of Dunces', 'John Kennedy Toole','7' , '20-5-20005' +
        mid)

    for i in range(31, 41):
        a = randint(97, 123)
        b = randint(97, 123)
        c = randint(97, 123)
        d = randint(97, 123)

        e = randint(0, 1)
        if e:
            mid = str(chr(a)) + str(chr(b)) + str(chr(c)) + str(chr(d))
        else:
            mid = '0'

        print(i , 'Comedy', 'Me Talk Pretty One Day', 'David Sedaris', '7' , '20-5-2021' +
        mid)


First_Table_Generator()


def Second_Table_Generator():
    for i in range(1, 101):
        year = str(randint(2020, 2021))
        m1 = randint(1, 10)  # month of loaning the book
        rd = randint(0, 1)
        if rd:
            sd = "'" + str(randint(1, 31)) + '/' + str(randint(m1, 10)) + '/' + year + "'"
        else:
            sd = "'___'"
        print(str(i) + ',' + str(randint(11, 100)) + ',' + "'" + str(randint(1, 31)) + '/' + str(m1) + '/'
              + year + "'," + sd)
