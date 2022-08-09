from movietheater import MovieTheater


def mainMenu():
    movie01 = MovieTheater(10, 16)
    print('-' * 35 + f'\n{"Welcome to CineCode":^35}\n' + '-' * 35 + f'\n{"Menu":^35}', end='')
    print(f'''
    {"[ 1 ] Buy Tickets":<35} 
    {"[ 2 ] Cancel Tickets":<35}
    {"[ 3 ] Sales Report":<35}
    {"[ 4 ] Exit":<35}''', end='')
    option = msgInt('\nChoose one of the options above: ')
    while True:
        if option == 1:
            movie01.buytickets()
            movie01.cleanscreen()
            mainMenu()
        elif option == 2:
            movie01.canceltickets()
            movie01.cleanscreen()
            mainMenu()
        elif option == 3:
            movie01.cleanscreen()
            print('-' * 78 + f'\n{"Sales Report":^78}\n' + '-' * 78)
            movie01.movieroom()
            movie01.salesreport()
            menu = str(input('Press Enter to return to Main Menu... '))
            movie01.cleanscreen()
            exit(mainMenu())
        elif option == 4:
            movie01.savereport()
            exit()
        else:
            option = msgInt(
                'The option you entered is not valid, please choose a valid option.\nChoose one of the options above:')

def msgInt(msg):
    try:
        n = int(input(msg))
    except(ValueError, TypeError):
        n = int(input('The option you entered is not valid, please choose a valid option.' + msg))
    return n


mainMenu()
