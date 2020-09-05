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

def get_first_record(list):
    return list[0];

def get_last_record(list):
    return list[len(list)-1];

text_first_record =  get_first_record(texts);

text_incoming_number = text_first_record[0];
text_answering_number = text_first_record[1];
text_time = text_first_record[2];

call_last_record = get_last_record(calls);

call_incoming_number = call_last_record[0];
call_answering_number = call_last_record[1];
call_time = call_last_record[2];
call_seconds = call_last_record[3];

print("First record of texts, {incoming_number} texts {answering_number} at time {time}"
      .format(incoming_number=text_incoming_number, answering_number=text_answering_number, time=text_time))
print("Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {during} seconds"
      .format(incoming_number=call_incoming_number, answering_number=call_answering_number, time=call_time, during=call_seconds))
