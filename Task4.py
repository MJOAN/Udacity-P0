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
    if phone.startswith('(0'):
        return 'fixed_line'
    elif phone.startswith('140'):
        return 'telemarketer'
    else:
        return 'mobile_number'

telemarketers_only = []
not_telemarketers = []
potential = [] 

def potential_telemarketers(calls, texts): 

    for call in calls:
        if get_phone_type(call[0]) == 'telemarketer' and get_phone_type(call[1]) != 'telemarketer':
            telemarketers_only.append(call[0])    
    
    for text in texts:
        if text[0] or text[1] not in telemarketers_only:
            not_telemarketers.extend([text[0], text[1]])
    
    potential.append(set(telemarketers_only).intersection(set(not_telemarketers)))

print("These numbers could be telemarketers: \n")
print('\n'.join(set(potential if len(potential) > 0 else telemarketers_only)))

potential_telemarketers(calls, texts)