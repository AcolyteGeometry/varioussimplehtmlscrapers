## Class for printing a menu and returning selection.
class MenuT:

    ## The Constructor
    def __init__(self):
        pass

    ## Print a menu to console, return selection
    #  @type self: MenuT
    #  @param self: The object
    #
    #  @type menu: a python list of lists in the form
    #  [["Menu", "Select an option: "], ["Option 1", 1], ["Option 2", 2], ["Option 3", 3]]
    #  @param menu: The menu to print containing title, and possible expected options, or none for standard input.
    #
    #  @rtype:
    def showMenu(self, menu = [["Menu", "Select an option: "], ["Option 1", 1], ["Option 2", 2], ["Option 3", 3]]):
        for i in range(len(menu)):
            if(i==0):
                print("\n" + menu[i][0])
            else:
                print("(" + str(menu[i][1]) + ") " + menu[i][0])
        ret = input("\n" + menu[0][1])
        return ret

    ## String to integer
    #  @type self: MenuT
    #  @param self: The object
    #
    #  @type str: string
    #  @param str: the integer string to convert
    #
    #  @rtype: int
    #  @return: The integer from string or 0 on error.
    def stoi(self, str):
        if (str.isdigit()):
            str = int(str)
            return str
        return 0




