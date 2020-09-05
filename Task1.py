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

def get_different_phone_numbers(list):
    diff_list = set()
    first_column = 0
    second_column = 1
    for phone in list:
        diff_list.add(phone[first_column])
        diff_list.add(phone[second_column])
    return diff_list

merged_list = texts + calls
diff_list = get_different_phone_numbers(merged_list)
diff_phone_numbers_count = len(diff_list)
print("There are {count} different telephone numbers in the records.".format(count=diff_phone_numbers_count))



