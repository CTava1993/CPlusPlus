import re
import string

'''Christian Tavares, CS210 Programming Languages 22EW1, 10/15/2022
   
   This file contains all of the Python functions for this bilingual program.
   Python was meant to do more of the heavy lifting for the back-end stuff, meanwhile 
   C++ was meant to be for the front-end and menus.'''

'''Description:
      This was a default function with the provided files that I kept with the final product.
      It functions just like a "Hello World!" and is printed with the menu screen.
'''
def printSomething():
    print ("Hello, from Python!")

'''Description:
      This function was designed to make loops dynamic for each item in the 'GroceryList.txt' file.
      Will return 99 by default, meaning the item sent did not match an ID.
   Example:
      getItemId('PotAToEs') || returns 5 || Most frequently used as the following: "ItemID = getItemID(item)"
'''
def getItemID(t_item):

    item = t_item #will throw errors if not defined in a new variable

    if item.upper() == "SPINACH": #items
        return 0
    if item.upper() == "RADISHES":
        return 1
    if item.upper() == "BROCCOLI":
        return 2
    if item.upper() == "PEAS":
        return 3
    if item.upper() == "CRANBERRIES":
        return 4
    if item.upper() == "POTATOES":
        return 5
    if item.upper() == "CUCUMBERS":
        return 6
    if item.upper() == "PEACHES":
        return 7
    if item.upper() == "ZUCCHINI":
        return 8
    if item.upper() == "CANTALOUPE":
        return 9
    if item.upper() == "BEETS":
        return 10
    if item.upper() == "CAULIFLOWER":
        return 11
    if item.upper() == "ONIONS":
        return 12
    if item.upper() == "YAMS":
        return 13
    if item.upper() == "APPLES":
        return 14
    if item.upper() == "CELERY":
        return 15
    if item.upper() == "LIMES":
        return 16
    if item.upper() == "GARLIC":
        return 17
    if item.upper() == "PEARS":
        return 18
    else:
        return 99

'''Description:
      This function will create and return a list of every item 'sold' throughout the day.
      The function should work with any additional items that are not currently in the default 'GroceryList.txt' file.
      For it to calculate frequencies however, you would need to add more conditions to getItemID.
   Example:
      listA = getItemFrequency() || Will return an array of integers based on content of 'GroceryList.txt' file.
'''
def getItemFrequency():
    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #instance variables
    itemID = 99

    file = open('GroceryList.txt') #open file

    for line in file: #read each line of file, deleting line breaks then calculates frequency change
        line = line.replace("\n", "")
        itemID = getItemID(line)
        
        if itemID != 99:
            frequency[itemID] = frequency[itemID] + 1

    file.close() #close file

    return frequency #return frequency list

'''Description:
      This function will calculate the frequency of a user defined item by fetching all frequencies through the
      inherited getItemFrequency() function, t
      hen run the user input through getItemID. If it returns something
      OTHER than the default value of 99, it will return the amount of those items that were purchased.
   Example:
      displaySpecificItemFrequency(item) || Will print text to the console showing how many of a specific item was purchased.
'''
def displaySpecificItemFrequency(t_item):
    item = t_item
    itemID = 99 #instance variables

    frequency = getItemFrequency() #fetch frequencies and itemID of user defined item/frequency
    itemID = getItemID(item)
    
    if itemID != 99: #if user defined item exists then the following happens. 99 is a default value
        amount = frequency[itemID] 
        print ("\n%d " %(amount) + item.upper() + " were purchased today. . .")
        print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print ("Type anything to continue. . .")
    else:
        print("Invalid item. . .") #if item doesn't exist'
        print ("Type anything to continue. . .")

    return 1 #a filler return statement since callIntFunc() expects a return value

