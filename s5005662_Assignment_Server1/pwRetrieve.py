import os  # Importing functions that shall be used throughout the program
import zipfile as zfile
from matplotlib import pyplot as mpl
import numpy as nmpy


def menu_input():  # Outputting options for
    print ""
    print "Menu Options:"
    print "1: Search through files to find a keyword"
    print "2: Exit program"
    print ""
    return raw_input("Input menu select: ")  # Returning the user input to the


def keyword_search():
    print ""
    return raw_input("Enter keyword to search by: ")


def encoding_type():
    print ""
    return raw_input("Enter the decoding style: ")


def selection(user_input):
    if user_input == "1":
        search_files(keyword_search(), encoding_type())
    elif user_input == "2":
        quit()
    else:
        print "Invalid input"


def search_files(keyword, type_encoding):
    pw_file_count = 0
    total_file_count = 0
    for root, dirs, files in os.walk("received_files/documents"):
        for each_file in files:
            path = root + "/" + each_file
            pw_file_count += 1
            total_file_count += 1
            current_file = open(path, "r")
            encoded_text = current_file.read()
            decoded_text = encoded_text.decode(encoding=type_encoding)
            current_file.close()
            if keyword in decoded_text:
                print ""
                search_result(pw_file_count, decoded_text, keyword)
    print ""
    print "The total number of files searched through is: {}".format(total_file_count)


def search_result(pwf_count, text, kw):
    print "The number of files searched through to find the password was: {}".format(pwf_count)
    print ""
    print "The text in the file is: {}".format(text)
    split_text(text, kw)


def split_text(text, keyword):
    pw_index = text.index(str(keyword))
    text = text[pw_index+14:]
    print "The password is: {}".format(text)
    unzip_secret(text)


def menu2_input():
    print ""
    print "Menu Options:"
    print "1: Create a histogram of data"
    print "2: Exit program"
    return raw_input("Input menu select: ")


def selection2(user_input2):
    if user_input2 == "1":
        create_histogram()
    else:
        print "Invalid input"


def unzip_secret(pw):
    zf = zfile.ZipFile("received_files/secret.zip")
    zf.extractall("received_files", pwd=pw)


def create_histogram():
    y = nmpy.genfromtxt('received_files/data.txt')
    mpl.hist(y, 50, normed=1, facecolor="y", edgecolor="g")
    mpl.xlabel("X-axis")
    mpl.ylabel("Y-axis")
    mpl.title("Histogram of data.txt")
    mpl.grid(True)
    mpl.show()


selection(menu_input())
selection2(menu2_input())

