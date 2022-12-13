# Damn-Bugs
**Simple (very simple) python script for ganarating a report of found bugs in a collection of files based of predefined comment structure.**

**The script is so far designed for c/c++ comments**
**The comment form for bug annotation taht the user follows is strict.**
* on-line
* in /* */
* begins with [!]  (this signals that this is a bug and not a different type of anotation)
* second [<>] defines the users that created this comment (can be initials).
* after that a desciption of the bug myst be added.

**Sample code.**
```
#include <stdio.h>
int main(int argc, char* argv[])
{
	int i =0;
  
  /*[!][tt] the iteration should end at 11 */
	for(i=0; i< 10; i++)
	{
		printf("Hello\n"); /*[!][tt] No "world" is inclulded */
	}
  
	return(0);
}
```

**The script  openc a directory selection dialog window where you choose the 
project directory with all the .c/.cpp/.h file**

**After that all files are scanned and a bugs.csv file is ganarated in the same directory. The csv file includes the file-name,line,owner,description for all detected bugs.**
