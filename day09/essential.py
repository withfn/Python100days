import os
def clear():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        sleep(2)
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


logo = '''                                                                                                        
 _____ _          _____     _         _          _   _   _   _ _            _____         _   _         
|_   _| |_ ___   |  _  |___|_|_ _ ___| |_ ___   | |_|_|_| |_| |_|___ ___   |  _  |_ _ ___| |_|_|___ ___ 
  | | |   | -_|  |   __|  _| | | | .'|  _| -_|  | . | | . | . | |   | . |  |     | | |  _|  _| | . |   |
  |_| |_|_|___|  |__|  |_| |_|\_/|__,|_| |___|  |___|_|___|___|_|_|_|_  |  |__|__|___|___|_| |_|___|_|_|
                                                                    |___|                                                                     
'''