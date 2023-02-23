import time
import string


def typewriter_simulator(message):
    '''
    typewriter_simulator function gives a typewritter effect( haracter by character) to a message print
    ''' 
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(0.2)
        time.sleep(0.01)
    print('')


def print_pause(message, delay=1):
    '''
    print_pause function gives a short pause after the typewritter message print
    '''     
    typewriter_simulator(message)
    time.sleep(delay)
