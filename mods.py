""" Project name.

Description
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"

""" revision notes:


"""

#include statements

#modules
def FindMin(inArray):
    """Finds the minimum value in an array

    Args:
        inArray: the array to find the max value in

    Returns:
        minArray: an array of the min value and the index of the min value

    Raises:
        None.
    """
    return [None, None]
    print("FindMin run as a stub")

def LinearSearch(inArray, target):
    """Performs a linear search.

    accepts a target value and checks every element of the array
    to be searched in turn, until either a match is found or
    the end of the array is reached.

    Args:
        inArray: the array to find the max value in
        target: the value to be found

    Returns:
        targetIndex: the index for the target or -1 if not found

    Raises:
        None.
    """
    print("LinearSearch run as a stub")
    
def BinarySearch(inArray, target):
    """Performs a binary search.

    divides the data set into two parts and determines
    in which part the element is to be found. That part
    of the array is again divided into two parts and a
    further decision is made as to which part may
    contain the target value. The process is continued
    until either the value is found or there are no
    more elements in the data set to be checked.

    Args:
        inArray: the array to find the max value in
        target: the value to be found

    Returns:
        targetIndex: the index for the target or -1 if not found

    Raises:
        None.
    """
    print("BinarySearch run as a stub")


def BubbleSort(inArray):
    """Performs a bubble sort.

    the elements are compared in pairs and swapped
    if necessary. In this way, the larger of the
    pair ‘bubbles’ towards one end of the array.
    After each pass one more element will have
    moved to its correct position in the array.

    Args:
        inArray: the array to be sorted

    Returns:
        sortedArray: a copy of the array that has been sorted

    Raises:
        None.
    """
    print("BubbleSort run as a stub")
    sortedArray = [None]
    return sortedArray


def SelectionSort(inArray):
    """Performs a selection sort.

    logically divide the array into two parts
    – an unsorted part and a sorted part.
    Each pass through the unsorted part finds
    the largest value and places it at the
    start of the sorted part. Initially the
    sorted part is empty. The size of the
    sorted part of the array increases by
    1 with each pass.

    Args:
        inArray: the array to be sorted

    Returns:
        sortedArray: a copy of the array that has been sorted

    Raises:
        None.
    """
    print("SelectionSort run as a stub")
    sortedArray = [None]
    return sortedArray


def InsertionSort(inArray):
    """Performs an insertion sort.

    logically divide the array into two parts
    – an unsorted part and a sorted part.
    Each pass through the unsorted part takes
    the end value of the unsorted part and
    places it in the correct position. It
    achieves this by successively moving
    the correct number of elements in the
    sorted part by one position to make room.
    Initially the sorted part contains one element.
    The size of the sorted part of the array
    increases by 1 with each pass.

    Args:
        inArray: the array to be sorted

    Returns:
        sortedArray: a copy of the array that has been sorted

    Raises:
        None.
    """
    print("InsertionSort run as a stub")
    sortedArray = [None]
    return sortedArray

def InsertElement(inArray, element):
    """Inserts an element into the correct position of a sorted array.

    inserts a new name into its correct position in an
    existing array, which is already in ascending order.

    Args:
        inArray: the array to be sorted

    Returns:
        editedArray: a copy of the array that has the
        element inserted in the correct position

    Raises:
        None.
    """
    print("InsertElement run as a stub")
    editedArray = [None]
    return editedArray
    


def FindMax(inArray):
    """Finds the maximum value in an array

    Args:
        inArray: the array to find the max value in

    Returns:
        maxArray: an array of the max value and the index of the max value

    Raises:
        None.
    """
    maxIndex = 0
    max = inArray[maxIndex]
    i = 0
    while i < len(inarray):
        if inArray[i] > max:
            max = inarray[i]
            maxIndex = i
    
    print("The maximum value is {} at position {}".format(max, maxIndex))
    
    return [max, maxIndex]


def sumArrayContents(thisArray):
    """Sums the contents of an array.

    Args:
        thisarray: the array which you want to sum the contents of.

    Returns:
        total: sum of the array.

    Raises:
        TypeError.
    """
    i = 0
    total = 0
    while i < len(thisArray):
        thisValue = thisArray[i]
        if thisValue.isnumeric():  # check to see if array value is number
            thisValue = eval(thisValue)  # change the value to a number
            total = total + thisValue 
        else:  # if not a number print massage and skip
            print("{} is invalid: you can only add numbers".format(thisValue))
        i = i + 1

    print("The sum for this array is {}".format(total))
    return total


def printArrayContents(thisArray):
    """prints the contents of an array.

    
    Args:
        thisArray: the array to be printed.

    Returns:
        None

    Raises:
        None.
    """
    i = 0 #indices in python start at 0
    while i < len(thisArray):
        print(thisArray[i], end="\t")
        i = i + 1
    
    print('\n')



def loadArray(inArray):
    """Appends data to an array.

    prompt the user to add data to an existing array

    Args:
        inArray: the array to which the data will be added

    Returns:
        outArray: the modified array

    Raises:
        None.
    """
    outArray = inArray[:]  # this creates a copy of inArray
    newData = input("enter the new data to add to the array, or 'Q' to quit: ")
    while newData != "Q":
        outArray.append(newData)
        newData = input("enter the new data to add to the array, or 'Q' to quit: ")
    print("There are now {} elements in the array".format(len(outArray)))
    return outArray



##### templates
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



