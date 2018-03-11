
print "Welcome to the best experience of music "


def menu():
    show_menu = True
    while show_menu:

        query = input("1. Listen to your old songs. \n2. Download some new songs. \n3. latest download songs. ")
        if query == 1:
            print "Welcome to old songs"
        elif query ==2:
            print "Please enter the naame of the song"
        elif query == 3:
            print"Your latest songs are- "
        else :
            show_menu = False
menu()


