import sys#to use later to terminate the programm
number_of_tries = 0#a variable to keep the while loop running
number_of_guesses = 1

easy_answers = ["world", "python", "print", "html"]#answers variables
easy_text = "The current paragraph reads as such:A common first thing to do in a language is display 'Hello __1__!' In __2__ this is particularly easy; all yo uhave to do is type in: __3__ 'Hello __1__!' Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the __3__ command, and produces a program which does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an __4__ file in a browser, but it's a step in learning __2__ syntax, and that's really its purpose."#text varibale
medium_answers = ["function", "arguments", "None", "list"]#answers variables
medium_text = "A __1__ is created with the def keyword.  You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses. __1__s by default returns __3__ if you don't specify the value to retrun. __2__ can be standard data types such as string, integer, dictionary, tuple, and __4__ or can be more complicated such as objects and lambda functions."
hard_answers = ["light", "gleaming", "free", "brave"]#answers variables
hard_text = "Oh, say can you see, By the dawn's early __1__, What so proudly we hailed, At the twilight's last __2__? Whose broad stripes and bright stars, Through the perilous fight, O'er the ramparts we watched, Were so gallantly streaming. And the rocket's red glare, The bombs bursting in air, Gave proof through the night, That our flag was still there. Oh say does that star spangled banner yet wave, For the land of the __3__, and the home of the __4__."
subs = [" What should be substituted in for __1__?          ",\
        " What should be substituted in for __2__?          ",\
        " What should be substituted in for __3__?          ",\
        " What should be substituted in for __4__?          "]

def string_in_blanks(word, blanks):#takes in 2 lists and returns 1 list with certain elements replaced
    for pos in blanks:
        if pos in word:
            return pos
        return None

def replace_blanks(text, blanks, user_input):#takes in 3 arguments:text, blanks and user_input. Checks the text for blanks and replaces them with the user_unput. returns updated text
    text = text.split()
    replaced = []

    for word in text:
        replacement = string_in_blanks(word, blanks)
        if replacement != None:
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    text = replaced
    return text

def quiz(text, answers):#takes in 2 parameters  and outputs text of a particular chosen level, then checks for answer fot that level and if correct prints out the text with blanks replaced with answers

    subs_number, answers_number, game_end, number_of_blanks = 0, 0, 4, 1

    while number_of_guesses >= 1:
        blanks = ["__" + str(number_of_blanks) + "__"]
        print text
        user_input = raw_input(subs[subs_number])
        if user_input == answers[answers_number]:
            print "Correct!\n\n"
            text = replace_blanks(text, blanks, user_input)
            subs_number += 1
            answers_number += 1
            number_of_blanks += 1
            if answers_number == game_end:
                print "\nYou won!"
                sys.exit()
        else:
            print "\nThis isn't the correct answer! Let's try again...\n"

while number_of_tries >= 0:#keeps checking if level is chosen
    user_input = raw_input('Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard.\n')#takes as input difficulty level

    if user_input == "easy":
        print quiz(easy_text, easy_answers)
    if user_input == "medium":
        print quiz(medium_text, medium_answers)
    if user_input == "hard":
        print quiz(hard_text, hard_answers)
    else:
        print "That's not an option!\n"
        number_of_tries += 1
