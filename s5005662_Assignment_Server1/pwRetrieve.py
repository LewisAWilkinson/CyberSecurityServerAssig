import os
from matplotlib import pyplot


def menu_input():
    print("")
    print("Menu Options:")
    print("1: Search through files to find a keyword")
    print("2: Display a histogram of the data found")
    print("")
    return raw_input("Input menu select: ")


def keyword_search():
    return raw_input("Enter keyword to search by: ")


def selection(user_input):
    if user_input == "1":
        search_files(keyword_search())
    else:
        print "Invalid input"


def search_files(keyword):
    pw_file_count = 0
    total_file_count = 0
    for root, dirs, files in os.walk("received_files/documents"):
        for eachfile in files:
            path = root + "/" + eachfile
            pw_file_count += 1
            total_file_count += 1
            current_file = open(path, "r")
            encoded_text = current_file.read()
            decoded_text = encoded_text.decode(encoding="Hex")
            current_file.close()
            if keyword in decoded_text:
                all_text = decoded_text
                print("")
                print "The number of files searched through to find the password was: {}".format(pw_file_count)
    print "The total number of files searched through is: {}".format(total_file_count)
    print("")
    print "The text in the file is: {}".format(all_text)
    split_text(all_text)


def split_text(text):  # index of whole file to remove and print pw
    pw_text = text.index("Millenium2000")
    pw_text = text[200+14:]
    print "The password is: {}".format(pw_text)



selection(menu_input())


