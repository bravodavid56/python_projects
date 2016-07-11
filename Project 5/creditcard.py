from tkinter import *


class CreditCard:
    """The CreditCard class is a class representative of
    a Credit Card.

    Attributes:
        None.
    """
    def __init__(self, numbers=[], type="", valid=False):
        """Constructor for the Credit Card class.

        Takes in several parameters pertaining to Credit Cards,
        including the number, the type, and validation.

        Arguments:
            numbers (list): a list of the numbers on the card
            type (str): a string holding the type of card
            valid (bool): a boolean indicating a valid/invalid card
        """
        self.numbers = numbers
        self.type = type
        self.valid = valid

    def fetch(self, entry):
        """fetch method; fetches the numbers input into message field.

        Takes in an entry parameter of type Entry, and checks to
        make sure the input is within 13 and 16 numbers. Also
        calls the validate function to validate the numbers, then
        calls the display function to display the numbers,
        type, and validity. Creates a window indicating the
        required input amount.

        Arguments:
            entry (Entry): the entry from the form, which holds the
                numbers input.
        Returns:
            None.
        """
        if 12 < len(entry.get()) < 17:
            total = self.validate(entry)
            self.display(entry.get(),total[0], total[1])
        else:
            row=Toplevel()
            t = "Must be between 13 and 16 numbers."
            l=Label(row, width=40, text=t, padx=10, pady=15)
            l.config(font="System 24 bold")
            l.pack(side=TOP)

    def display(self, numbers, type, valid):
        """display function, displays the numbers, type, and validity
        of the credit card number input by the user.

        Creates a window showing the credit card number, the type of
        credit card, and the validity. Displays a teal valid message if
        valid, and red if invalid.

        Arguments:
            numbers (Int): the numbers input on form
            type (str): the string representation of the type of card
            valid (bool): a boolean representing validity of card
        Returns:
            None.
        """
        row=Toplevel()
        l=Label(row, width=40, text=numbers, padx=10, pady=15)
        l.config(font="System 16 bold")
        l.config(fg="white", bg="#309C99")
        l2=Label(row, width=20, text=type, padx=10, pady=5)
        l2.config(fg="white", bg="#309C99")
        l3=Label(row, width=10, text=valid, padx=10, pady=5)
        if valid == "Invalid":
            l3.config(bg="white", fg="#BF0631")
        else:
            l3.config(fg="#309C99", bg="white")
        l.pack(side=TOP, fill=X)
        l2.pack(side=TOP, fill=X)
        l3.pack(side=TOP, fill=X)

    def make_form(self, root, field):
        """make_form function, creates the form for inputting the numbers.

        Creates a form, using a frame to hold the label, and Entry widgets.

        Arguments:
            root (Frame): used to create the frame in the same window
            field (str): the fields required for the form, in this case
                only the numbers are required so field is 'Numbers'
        Returns:
            Entry: entry object, which holds the numbers input into
                the required field
        """
        row = Frame(root)
        lab = Label(row, width=20, text=field)
        ent = Entry(row)
        lab.config(pady=40)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)

        return ent

    def validate(self, entry):
        """validate function, validates the number in entry parameter.

        This function gets the number input from the entry parameter, and
        creates a list of Int holding the individual numbers at each index.
        Since the numbers retrieved from entry are strings, this function
        attempts to cast the string representations of the numbers into Int,
        and catches a ValueError exception when a non-number input is
        detected when casting. This exception clause creates a window
        indicating the program does not accept spaces, punctuation, or
        symbols, where symbols include the alphabet. Furthermore,
        this function calls the cckind function to check the type, and
        check_valid to check if valid or invalid.

        Arguments:
            entry (Entry): an entry holding the string representation
                of the input numbers.
        Returns:
            list: a list containing the parameters of the Credit Card
                object; the numbers, the type, and the validity.
        """
        try:
            total = []
            int(entry.get())
            stringnum = list(entry.get())
            numbers = []

            for num in stringnum:
                numbers.append(int(num))

            type = self.cckind(numbers[0], numbers[1])
            total.append(type)

            valid = self.check_valid(numbers)
            total.append(valid)

            return total
        except ValueError:
            row=Toplevel()
            t = "No spaces, punctuation, or symbols"
            l=Label(row, width=40, text=t, padx=10, pady=15)
            l.config(font="System 24 bold")
            l.pack(side=TOP)

    def cckind(self, a, b):
        """cckind function, checks which kind of card pertains to the
        numbers a and b.

        This function uses a and b to determine which kind of credit
        card number is input, and returns which type these numbers
        pertain to.

        Arguments:
            a (Int): the first number in the credit card
            b (Int): the second number in the credit card
        Returns:
            str: a string representation of the type of
                credit card detected by the program
        """
        if a == 4:
            return "Visa Card"
        elif a == 5:
            return "Master Card"
        elif a == 6:
            return "Discover Card"
        elif a == 3 and b == 7:

            return "American Express"
        else:
            return "Not a Valid Card Type"

    def check_valid(self, b):
        """check_valid function, uses a formula for detecting
        validity.

        This function uses a mathematical formula for detecting
        credit card validity. It also employs list comprehension
        to iterate through the list of numbers b and odd and even
        indexes.

        Arguments:
            b (list): a list of Int representing the numbers
        Returns:
            str: returns valid if a valid number, invalid
                if invalid number.



        """
        c = [(x * 2) - 9 for x in b[-2::-2] if x * 2 > 9]
        d = [x * 2 for x in b[-2::-2] if x * 2 <= 9]
        e = c + d
        sum1 = sum(e)
        sum2 = sum([x for x in b[-1::-2]])
        if (sum1 + sum2) % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