'''Description:
      This function is called by option 1 and will print up a table that shows each item on the default
      'GroceryList.txt' file provided and how many times they appear on the file. This function is not
      very flexible if you change the contents of the input file.
'''
def displayItemsAndFrequency():
    frequency = []
    frequency = getItemFrequency() #instance variables
    
    print ("Items purchased today:") #print lines of each item and the amount that were purchased
    print ("\nSPINACH:     %d" %(frequency[0]))
    print ("RADISHES:    %d" %(frequency[1]))
    print ("BROCCOLI:    %d" %(frequency[2]))
    print ("PEAS:        %d" %(frequency[3]))
    print ("CRANBERRIES: %d" %(frequency[4]))
    print ("POTATOES:    %d" %(frequency[5]))
    print ("CUCUMBERS:   %d" %(frequency[6]))
    print ("PEACHES:     %d" %(frequency[7]))
    print ("ZUCCHINI:    %d" %(frequency[8]))
    print ("CANTALOUPE:  %d" %(frequency[9]))
    print ("BEETS:       %d" %(frequency[10]))
    print ("CAULIFLOWER: %d" %(frequency[11]))
    print ("ONIONS:      %d" %(frequency[12]))
    print ("YAMS:        %d" %(frequency[13]))
    print ("APPLES:      %d" %(frequency[14]))
    print ("CELERY:      %d" %(frequency[15]))
    print ("LIMES:       %d" %(frequency[16]))
    print ("GARLIC:      %d" %(frequency[17]))
    print ("PEARS:       %d" %(frequency[18]))
    print ("")
    print ("Type anything to continue. . .")

'''Description:
      This function will create a histogram by reading from the 'GroceryList.txt' file. First it will inherit the
      getItemFrequency() function to create a frequency list, then for each element of the created array, it will create
      a string of asterisks depending on the frequency of each item within the file. IE, if the word 'Radish' appears in
      the test file 5 times, the second line of the file will read 'Radishes *****'.
      
      As the Groceries.cpp file said previously, this function was meant to write the 'frequency.dat file' in a way to be
      read from with another function to create the histogram. I instead created the histogram 1 line at a time and simply
      saved it to a file, then reading from the newly written file using the printHistogramFromFile() function.
'''
def displayHistogram():
    i = 0
    frequencyString = "" #instance variables
    frequency = []
    frequencyStrings = [""] * 30
    frequency = getItemFrequency()

    for element in frequency: #uses frequencyString variable to create a string of * based on item frequency
        frequencyString = ""
        if element > 0:
            for j in range(element):
                frequencyString += "*"
        frequencyStrings[i] = frequencyString
        i += 1
    
    file = open("frequency.dat", "w+") #open file

    file.write("Spinach " + frequencyStrings[0] + "\n") #print lines to file. Customized and not too flexible
    file.write("Radishes " + frequencyStrings[1] + "\n")
    file.write("Broccoli " + frequencyStrings[2] + "\n")
    file.write('Peas ' + frequencyStrings[3] + "\n")
    file.write('Cranberries ' + frequencyStrings[4] + "\n")
    file.write('Potatoes ' + frequencyStrings[5] + "\n")
    file.write('Cucumbers ' + frequencyStrings[6] + "\n")
    file.write('Peaches ' + frequencyStrings[7] + "\n")
    file.write('Zucchini ' + frequencyStrings[8] + "\n")
    file.write('Cantaloupe ' + frequencyStrings[9] + "\n")
    file.write('Beets ' + frequencyStrings[10] + "\n")
    file.write('Cauliflower ' + frequencyStrings[11] + "\n")
    file.write('Onions ' + frequencyStrings[12] + "\n")
    file.write('Yams ' + frequencyStrings[13] + "\n")
    file.write('Apples ' + frequencyStrings[14] + "\n")
    file.write('Celery ' + frequencyStrings[15] + "\n")
    file.write('Limes ' + frequencyStrings[16] + "\n")
    file.write('Garlic ' + frequencyStrings[17] + "\n")
    file.write('Pears ' + frequencyStrings[18] + "\n")

    file.close() #close file

'''Description:
      This function simply reads the 'frequency.dat' file and prints it to the console 1 line at a time. It is called
      after the histogram is created and saved to the file this function will read.
'''
def printHistogramFromFile():
    file = open("frequency.dat", "r")

    for line in file:
        print(line)

    file.close()