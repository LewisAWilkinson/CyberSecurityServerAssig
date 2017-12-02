import s5005662_Assignment_Server1.source_code.pwRetrieve as pWR  # Importing pwRetrieve
import s5005662_Assignment_Server2.source_code.decode as dC  # Importing decode22


def main_menu():
    print "1: Server 1"
    print "2: Server 2"
    return raw_input("Input menu option here: ")


def main_selection(main_menu_input):
    if main_menu_input == "1":
        pWR.selection(pWR.menu1_input())  # Calling the selection function using the returned value from menu1_input
        pWR.selection2(pWR.menu2_input())  # Calling the selection function using the returned value from menu2_input
        go_to_server2()
    elif main_menu_input == "2":
        dC.decode_text()
    else:
        print "Invalid input"


def go_to_server2():
    print ""
    s2_input = raw_input("Would you like to access server 2? (Y/N): ")
    if s2_input == "Y" or s2_input == "y":
        main_selection("2")
    elif s2_input == "N" or s2_input == "n":
        quit()
    else:
        print "Invalid input"


main_selection(main_menu())


