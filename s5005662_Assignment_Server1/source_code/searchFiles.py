import os
import unzip


def search_files(keyword, type_encoding):  # Searches through the file structure
    pw_file_count = 0
    total_file_count = 0
    for root, dirs, files in os.walk("s5005662_Assignment_Server1/received_files/documents"):
        for each_file in files:
            path = root + "/" + each_file
            pw_file_count += 1  # Incrementing the file counts
            total_file_count += 1  # ^
            current_file = open(path, "r")  # Opens the current file
            encoded_text = current_file.read()
            decoded_text = encoded_text.decode(encoding=type_encoding)  # The contents of the file is decoded using the
            # type the user specified, and placed in the variable decoded_text
            current_file.close()
            if keyword in decoded_text:  # Searches through the contents of the file for the keyword the user specified
                search_result(pw_file_count, decoded_text, keyword)  # If the keyword is found within the text of the
                # entire contents of the file is sent to the function search_result, along with the count until the
                # password is found, and the keyword the user searched for
    print ""
    print ""
    print "The total number of files searched through is: {}".format(total_file_count)


def search_result(pwf_count, text, kw):  # Printing the results of the search
    print "The number of files searched through to find the password was: {}".format(pwf_count)
    print ""
    print "The text in the file is: {}".format(text)
    split_text(text, kw)  # Passing the variables text and the keyword the user searched for to the function split_text


def split_text(text, keyword):  # Splitting the password from the text of the file
    pw_index = text.index(str(keyword))  # The position of the keyword in the string is put in the variable pw_index
    text = text[pw_index+14:]  # The everything before the end of the keyword has been stripped, only leaving the
    # password, this is then placed into the variable text as I will no longer be using this
    print "The password is: {}".format(text)
    unzip.unzip_secret(text)  # Passing the variable text into the unzip_secret function
