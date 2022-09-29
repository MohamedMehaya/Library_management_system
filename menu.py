from tkinter import *
import bookCharge
import bookCheckout
import bookRecommend
import bookReturn


def helper_1():
    """Handle clicks on the button"""
    msg3_label['text'] = bookCharge.bookCharge()


def helper_2():
    """Handle clicks on the button"""
    some_label = Label(window, text=bookCheckout.bookCheckout(bCheck_mid_entry.get(), bCheck_bid_entry.get()))
    some_label.grid(row=7, column=0)


def helper_3():
    """Handle clicks on the button"""
    some_label = Label(window, text=bookReturn.bookReturn(bRetur_bid_entry.get()))
    some_label.grid(row=10, column=0)


def helper_4():
    """Handle clicks on the button"""
    some_label = Label(window, text=bookRecommend.bookRecommend())
    some_label.grid(row=12, column=0)


window = Tk("")

msg1_label = Label(window, text=" Hello! This is the Library Management System")
msg1_label.grid(row=0, column=0)

msg2_label = Label(window, text=" Click This button to know money due to the library")
msg2_label.grid(row=1, column=0)

button1 = Button(window, text="bookCharge", command=helper_1)
button1.grid(row=2, column=0)

msg3_label = Label(window, text="")
msg3_label.grid(row=3, column=0)

msg4_label = Label(window, text=" Please enter the Member ID and the Book ID to withdraw a book")
msg4_label.grid(row=4, column=0)

bCheck_mid_entry = Entry(window)  # the "Entry" widget is for getting a user input.
bCheck_mid_entry.grid(row=5, column=0)

bCheck_bid_entry = Entry(window)  # the "Entry" widget is for getting a user input.
bCheck_bid_entry.grid(row=5, column=1)

button2 = Button(window, text="bookCheckout", command=helper_2)
button2.grid(row=6, column=0)

msg5_label = Label(window, text=" Please enter the Book ID to return a book")
msg5_label.grid(row=7, column=0)

bRetur_bid_entry = Entry(window)  # the "Entry" widget is for getting a user input.
bRetur_bid_entry.grid(row=8, column=0)

button3 = Button(window, text="bookReturn", command=helper_2)
button3.grid(row=9, column=0)

msg6_label = Label(window, text=" Please press to know the recommended books for each user")
msg6_label.grid(row=10, column=0)

button4 = Button(window, text="bookRecommend", command=helper_4)
button4.grid(row=11, column=0)

window.mainloop()
