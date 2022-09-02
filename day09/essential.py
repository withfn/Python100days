import os
from time import sleep
def clear():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        sleep(2)
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''