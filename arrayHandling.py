""" A script to test the array handling standard algorithms.
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"


""" revision notes:


"""

#include statements
from mods import *
import random

#other setup stuff


#now the real stuff we came here for
def main():
    #first lets make a 10 element array with random numbers between 1 and 100
    firstArray = []
    while len(firstArray) < 10:
        firstArray.append(random.randrange(1, 100))
    
    #now lets use our printArrayContents funtion to see what that looks like
    printArrayContents(firstArray)
    
    #now find the minimum value in the array
    firstArrayMin = FindMin(firstArray)
    # uncomment the following line when findMin is working
    print("the minimum value is {} at index {}".format(firstArrayMin[0], firstArrayMin[1]))
    
    #look for the number 42 in the array using linear search
    targetValue = 42
    targetIndex = LinearSearch(firstArray, targetValue)
    print("the target {} was found at index {}".format(targetValue, targetIndex))
        
    #look for the number 66 in the array using binary search
    targetValue = 66
    targetIndex = BinarySearch(firstArray, targetValue)
    print("the target {} was found at index {}".format(targetValue, targetIndex))
        
    # now do a bubble sort
    bubbleSortedArray = BubbleSort(firstArray)
    printArrayContents(bubbleSortedArray)
    
    # and a selection sort
    selectionSortedArray = SelectionSort(firstArray)
    printArrayContents(selectionSortedArray)
    
    
    # and an insertion sort
    insertedSortedArray = InsertionSort(firstArray)
    printArrayContents(insertedSortedArray)
    
    # finally lets insert a new element in the correct place
    newElement = 7
    secondArray = InsertElement(bubbleSortedArray, newElement)
    printArrayContents(secondArray)

if __name__ == '__main__':
    main()    

        
