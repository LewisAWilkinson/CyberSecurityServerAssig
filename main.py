import s5005662_Assignment_Server1.source_code.pwRetrieve as pWR  # Importing pwRetrieve
import s5005662_Assignment_Server2.source_code.decoder as dC


def main_menu():
    print "1: Server 1"
    print "2: Server 2"
    return raw_input("Input menu option here: ")


def main_selection(main_menu_input):
    if main_menu_input == "1":
        pWR.selection(pWR.menu1_input())  # Calling the selection function using the returned value from menu1_input
        pWR.selection2(pWR.menu2_input())  # Calling the selection function using the returned value from menu2_input
    elif main_menu_input == "2":
        print"test"
    else:
        print "Invalid input"


main_selection(main_menu())


