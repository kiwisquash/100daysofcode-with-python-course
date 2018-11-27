'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''

from datetime import datetime
import os
# import urllib.request # Not necessary for the local version 

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('tmp', 'log')
# urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile) # Not necessary for the local version

with open(logfile) as f:
    loglines = f.readlines()

# Quick test to see if the log file is being read properly. Comment it out for the webversion
# for line in loglines:
#     print(line)

# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    blankIndex1 = line.find(" ")
    if blankIndex1 !=-1:
        blankIndex2 = line[blankIndex1 + 1:].find(" ") + blankIndex1 + 1
        timeString = line[blankIndex1 + 1:blankIndex2]
        return datetime.strptime(timeString,"%Y-%m-%dT%H:%M:%S")
    # print(timeString) 

# Quick test to see if the times are being extracted correctly
# for line in loglines:
#     print(convert_to_datetime(line))


def first_shutdown(loglines):
    for line in loglines:
        if "Shutdown initiated" in line:
            return line

def last_shutdown(loglines):
    for line in loglines[::-1]:
        if "Shutdown initiated" in line:
            return line

# Quick test to see if the first_shutdown and last_shutdown are working
# print(first_shutdown(loglines))
# print(last_shutdown(loglines))

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    first = convert_to_datetime(first_shutdown(loglines))
    last = convert_to_datetime(last_shutdown(loglines))
    return last - first

print(time_between_shutdowns(loglines))
print(type(time_between_shutdowns(loglines)))
