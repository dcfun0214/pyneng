# -*- coding: utf-8 -*-
"""
Task 17.4

Create function write_last_log_to_csv.

Function arguments:
* source_log - the name of the csv file from which the data is read (mail_log.csv)
* output - the name of the csv file into which the result will be written

The function returns None.

The write_last_log_to_csv function processes the csv file mail_log.csv.
The mail_log.csv file contains the logs of the username change.
User cannot change email, only username.

The write_last_log_to_csv function should select from the mail_log.csv file
only the most recent entries for each user and write them to another csv file.
In the output file, the first line should be the column headers as in the source_log file.

For some users, there is only one record, and then it is necessary to write
to the final file only her. For some users, there are multiple entries with
different names. For example, a user with email c3po@gmail.com changed his
username several times:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Of these three records, only one should be written to the final file - the most recent:
C-3PO,c3po@gmail.com,16/12/2019 17:24


It is convenient to use datetime objects from the datetime module
for comparing dates. To make it easier to work with dates,
the convert_str_to_datetime function has been created - it converts a date
string in the format 11/10/2019 14:05 into a datetime object.
The resulting datetime objects can be compared with each other.
The second function, convert_datetime_to_str, does the opposite — it turns
a datetime object into a string.

It is not necessary to use the functions convert_str_to_datetime and convert_datetime_to_str

"""

import datetime
import csv

def convert_str_to_datetime(datetime_str):
    """
    Converts a date string formatted as 11/10/2019 14:05 to a datetime object.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Converts a datetime object to a date string in the format 11/10/2019 14:05.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, output):
    result = {}
    mails = set()
    result_final = []
    with open(source_log) as f:
        reader = csv.reader(f)
        a = list(reader)
        for i in a[1:]:
            mails.add(i[1])
            i[2] = convert_str_to_datetime(i[2])
        for i in mails:
            result[i] = []
        for i in result.keys():
            for b in a:
                if i == b[1]:
                    result[i].append(b[2])
        for x, y in result.items():
            result[x] = convert_datetime_to_str(max(y))
        for i in a[1:]:
            i[2] = convert_datetime_to_str(i[2])
        result_final.append(a[0])
        for x, y in result.items():
            result_final_sub = []
            for i in a:
                if x in i and y in i:
                    result_final_sub = [i[0], x, y]
                    result_final.append(result_final_sub)
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in result_final:
            writer.writerow(row)
