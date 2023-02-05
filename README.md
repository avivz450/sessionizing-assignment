# Sessionizing assignment

### Solution description

### How to run the program?
+ clone this repository to your local machine.
+ If the packages `pandas` and `mrjob` are not installed, please install them.
+ Run the project by running `python .\index.py`, as `index.py` is the starting point.
  After running that command, the program will create the sessions automatically from the input files (which are in the `data` folder).
  After finishing creating, you can pass your query request to the program through the command line.

### Changes required for large scale input
+ seperate mapper and reducer in other instances
+ fetch sessions from external db
+ use cache to reduce number of external calls to the db

### Complexity
+ defined in the program in notes