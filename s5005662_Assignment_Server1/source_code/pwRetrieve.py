import searchFiles as sFiles
import createHistogram as cF


def menu1_input():  # First menu allowing the user to search through the files or quit the program
    print ""
    print "Menu Options:"
    print "1: Search through files to find a keyword"
    print "2: Exit program"
    print ""
    return raw_input("Input menu select: ")  # Returning the input for later use


def keyword_search():  # Allows the user to search for a keyword in the file search
    print ""
    return raw_input("Enter keyword to search by: ")


def encoding_type():  # Allows the user to choose the decoding style for the file's text
    print ""
    return raw_input("Enter the decoding style: ")


def selection(user_input):  # Takes the menu1 input and performs the function the user has selected
    if user_input == "1":
        sFiles.search_files(keyword_search(), encoding_type())  # Passes the result of the two functions into
        # search_files
    elif user_input == "2":
        quit()
    else:
        print "Invalid input"


def menu2_input():  # Second menu where the user can select whether to display a histogram or quit the program
    print ""
    print "Menu Options:"
    print "1: Create a histogram of data"
    print "2: Exit program"
    return raw_input("Input menu select: ")


def selection2(user_input2):  # Takes the menu2 input and performs the function the user has selected
    if user_input2 == "1":
        cF.create_histogram()
    elif user_input2 == "2":
        quit()
    else:
        print "Invalid input"
