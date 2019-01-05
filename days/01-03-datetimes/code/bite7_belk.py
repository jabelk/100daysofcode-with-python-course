'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events

    In this bite we will look at this small server log finding the first and last Shutdown initiated events and
    calculate the time between the two events.

    In order to do this you need to extract the timestamps from the log entries and convert them to datetime objects.
    You can then use datetime.timedelta to calculate time differences between them. Check out the docstrings
    and the TESTS for more info.

    Good luck and have fun!

   '''

from datetime import datetime
import os
import urllib.request


#print(loglines)

# for you to code:


def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''

    time_from_log_line = line.split()[1]
    log_year = time_from_log_line.split("-")[0]
    log_month = time_from_log_line.split("-")[1]
    log_days = time_from_log_line.split("-")[2].split("T")[0]
    log_hours = time_from_log_line.split("-")[2].split("T")[1].split(":")[0]
    log_minutes = time_from_log_line.split("-")[2].split("T")[1].split(":")[1]
    log_seconds = time_from_log_line.split("-")[2].split("T")[1].split(":")[2]
    conv_date = datetime(year=int(log_year), month=int(log_month), day=int(log_days), hour=int(log_hours),
                         minute=int(log_minutes),
                         second=int(log_seconds))
    return conv_date


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    pass


if __name__ == "__main__":
    SHUTDOWN_EVENT = 'Shutdown initiated'

    # prep: read in the logfile
    logfile = os.path.join('/tmp', 'log')
    urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

    with open(logfile) as f:
        loglines = f.readlines()

    line = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file, resetting to empty.\n'

    print (convert_to_datetime(line))
