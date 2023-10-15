"""""
Author: Ruth in collabration with James
Description: This is a python code to design an ATM Machine
Date: 14th October,2023
"""""
import os
from time import sleep
from random import randint
default_balance = float(randint(1000, 10000))
while True:
    print('* ' * 40, " \n\t\t\t\t FIRST BANK NIG PLC\n\t\t\t\t\t ATM Simulator")
    print(f"\tYour current balance is :$ {default_balance}")

    print_state = "\n\t\t\t\t\t Deposit: D\n\t\t\t\t\tWithdraw: W\n\t\t\t\t\t To Quit: Q"
    print(print_state)
    print('* ' * 40)
    User_input = input("Enter a selection $ ")
    # print(User_input)
    if User_input.upper() == "D":
        depo = float(input("Enter amount of transaction : "))
        if depo < default_balance or depo > default_balance:
            default_balance += depo
            print('* ' * 40)
            print(f"\t\tYour current balance is:$ {default_balance} ")
            print('* ' * 40)

    elif User_input.upper() == "W":
        withdraw = float(input("Enter amount of transaction : "))
        if withdraw <= default_balance:
            default_balance -= withdraw
        else:
            print('* ' * 40)
            print("\tINSUFFICIENT FUNDS")
            print('* ' * 40)
    elif User_input.upper() == "Q":
        print("\t\tGOODBYE")
        print('* ' * 40)
        break

    else:
        print("INVALID SELECTION \n", '* ' * 40)
    sleep(3)
    os.system('cls'if os.name == 'nt' else'clear')
