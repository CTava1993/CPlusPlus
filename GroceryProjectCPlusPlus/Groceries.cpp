#include <Python.h>
#include <iostream>
#include <Windows.h>
#include <cmath>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>

/* Christian Tavares, CS210 Programming Languages 22EW1, 10/15/2022
 *
 * This program will combine both C++ and Python in a VS2019 project in order to create a menu program that does 4 things:
 *
 * 1.) Read a file named 'GroceryList.txt' in order to then calculate the number of times each string appears and then print a table showing how many
 * of these 'items' were 'bought' from the company on the given day (represented by the text file it is read from)
 *
 * 2.) Calculate the number of items a specific item was bought from the store on this day. The item is defined through user input and will inherit
 * some functions used for the 1st feature.
 *
 * 3.) The menu program will inherit the same function that calculates the items and their frequencies and write a new file called 'frequency.dat'. 
 * Originally this function was supposed to read the frequency.dat file and create a histogram from it, but in my program I wrote it incorrectly by
 * printing the histogram itself to a file, instead of creating one from the newly written file. I'm sticking with the change regardless since it
 * more or less accomplishes the same task. It will print a table similarly to feature #1 but will have a number of asterisks next to each item that
 * represent the quantity of items purchased to the console, then write it to the frequency.dat file.
 *
 * 4.) Simply exit the program
 */

using namespace std;

/*Decription:
	Calling this function simply clears the text console.
*/
void clearScreen() {
	system("cls");
}

/*
Description:
	To call this function, simply pass the function name in Python that you wish to call.
Example:
	callProcedure("printsomething");
Output:
	Python will print on the screen: Hello from python!
Return:
	None
*/
void CallProcedure(string pName)
{
	char* procname = new char[pName.length() + 1];
	std::strcpy(procname, pName.c_str());

	Py_Initialize();
	PyObject* my_module = PyImport_ImportModule("PythonCode");
	PyErr_Print();
	PyObject* my_function = PyObject_GetAttrString(my_module, procname);
	PyObject* my_result = PyObject_CallObject(my_function, NULL);
	Py_Finalize();

	delete[] procname;
}

/*
Description:
	To call this function, pass the name of the Python functino you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("PrintMe","Test");
Output:
	Python will print on the screen:
		You sent me: Test
Return:
	100 is returned to the C++
*/
int callIntFunc(string proc, string param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	char* paramval = new char[param.length() + 1];
	std::strcpy(paramval, param.c_str());


	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	// Build the name object
	pName = PyUnicode_FromString((char*)"PythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(z)", paramval);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;
	delete[] paramval;


	return _PyLong_AsInt(presult);
}

/*
Description:
	To call this function, pass the name of the Python functino you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("doublevalue",5);
Return:
	25 is returned to the C++
*/
int callIntFunc(string proc, int param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	// Build the name object
	pName = PyUnicode_FromString((char*)"PythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(i)", param);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;

	return _PyLong_AsInt(presult);
}

/*Decription:
	Calling this function will print out the main menu of the program. 
	This is looped endlessly until the user prompts to exit the program.
*/
void printMenu() {
	cout << "======================================================" << endl;
	cout << "Choose which function to run:" << endl;
	cout << "1. Display list of items and # purchased" << endl;
	cout << "2. Show how many times a specific item was purchased" << endl;
	cout << "3. Display a text-based histogram of items purchased" << endl;
	cout << "4. Exit program" << endl;
	cout << "(Input your choice as a 1, 2, 3 or 4): "; //expected user inputs
}

/*Decription:
	This function will create a histogram from the provided 'GroceryList.txt' file.
	See displayHistogram() function in 'PythonCode.py' for more information.
*/
void displayHistogram() {
	try {
		CallProcedure("displayHistogram");
		CallProcedure("printHistogramFromFile");
		cout << "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n" << endl;
		cout << "The above histogram has been saved to and read from file:'frequency.dat'. . ." << endl;
		cout << "Type anything to continue . . .";
	}
	catch (exception e) {
		cout << "ERROR: Could not write 'frequency.dat' file. . ."; //error catch in case of file reading issues
	}
}

/*Decription:
	This function will show the specific frequency of an item that is defined by the user's input.
	See displaySpecificItemFrequency() function in 'PythonCode.py' for more information.
*/
void displaySpecificItem() {
	string item;
	cout << "Which item will you search for?: ";
	cin >> item; //inputs
	callIntFunc("displaySpecificItemFrequency", item); //call python function with user input
	cin >> item;
}

/*Decription:
	This function is an endless loop that will clear the screen and print the main menu until prompted otherwise.
	It's a simply if-statement tree that asks for user input of a number from 1-4. Else statement, just in case.
*/
void initialize() {
	string input;

	while (0 == 0) {
		clearScreen();
		CallProcedure("printSomething"); //just a flavor text line on top to make python feel at home :)
		printMenu();

		cin >> input; //user input

		if (input == "1") { //display items and frequency
			clearScreen();
			CallProcedure("displayItemsAndFrequency");
			cin >> input;
		}
		else if (input == "2") { // display specific item frequency
			clearScreen();
			displaySpecificItem();
		}
		else if (input == "3") { //histogram
			clearScreen();
			displayHistogram();
			cin >> input;
		}
		else if (input == "4") { //close program
			break;
		}
		else {
			clearScreen();
			cout << "INVALID INPUT" << endl;
			//do nothing
		}
	}
}

/*Decription:
	The main function where the program starts. Simply calls the initialize() function.
*/
int main()
{
	initialize();
}