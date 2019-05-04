"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def unique_phone_count(calls):
    result = set()
    for call in calls:
        if call[0] not in result:
            result.add(call[0])
        else: 
            result.add(call[1])
    count = len(result)
    return count

unique_phone_count(calls) # 544
count = unique_phone_count(calls) 
print('There are', count, 'different telephone numbers in the records.')
# There are 544 different telephone numbers in the records.