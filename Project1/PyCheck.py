# READ ME
# I wrote a program using a while loop, an if statement,
# and console input. It's really just a dummy program
# that trolls the user into choosing any number
# and requires constant reassurance.
# I also defined a function like in the slides.
# I didn't see a reason to use a for loop or a mutable
# object so I didn't use either, but I did experiment
# with them.
# P.S. I wrote if statements until right before the 79th
# character of the line, just like the Style Guide suggests!
# - Dave Bravo-Ruelas

superDuperSure = False
again = False
while not superDuperSure:
    if again:
        a = int(input("Enter a number...Again: "))
    else:
        a = int(input("Enter a number: "))
    answer = input("Are you sure? y/n: ")
    if answer == "y":
        answer = input("Are you really sure? y/n: ")
        if answer == "y":
            answer = input("Are you really, really sure? y/n: ")
            if answer == "y":
                answer = input("But are you really, REALLY sure? y/n: ")
                if answer == "y":
                    answer = input("Are you super duper sure? y/n: ")
                    if answer == "y":
                        print("Good Choice.", a, "plus one is", a + 1)
                        superDuperSure = True
    if superDuperSure:
        def myFunction():
            print("Congratulations on making it out of the loop!")
    else:
        def myFunction():
            print("You're so indecisive!")
    myFunction()
