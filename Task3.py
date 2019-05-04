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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_phone_type(phone):
    if phone.startswith('(0'):
        return 'fixed_line'
    elif phone.startswith('140'):
        return 'telemarketer'
    else:
        return 'mobile_number'

list_of_codes = []
for call in calls:
    caller, receiver = call[0], call[1]
    caller_type = get_phone_type(caller)
    receiver_type = get_phone_type(receiver)
    
    if receiver_type == 'fixed_line':
        codes = receiver.split('(', 1)[1].split(')')[0]
        list_of_codes.append(codes)
                
print("The numbers called by people in Bangalore have codes:\n")
print('\n'.join(sorted(set(list_of_codes))))

def fixed_percentage(calls):
    from_fixed = []
    from_fixed_to_fixed = []

    for call in calls:
        caller, receiver = call[0], call[1]
        caller_type = get_phone_type(caller)
        receiver_type = get_phone_type(receiver)

        if receiver_type == 'fixed_line':
            from_fixed.append(receiver)
            # print(len(from_fixed))

        if caller_type == 'fixed_line' and receiver_type == 'fixed_line': 
            from_fixed_to_fixed.append(receiver)
            # print(len(from_fixed_to_fixed))
    
    answer = len(from_fixed_to_fixed) / len(from_fixed) 
    percent = round(answer, 2)
    print(round(percent,2), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.\n")

fixed_percentage(calls)