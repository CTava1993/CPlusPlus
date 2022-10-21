# CPlusPlus
A repository of code projects for my C++ course


~ Summarize the project and what problem it was solving.

This project was designed to combine C++ and Python code in a Visual Studio 2019 project in order to emulate a grocery tracking program. The GroceryList file provided has lines of words that the program will recieve as items that were "sold" by the store during the day. The program is a menu that performs several functions based on user input, starting with this GroceryList file. The C++ side of the program will handle menu navigation while Python will handle most of the mathematics and calculations.
 
 
~ What did you do particularly well?
 
One thing I think I did well on this project was general organization. I'm sure there are more efficient ways to arrive at the end result, but I feel that this project was fairly neat outside of the fact that it doesn't utilize classes.
 
 
~ Where could you enhance your code? How would these improvements make your code more efficient, secure, and so on?
 
If there is one place that I could definitely improve on with this code, it would be to make it more adjustable in case there was ever a time that I or someone else would like to tweak the GroceryList file. At the moment, if you add any word to the GroceryList file that isn't defined by the getItemID function then the item is just discounted. This could have been written to work with any string to create an instance of an item if it were more intuitive.
 
 
~ Which pieces of the code did you find most challenging to write, and how did you overcome this? What tools or resources are you adding to your support network?
 
Ironically, the hardest thing for me to write with this code was just getting it to create a table of items that were bought. The compiler likes to have an aneurysm when the Python code can't be compiled, which will often give an error that is misleading. I spent a long time trying to debug simple print commands to use string objects because the Python interpreter detected syntax errors.


~ What skills from this project will be particularly transferable to other projects or course work?

I think one of the skills I find to be very transferable is how this project combines 2 languages into one Visual Studio solution. Understanding how to work with the IDE to incorporate another language will prove to be handy, I'm sure.
 
 
~ How did you make this program maintainable, readable, and adaptable?
 
I made the program with the constant thought of what would happen if the user decided to tweak something in the input file. I wanted to make it easy to add more objects into the file that wouldn't be defined by the program by default. To make it readable, I just tried to keep things as neat as possible while adding appropriate comments.
