"""Homework2 Module -- Demonstrates a credit card validator.

This module validates credit card numbers. It reads a series
of numbers from user input. It checks for a credit card
type, and whether the numbers are a valid sequence for credit cards.

    Run the program from the command line:
        $ python Homework2.py

Attribute(s):
    None.
"""


def main():
    """main function, runs the required Menu window from which a user
    chooses which action is desired to take.

    This function provides the user with the choice of validating a number,
    or exiting the program. This runs in a loop to ensure a user
    validates more than one series of numbers if so desired.
    This function calls on the numbers() function, and prints the returned
    string.

    Arguments:
        None.
    Returns:
        None.
    """
    end = False
    while not end:
        print("")
        print("===Credit Card Validation===")
        print("1. Validate Number")
        print("2. Exit Program")
        print("============================")
        a = int(input("Menu Choice: "))
        if a == 2:
            end = True
        else:
            s = numbers()
            print(s)


def numbers():
    """numbers function, asks the user for a series of numbers and
    places them in a list to validate with the validate() function.

    This function asks for a series of numbers to be validated.
    The numbers are split into a list of integers, and checks to
    make sure the input is between 13 and 16 integers, which is
    required for credit cards. If not, it recursively calls the
    numbers() function again until an appropriate series is submitted.
    Otherwise, it calls the validate(b) function, using the
    list of integers as the passed parameter.

    Arguments:
        None.
    Returns:
        str: Returns the submitted number, the card type, and validation.

        This function returns a string composed of the submitted number,
        the card type, and a string containing "Valid" or "Invalid"
        depending on validation.
    """

    valid = False
    while not valid:
        a = input("\nEnter a series of numbers (1 2 3...): ")
        b = [int(x) for x in a.split()]
        if len(b) < 13 or len(b) > 16:
            print("Must be between 13 and 16 Numbers. Try again.")
            valid = False
        else:
            valid = True
            return a + "\n" + validate(b)


def validate(b):
    """Validate function, takes a list of integers and checks for
    valid credit card number sequences.

    This function takes a list of integers, b, and checks for
    valid numbers using a provided algorithm.

    Arguments:
        b (list): A list of integers.
            This parameter is a list of the integers submitted in numbers().
    Returns:
        str: Returns credit card type, and valid or invalid.

        This function returns a string containing the credit card type,
        and the checked validation.
    """
    cc = cckind(b[0], b[1])
    c = [(x * 2) - 9 for x in b[-2::-2] if x * 2 > 9]
    d = [x * 2 for x in b[-2::-2] if x * 2 <= 9]
    e = c + d
    sum1 = sum(e)
    sum2 = sum([x for x in b[-1::-2]])
    if (sum1 + sum2) % 10 == 0:
        return cc + "\nValid"
    else:
        return cc + "\nInvalid"


def cckind(a, b):
    """cckind function: Takes in two numbers, checks for credit card
    type.

    This function takes in two numbers from the list of submitted
    numbers, and checks if they match to any of the credit card
    types.

    Arguments:
        a (Int): The first number in the list of integers.
        b (Int): The second number in the list of integers.
    Returns:
        str: Returns a string of the credit card type.
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


if __name__ == '__main__':
    main()
