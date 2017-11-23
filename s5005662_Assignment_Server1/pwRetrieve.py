import os
from matplotlib import pyplot


def menu_input():
    print""
    print"Menu Options:"
    print"1: Search through files to find a keyword"
    print"2: Display a histogram of the data found"
    print""
    return raw_input("Input menu select: ")


def keyword_search():
    return raw_input("Enter keyword to search by: ")


def encoding_type():
    return raw_input("Enter the decoding style: ")


def selection(user_input):
    if user_input == "1":
        search_files(keyword_search())
        search_files(encoding_type())
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
                all_text = decoded_text
                print""
                print "The number of files searched through to find the password was: {}".format(pw_file_count)
    print "The total number of files searched through is: {}".format(total_file_count)
    print""
    print "The text in the file is: {}".format(all_text)
    split_text(all_text, keyword)
    file_found(all_text)


def file_found(text):
    if text == "":
        print "File has not been found"


def split_text(text, keyword):  # index of whole file to remove and print pw
    pw_text = text.index(str(keyword))
    pw_text = text[200+14:]
    print "The password is: {}".format(pw_text)



selection(menu_input())


