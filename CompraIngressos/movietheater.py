import numpy as np
from colorama import Back, init, Style
from os import system, name
from time import sleep


class MovieTheater:
    availableseats = list()
    reservedseats = list()

    def __init__(self, line, column):
        self._line = line
        self._column = column

    @property
    def line(self):
        return self._line

    @line.setter
    def linesetter(self, line):
        self._line = line

    @property
    def column(self):
        return self._column

    @column.setter
    def columnSetter(self, column):
        self._column = column

    def canceltickets(self):
        self.cleanscreen()
        print('-' * 78 + f'\n {"Cancel Tickets":^78}\n' + '-' * 78)
        self.movieroom()
        if len(self.reservedseats) == 0:
            print('\nThere are no reserved seats, so cancellation is not possible.')
            sleep(2)
        else:
            seat = self.validateint(msg=f'Enter the seat you wish to cancel: ',
                                       msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to cancel: ')
            while seat in self.availableseats:
                seat = self.validateint(msg='The chosen seat is available for purchase. Please choose another seat: ',
                                            msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to cancel: ')
            while seat <= 0 or seat > 112:
                seat = self.validateint(msg='Non-existent seat. Please choose another seat: ',
                                            msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to cancel: ')
                while seat in self.availableseats:
                    seat = self.validateint(
                        msg='The chosen seat is available for purchase. Please choose another seat: ',
                        msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to cancel: ')
            self.availableseats.append(seat)
            self.reservedseats.remove(seat)

    def buytickets(self):
        self.cleanscreen()
        print('-' * 78 + f'\n {"Buy Tickets":^78}\n' + '-' * 78)
        self.movieroom()
        amount = self.validateint(msg='How many tickets do you want to buy? ',
                                      msgerro='The value entered is not valid. Please enter a valid quantity.\nHow many tickets do you want to buy? ')
        if amount == 112:
            print("You have reserved the entire room for this session. \nEnjoy your movie and don't forget your popcorn.")
            exit()
        else:
            countamount = 1
            while countamount <= amount:
                self.cleanscreen()
                print('-' * 78 + f'\n {"Buy Tickets":^78}\n' + '-' * 78)
                self.movieroom()
                seats = self.validateint(msg=f'Enter the {countamount}º seat you wish to reserve: ',
                                            msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to reserve: ')

                while seats in self.reservedseats:
                    seats = self.validateint(
                        msg='The chosen seat is already reserved. Please choose another seat: ',
                        msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to reserve: ')
                while seats <= 0 or seats > 112:
                    seats = self.validateint(msg='Non-existent seat. Please choose another seat: ',
                                                msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to reserve: ')
                    while seats in self.reservedseats:
                        seats = self.validateint(
                            msg='The chosen seat is already reserved. Please choose another seat: ',
                            msgerro='The value entered is not valid. Please enter a valid seat.\nEnter the seat you wish to reserve: ')
                self.availableseats.remove(seats)
                self.reservedseats.append(seats)
                countamount += 1
            sleep(1)

    def movieroom(self):
        cont = 1
        init(autoreset=True)
        # Cria a sala automaticamente, o tamanho da sala é definido ao chamar a classe, pelas variaveis linha e coluna pois pode ser mutável.
        room = np.arange(1, self.linesetter * self.columnSetter + 1)
        room = ' '.join(str(e) for e in room)
        room = np.asarray(room.split(sep=' ')).reshape(self.linesetter, self.columnSetter)
        for l in range(self.linesetter):
            for c in range(self.columnSetter):
                if l == 0 and c == 5:
                    room[l][c] = 'S'
                    print(f'{room[l][c]:^4}', end=' ')
                elif l == 0 and c == 6:
                    room[l][c] = 'C'
                    print(f'{room[l][c]:^4}', end=' ')
                elif l == 0 and c == 7:
                    room[l][c] = 'R'
                    print(f'{room[l][c]:^4}', end=' ')
                elif l == 0 and c == 8:
                    room[l][c] = 'E'
                    print(f'{room[l][c]:^4}', end=' ')
                elif l == 0 and c == 9:
                    room[l][c] = 'E'
                    print(f'{room[l][c]:^4}', end=' ')
                elif l == 0 and c == 10:
                    room[l][c] = 'N'
                    print(f'{room[l][c]:^4}', end=' ')
                elif l == 0 or l == 1:
                    room[l][c] = ' '
                    print(f'{room[l][c]:^4}', end=' ')
                elif c == 4 or c == 11:
                    room[l][c] = 'C'
                    print(f'{room[l][c]:^4}', end=' ')
                else:
                    if cont in self.reservedseats:
                        room[l][c] = cont
                        print(f'{Back.RED}{room[l][c]:^4}', end=' ')
                    else:
                        room[l][c] = cont
                        print(f'{Back.GREEN}{room[l][c]:^4}', end=' ')
                        if cont not in self.availableseats:
                            self.availableseats.append(cont)
                    cont += 1
            print(' ')

    def cleanscreen(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def salesreport(self):
        print(' ')
        print(f'''{Back.RED}{len(self.reservedseats)}{Style.RESET_ALL} tickets have been sold.
We have available {Back.GREEN}{len(self.availableseats)}{Style.RESET_ALL} tickets.\n''')

    def savereport(self):
        self.reservedseats.sort()
        self.availableseats.sort()
        with open('seatlist.txt', 'w', encoding='utf-8') as file:
            file.write('-' * 30)
            file.write(f'\n{"Seat List":^30}\n')
            file.write('-' * 30)
            file.write('\nAvailable Seats: ' + f'{self.availableseats}')
            file.write('\nReserved Seats: ' + f'{self.reservedseats}')

    def validateint(self, msg, msgerro):
        try:
            x = int(input(msg))
        except(TypeError, ValueError):
            x = int(input(msgerro))
        return x
