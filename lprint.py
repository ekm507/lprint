import sys
import time

# define a printer object with its specified preferences
class printer:
    """This class provides you with print function and some other options
    """

    def __init__(self, file=None, function='default', separator=' ', shellmode=True):
        # check if you are to write to a file also
        if file == None:
            self.logmode = False
        else:
            # get a file to print tos
            self.logfile = file
            self.logmode = True
        
        # set if we need to print into sys.out too
        self.shellmode = shellmode

        # get print function mode
        if function == 'default':
            # set print functions
            self.head_function = head_default
            self.tail_function = tail_default
            self.text_function = text_default

            # set file print functions
            self.fhead_function = fhead_default
            self.ftail_function = ftail_default
            self.ftext_function = ftext_default
            
        
        # set separator string
        self.separator = separator

    # print initials
    def print_head(self):
        """prints only the header and exits"""
        self.head_function()

    # print endings
    def print_tail(self):
        """prints only the tail and exits"""
        self.tail_function()
    
    # print main text body
    def print_text(self, args):
        """prints only the text body without head or tail"""
        self.text_function(args, seperator=self.separator)
    

    # print initials into file
    def fprint_head(self):
        """prints only the header and exits"""
        self.fhead_function(self.logfile)

    # print endings into file
    def fprint_tail(self):
        """prints only the tail and exits"""
        self.ftail_function(self.logfile)
    
    # print main text body into file
    def fprint_text(self, args):
        """prints only the text body without head or tail"""
        self.ftext_function(args, seperator=self.separator, file=self.logfile)

    # main function
    # prints anything you give it in a formatted way
    def print(self, *args):
        """print anything in formatted mode"""

        # print into sys.out if it is required
        if self.shellmode == True:
            # print the initials first
            self.print_head()
            # then the main text
            self.print_text(args)
            # finally print the endings
            self.print_tail()
        
        # if it is required to print into file
        if self.logmode == True:
            # print the initials first into file
            self.fprint_head()
            # then the main text into file
            self.fprint_text(args)
            # finally print the endings into file
            self.fprint_tail()


# default head print function for printer
def head_default():
    # set shell color to cyan
    sys.stdout.write('\u001b[36m')
    sys.stdout.write('* ')
    # set shell color to default
    sys.stdout.write('\u001b[0m')
    # print current system time
    sys.stdout.write((time.ctime(time.time())))
    # set shell color to bright red
    sys.stdout.write('\u001b[31;1m')
    sys.stdout.write(' - ')
    # set shell color to default
    sys.stdout.write('\u001b[0m')

# default tail print function for printer
def tail_default():
    # set shell color to cyan
    sys.stdout.write('\u001b[36m')
    sys.stdout.write(' .')
    # set shell color to default
    sys.stdout.write('\u001b[0m')
    # it is necessary to print a newline at the end
    # otherwise it will be a mess
    sys.stdout.write('\n')

# default text body print function for printer
def text_default(args, seperator=' '):
    # generate a printable text based on args
    text = ''
    for value in args:
        # if value is string, it should be printed directly
        if isinstance(value, str):
            text += value + seperator
        else:
            # otherwise repr function should be used
            text += repr(value) + seperator
    text = text[:-len(seperator)]
    # write the generated text
    sys.stdout.write(text)


# default head print function for printer
def fhead_default(file):
    file.write('* ')
    # print current system time
    file.write((time.ctime(time.time())))
    file.write(' - ')

# default tail print function for printer
def ftail_default(file):
    file.write(' .')
    # it is necessary to print a newline at the end
    # otherwise it will be a mess
    file.write('\n')

# default text body print function for printer
def ftext_default(args, seperator=' ', file=None):

    # do nothing if there is no file!
    if file == None:
        return

    # generate a printable text based on args
    text = ''

    # get args to print
    for value in args:
        # if value is string, it should be printed directly
        if isinstance(value, str):
            text += value + seperator
        else:
            # otherwise repr function should be used
            text += repr(value) + seperator
    text = text[:-len(seperator)]
    # write the generated text
    file.write(text)


# old lprint function still supported for a simple and fast way of printing
def lprint(*args, **kwargs):
    """prints anything it gets in a specified way
    """
    # check if there are any inputs
    if len(args) == 0:
        return

    # generate printable text body
    text = ''
    # get input from args
    for value in args:
        # for strings, we will print them directly
        if isinstance(value, str):
            text += value + ' '
        # for others we will use repr function
        else:
            text += repr(value) + ' '
    # clear the last whitespace character :)
    text = text[:-1]

    #print the initials
    sys.stdout.write('\u001b[36m')
    sys.stdout.write('* ')
    sys.stdout.write('\u001b[0m')
    sys.stdout.write((time.ctime(time.time())))
    sys.stdout.write('\u001b[31;1m')
    sys.stdout.write(' - ')
    sys.stdout.write('\u001b[0m')

    # print the text body
    try:
        sys.stdout.write(text)
    except:
        sys.stdout.write('error')
    
    # print the endings
    sys.stdout.write('\n')
