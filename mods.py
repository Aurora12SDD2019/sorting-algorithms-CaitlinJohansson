""" Modules of Standard algorithms functions for the SDD course.

This scirpt will contain functions corresponding to all of the standard
algorithms listed in the course specs for the HSC SDD course

"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"

""" revision notes:


"""

#include statements


def function_name(arg1, arg2, other_silly_variable=None):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    pass

class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""



def loadArray():
    """load data into an array.

    prompts the user to enter data and
    loads that data into an array.

    Args:

    Returns:

    Raises:

    """
    thisArray = []
    i = 0
    dataValue = input("please enter some data, or 'xxx' to quit: ")
    
    while dataValue != 'xxx':
        thisArray.append(dataValue)
        i = i + 1
        dataValue = input("please enter some data, or 'xxx' to quit: ")

    numElements = i
    print("There are " + str(numElements) + " items in the array")

def printArray():
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    print("printArray called")
