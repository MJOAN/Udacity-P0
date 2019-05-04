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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def get_phone_type(phone):
    if phone.startswith('(080)'):
        return 'bangalore'
    elif phone.startswith('140'):
        return 'telemarketer'
    elif phone.startswith('(0'):
        return 'fixed_lines'
    else:
        return 'mobile_number'

def potential_telemarketers(calls, texts): 
    telemarketers_only = set()
    
    for call in calls:
        caller, receiver = call[0], call[1]
        caller_type = get_phone_type(caller)
        
        if caller != receiver:
            telemarketers_only.add(caller)
    
    for text in texts:
        sender, receiver = text[0], text[1]
        if sender and receiver not in telemarketers_only:
            result = sorted(telemarketers_only)
            
    print("These numbers could be telemarketers: \n")
    print('\n'.join(result))
    
potential_telemarketers(calls, texts)