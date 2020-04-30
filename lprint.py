import sys
import time

class printer:
    def __init__(self, logfile=None, mode='default'):
        if logfile == None:
            self.logmode = False
        else:
            try:
                self.logfile = open(logfile, 'w')
                self.logmode = True
            except:
                self.logmode = False
        
        if mode == 'default':
            self.head_function = head_default
            self.tail_function = tail_default
            self.text_function = text_default

    def print_head(self):
        self.head_function()

    def print_tail(self):
        self.tail_function()
    
    def print_text(self, *args):
        self.text_function(args)


    def print(self, *args):
        self.head_function()
        self.text_function(args)
        self.tail_function()

def head_default():
    sys.stdout.write('\u001b[36m')
    sys.stdout.write('* ')
    sys.stdout.write('\u001b[0m')
    sys.stdout.write((time.ctime(time.time())))
    sys.stdout.write('\u001b[31;1m')
    sys.stdout.write(' - ')
    sys.stdout.write('\u001b[0m')

def tail_default():
    sys.stdout.write('\u001b[36m')
    sys.stdout.write(' .')
    sys.stdout.write('\u001b[0m')
    sys.stdout.write('\n')

def text_default(args):
    text = ''
    for value in args:
        if isinstance(value, str):
            text += value + ' '
        else:
            text += repr(value) + ' '
    text = text[:-1]
    sys.stdout.write(text)


def lprint(*args, **kwargs):
    if len(args) == 0:
        return

    text = ''
    for value in args:
        if isinstance(value, str):
            text += value + ' '
        else:
            text += repr(value) + ' '
    text = text[:-1]
    sys.stdout.write('\u001b[36m')
    sys.stdout.write('* ')
    sys.stdout.write('\u001b[0m')
    sys.stdout.write((time.ctime(time.time())))
    sys.stdout.write('\u001b[31;1m')
    sys.stdout.write(' - ')
    sys.stdout.write('\u001b[0m')
    try:
        sys.stdout.write(text)
    except:
        sys.stdout.write('error')
    sys.stdout.write('\n')
