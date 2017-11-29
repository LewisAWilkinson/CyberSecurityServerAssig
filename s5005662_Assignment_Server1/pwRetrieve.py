import os  # Importing functions that shall be used throughout the program
import zipfile as zfile
from matplotlib import pyplot as mpl
import numpy as nmpy
import unzip
import searchFiles as sFiles


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
        sFiles.search_files(keyword_search(), encoding_type())  # Passes the result of the two functions into search_files
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
        create_histogram()
    elif user_input2 == "2":
        quit()
    else:
        print "Invalid input"


def create_histogram():  # Creating a histogram of data using the data.txt
    y = nmpy.genfromtxt('received_files/data.txt')
    mpl.hist(y, 50, normed=1, facecolor="y", edgecolor="g")  # Cosmetic changes to the histogram
    mpl.xlabel("X-axis")  # Labelling the axis
    mpl.ylabel("Y-axis")  # ^
    mpl.title("Histogram of data.txt")  # Titling the histogram
    mpl.grid(True)  # Showing a grid to make reading the histogram easier
    mpl.show()


selection(menu1_input())  # Calling the selection function using the returned value from menu1_input
selection2(menu2_input())  # Calling the selection function using the returned value from menu2_input
