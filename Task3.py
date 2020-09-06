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

def get_number_of_calls_of_bangalore(calls):
  number_of_calls_from_bangalore = 0
  number_of_calls_inside_bangalore_area = 0
  
  for record in calls:
    if record[0].startswith("(080)"): 
      number_of_calls_from_bangalore+=1
    if record[0].startswith("(080)") and record[1].startswith("(080)"):
      number_of_calls_inside_bangalore_area+=1
  return number_of_calls_from_bangalore, number_of_calls_inside_bangalore_area   


def calculate_calls_percentage(count1, count2):
  percentage = (count2/count1)*100
  return percentage

def get_code(phone_number):
  index_s_bracket = phone_number.index("(")+1
  index_e_bracket = phone_number.index(")")

  return phone_number[index_s_bracket: index_e_bracket]

def get_mobile_prefix(phone_number):
  return phone_number[0:4]

def get_list_of_codes_called_by_bangalore(calls):
  phone_dict={}
  for key in calls:
    if key[0].startswith("(080)"):
      if key[1].startswith("(0"):
        phone_dict[get_code(key[1])]=0
      if key[1].startswith("7") or key[1].startswith("8") or key[1].startswith("9"):
        phone_dict[get_mobile_prefix(key[1])]=0
  return phone_dict


def part_a(calls):
  list_of_codes = get_list_of_codes_called_by_bangalore(calls)
  print("The numbers called by people in Bangalore have codes:")
  for code in sorted(list_of_codes):
    print(code)

def part_b(calls):
  number_of_calls_from_bangalore, number_of_calls_inside_bangalore_area =  get_number_of_calls_of_bangalore(calls)

  percentage = calculate_calls_percentage(number_of_calls_from_bangalore, number_of_calls_inside_bangalore_area)

  print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


def show_data_about_bangalore(calls):

  part_a(calls)  
  
  part_b(calls)
 
show_data_about_bangalore(calls)