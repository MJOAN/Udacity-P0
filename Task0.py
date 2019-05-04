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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_record_texts = texts[0]
print(first_record_texts)

last_record_calls = calls[len(calls)-1]
print(last_record_calls)

# ['97424 22395', '90365 06212', '01-09-2016 06:03:22']
# ['98447 62998', '(080)46304537', '30-09-2016 23:57:15', '2151']

text_incoming_number = first_record_texts[0]
text_answering_number = first_record_texts[1]
text_time = first_record_texts[2][11:20]

print('First record of texts,', text_incoming_number ,'texts,',  text_answering_number, 'at time', text_time)
# First record of texts, 97424 22395 texts, 90365 06212 at time 06:03:22

call_incoming_number = last_record_calls[0]
call_answering_number = last_record_calls[1]

area_code = call_answering_number[:5]
prefix_phone = call_answering_number[5:8]
suffix_phone = call_answering_number[8:15]
call_answering_number = area_code + ' ' + prefix_phone + suffix_phone

call_during = last_record_calls[2][17:20]
call_time = last_record_calls[2][11:16]

print('Last record of calls,', call_incoming_number, 'calls,', call_answering_number, 'at time', call_time, 'lasting', call_during, 'seconds')
# Last record of calls, 98447 62998 calls, (080) 46304537 at time 23:57 lasting 15 seconds
