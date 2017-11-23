import os
import matplotlib


def menu():
    menu_option = raw_input("Input menu option: ")


def search_files():
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
            if "Millenium2000" in decoded_text:
                password = decoded_text
                print "The number of files searched through to find the password was: {}".format(pw_file_count)
    print "The total number of files searched through is: {}".format(total_file_count)
    return password

# def split_text():



print search_files()

menu()
