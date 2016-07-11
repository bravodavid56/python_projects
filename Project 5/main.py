from tkinter import *
from creditcard import CreditCard

"""main module -- Implements a credit card GUI.

This module creates a GUI representing a credit card
validator. It creates a window representing a form
with a 'validate' button, and a 'quit' button. The user
can choose to validate a number, or quit the program.

Attribute(s):
    None.
"""


def main():
    """main function, creates the beginning window for the GUI.

    This function creates the primary window allowing for number
    input. It also calls the function cc() to create the widgets
    including the button for 'Validate' and the button for
    'Quit.'

    Arguments:
        None.

    Returns:
        None.
    """
    root = Tk()
    win = Frame(root)
    win.pack(fill=X, expand = True)
    root.config(width=500, height=300)
    root.title("Welcome to Credit Card Validator 2.0")
    root.pack_propagate(0)

    label_font = ('system', 20, 'bold', 'italic')
    l = Label(root, text='Validator 2.0')
    l.config(font=label_font)
    l.config(bg='#61AB3C', fg='white')
    l.pack(expand=YES,fill=BOTH)

    cc(win)

    b = Button(win, text="Quit", command = win.quit)
    b.config(bg="#8C0104",fg="white")
    b.pack(side=RIGHT)
    b.config(width=30)

    win.mainloop()


def cc(root):
    """cc function -- creates an instance of CreditCard, and binds a button
    to the function fetch() on CreditCard object.

    This function creates a CreditCard object representing a Credit Card,
    and creates an Entry through the make_form function. Then it associates
    a button's command with the deferred callback function fetch() on Credit
    Card. Then it just configures some settings on the button.

    Arguments:
        root (Frame): expects a Frame object to put the button (widgets) on
    Returns:
        None.
    """
    fields = 'Numbers (no spaces):'
    c = CreditCard()
    ent = c.make_form(root, fields)
    # in case of exception, the try-catch clause does not work.
    # Because the program does not terminate, it becomes difficult
    # to address the "object not subscriptable" message
    # I suspect addressing this issue requires implementing
    # a non-lambda syntax, which seems unnecessary since
    # the program does not terminate at finding the exception
    b = Button(root, text='Validate', command = (lambda: c.fetch(ent)))
    b.config(fg="white", bg="#61AB3C")
    b.pack(side=LEFT)
    b.config(width=30)

if __name__ == '__main__':
    main()
