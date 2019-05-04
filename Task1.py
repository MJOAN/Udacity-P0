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
    combined = set()
    for a,b in zip(calls, texts):
        group = [a[0], a[1], b[0], b[1]]
        for item in group: 
            combined.add(item)

    return len(combined)

unique_phone_count(calls) # 570
count = unique_phone_count(calls) 
print('There are', count, 'different telephone numbers in the records.')
# There are 570 different telephone numbers in the records.