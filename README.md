# Sessionizing assignment

## Solution description
I created a service that runs in the following order:
+ Processes the data in the data folder, where the .csv input files are located, to create one .csv session file (corresponding to the input files).
+ Reveals a user interface that allows him to enter several queries through the command line

### What the sessions file will have?
The sessions file will have all the sessions corresponding to the input files, and each line will have the following fields:
+ session_length - length of the session
+ site_url - the main URL of the visited site
+ visitor_id - unique identifier of the visitor on that site

for example:
```
...
1706,www.s_3.com,visitor_2632
2163,www.s_2.com,visitor_5388
518,www.s_2.com,visitor_5388
...
```

### How the data process is made?
The processing works by using the "Map Reduce" method twice:
1. For each input_i.csv file, an ouput_i.csv file is generated - which contains the sessions for that file. more details about this stage are in `sessions-creator.py`
2. After creating the session files, we use another "Map Reduce" method to combine them into one session file. more details about this stage are in `sessions-merger.py`

## How to run the program?
+ Clone this repository to your local machine.
+ Install the requirements - `pandas` v1.5.3 and `mrjob` v0.6.12
+ Run the project by running `python .\index.py`  from the project's directory, as `index.py` is the starting point.
  After running that command, the program will create the sessions automatically from the input files (which are in the `data` folder).
  After finishing creating, you can pass your query request to the program through the command line.
+ The query request can be one of : `num_sessions`, `median_session_length` or `num_unique_visited_sites`.

## Changes required for large scale input (need to update)
+ Separate the "sessions API" and the sessions data process
+ Separate the mapper and reducer methods into some instances, according to the input size.
  Each mapper will handle (at most) the number of inputs that are known in advance.
  Each reducer will handle certain keys.
  If needed, assign more instances for the relevant method.
+ Fetch sessions from external DB (instead of from in-memory)
+ Use cache in the API service to reduce the number of external calls to the DB once requesting a query

## Complexity
+ written in the code

## Testing the code
I have made unit and integration tests for the logical parts of this service.
+ Unit tests - tested each method separately in each logical part
+ Integration tests - tested each functionality of the service
