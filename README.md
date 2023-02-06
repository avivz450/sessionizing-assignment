# Sessionizing assignment

## Solution description (need to update)
I created a service that works in the following order:
+ Processes the data in the data folder, where the input files are located, to create one session file (corresponding to the input files).
+ Reveals a user interface that allows him to enter several queries through the command line

### What the sessions file will have?
The sessions file will have all the sessions corresponding to the input files, and each line will have the following fields:
+ session_length - length of the session
+ site_url - the main URL of the visited site
+ visitor_id - unique identifier of the visitor on that site

### How the data process is made?
The processing works by using the "MapReduce" method twice:
1. For each input_i.csv file, an ouput_i.csv file is generated, which contains the sessions for that file.
2. After creating the session files, we use this method again to combine them into one session file.

## How to run the program?
+ Clone this repository to your local machine.
+ If the packages `pandas` and `mrjob` are not installed, please install them.
+ Run the project by running `python .\index.py`  from the project's directory, as `index.py` is the starting point.
  After running that command, the program will create the sessions automatically from the input files (which are in the `data` folder).
  After finishing creating, you can pass your query request to the program through the command line.
+ The query request can be one of : `num_sessions`, `median_session_length` or `num_unique_visited_sites`.

## Changes required for large scale input (need to update)
+ separate mapper and reducer in other instances
+ fetch sessions from external DB
+ use cache to reduce the number of external calls to the DB

## Complexity (need to check)
+ written in the code

## Testing the code
I have made unit and integration tests for the logical parts of this service.
+ Unit tests - tested each method separately in each logical part
+ Integration tests - tested each functionality of the service
