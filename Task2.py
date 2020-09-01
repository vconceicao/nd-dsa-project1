"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def check_max_value(phone_dict):
    max_duration=0
    phone_number = ''

    for key in phone_dict:
        if max_duration < phone_dict[key]:
            max_duration = phone_dict[key]
            phone_number = key
    return key, max_duration

phone_dict = {}
for key in calls:
    phone_dict[key[0]] = 0

for key in calls:
    phone_dict[key[0]] = phone_dict[key[0]] + int(key[3])

phone_number, max_duration = check_max_value(phone_dict)



print(phone_number+" spent the longest time, " +str(max_duration) +" seconds, on the phone during September 2016.")
