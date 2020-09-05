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

def remove_false_telemarketers(possible_telemarketers, non_telemarketers):
    return possible_telemarketers.difference(non_telemarketers)

possible_telemarketers =set()
non_telemarketers = set()

for phone in calls:
    possible_telemarketers.add(phone[0])
    non_telemarketers.add(phone[1])

for phone in texts:
    non_telemarketers.add(phone[0])
    non_telemarketers.add(phone[1])

validated_telemarketers = remove_false_telemarketers(possible_telemarketers, non_telemarketers)

print("These numbers could be telemarketers: ")
for phone in sorted(validated_telemarketers):
    print(phone)