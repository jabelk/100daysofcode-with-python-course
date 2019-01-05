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

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()
print(loglines)



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
    loglines = ['INFO 2014-07-03T23:27:51 supybot Shutdown initiated.\n', 'INFO 2014-07-03T23:27:51 supybot Killing Driver objects.\n', 'INFO 2014-07-03T23:27:51 supybot Killing Irc objects.\n', 'INFO 2014-07-03T23:27:51 supybot Shutdown complete.\n', 'INFO 2014-07-03T23:30:37 supybot Creating new Irc for freenode.\n', 'INFO 2014-07-03T23:30:37 supybot Connecting to irc.freenode.net:8001.\n', 'INFO 2014-07-03T23:30:38 supybot Loading plugins (connecting to freenode).\n', 'INFO 2014-07-03T23:30:46 supybot Server orwell.freenode.net has version ircd-seven-1.1.3\n', 'INFO 2014-07-03T23:30:48 supybot Got end of MOTD from orwell.freenode.net\n', 'INFO 2014-07-03T23:30:54 supybot Join to #timvideos on freenode synced in 2.41 seconds.\n', "INFO 2014-07-03T23:31:22 supybot Exiting due to Ctrl-C.  If the bot doesn't exit within a few seconds, feel free to press Ctrl-C again to make it exit without flushing its message queues.\n", 'INFO 2014-07-03T23:31:22 supybot Flushers flushed and garbage collected.\n', 'INFO 2014-07-03T23:31:22 supybot Driver for Irc object for freenode dying.\n', 'INFO 2014-07-03T23:31:22 supybot Irc object for freenode dying.\n', 'INFO 2014-07-03T23:31:22 supybot Driver for Irc object for freenode dying.\n', 'WARNING 2014-07-03T23:31:22 supybot Disconnect from irc.freenode.net:8001: error: [Errno 9] Bad file descriptor.\n', 'INFO 2014-07-03T23:31:22 supybot Reconnecting to freenode at 2014-07-03T23:31:32.\n', 'INFO 2014-07-03T23:31:22 supybot Removing driver SocketDriver(Irc object for freenode).\n', 'INFO 2014-07-03T23:31:22 supybot Total uptime: 45 seconds.\n', 'INFO 2014-07-03T23:31:22 supybot Total CPU time taken: 1.12 seconds.\n', 'INFO 2014-07-03T23:31:22 supybot No more Irc objects, exiting.\n', 'INFO 2014-07-03T23:31:22 supybot Shutdown initiated.\n', 'INFO 2014-07-03T23:31:22 supybot Killing Driver objects.\n', 'INFO 2014-07-03T23:31:22 supybot Killing Irc objects.\n', 'INFO 2014-07-03T23:31:22 supybot Writing registry file to planet-news.conf\n', 'INFO 2014-07-03T23:31:22 supybot Finished writing registry file.\n', 'INFO 2014-07-03T23:31:22 supybot Shutdown complete.\n']

    shut_events = []
    for line in loglines:
        if "Shutdown initiated." in line:
            shut_events.append([line, convert_to_datetime(line)])

    if shut_events:
        print(shut_events[0][1], shut_events[-1][1])
        first_last_delta =  shut_events[-1][1] - shut_events[0][1]
        return first_last_delta

    return shut_events


if __name__ == "__main__":
    SHUTDOWN_EVENT = 'Shutdown initiated'

    # prep: read in the logfile
    logfile = os.path.join('/tmp', 'log')
    urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

    with open(logfile) as f:
        loglines = f.readlines()
    print(loglines)
    line = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file, resetting to empty.\n'

    print(convert_to_datetime(line))
    print(time_between_shutdowns(loglines))
