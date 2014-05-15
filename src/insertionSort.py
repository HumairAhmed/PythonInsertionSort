#/****************************************************************/ 
# Program:  insertionSort
# Version:  1.0
# Date:     05/14/2014
# Website:  http://www.HumairAhmed.com
#
# Lead Developer:   Humair Ahmed 
#
# Written for educational purposes. Program takes a list of numbers from a file
# named 'UNSORTED' and sorts the list while counts each iteration. Displays 
# the final sorted list at end and how long it took to sort in seconds. Results 
# are also written to a file named 'SORTED'. Program also demonstrates how to use
# many file functions from the 'os' library.
# 
#  
# License:
# 
# Open source software being distributed under GPL license. For more information see here:
# http://www.gnu.org/copyleft/gpl.html. 
# 
# Can edit and redistribute code as long as above reference of authorship is kept within the code.
#/****************************************************************/

import time, os


#function reads unsorted list from file and returns unsorted list
def getUnsortedList(fileName):
    f = open(fileName, "r")   #open file with unsorted numbers as 'read-only'
    unsortedList = (f.readline()).split()
    f.close()
    
    return unsortedList       #return unsorted list read from file



#function sorts list argument and returns sorted list
def insertionSort(unsortedList):
    global iterations #holds # of sort iterations
    
    for index in range(1, len(unsortedList)):
        i = index - 1 
        markerVal = unsortedList[index]
        while (unsortedList[i] > markerVal) and (i >= 0):
            unsortedList[i + 1] = unsortedList[i]
            i -= 1
            iterations += 1
        unsortedList[i + 1] = markerVal
        
    return unsortedList



#function saves sortedList argument to file
def saveSortedList(fileName, sortedList):
    f = open(fileName, "w")
    
    for number in sortedList:
        f.write(number + " ")
        
    f.close()



def main():
    global iterations #holds # of sort iterations
    unsortedFileName = "UNSORTED"
    sortedFileName= "SORTED"
    
    iterations= 0
    
    os.chdir("..")        #change directory to one upper-level
    cwd = os.getcwd()     #get current working directory pathname
    dataDir = os.path.join(cwd, 'data')
    
    unsortedFileName = os.path.join(dataDir, unsortedFileName)
    time_started = time.time()
    sortedFileName = os.path.join(dataDir, sortedFileName)
    time_stopped = time.time()
    
    time_passed = time_stopped - time_started
    
    
    unsortedList = getUnsortedList(unsortedFileName)
    unsortedList = list(map(int, unsortedList)) #convert all items in list to int
    
    sortedList = insertionSort(unsortedList)
    
    print("\nSorted after", iterations, "iterations.")
    print("Sorted:  ", sortedList) 
    print("\nOverall Time:", time_passed, "seconds\n") 
    
    sortedList= map(str, sortedList) #convert all items in list to string
    saveSortedList(sortedFileName, sortedList)
    
    
    
if __name__ == "__main__":
    main()

    