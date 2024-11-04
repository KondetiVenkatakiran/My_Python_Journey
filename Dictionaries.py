# 1. Basic Dictionary Operations
# Create a dictionary that stores information about a person (e.g., name, age, city). Then:
#
# 	•	Retrieve the person’s age.
# 	•	Update the city.
# 	•	Add a new key-value pair for the person’s job.
from fontTools.merge.tables import merge

customer = {
    'name': 'kiran','age': 22,'is_verified':True
}
customer['name'] = 'venkata kiran'
customer['DOB'] = '12-13-2001'

print(customer)
print(customer['name'])
print(customer['age'])
print(customer['DOB'])
print(customer.get('is_verified'))

phone = input("Phone: ")
digits_mapping = {
    '1':'one',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine'
}
output = " "
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


# 2. Counting Occurrences
# Given a list of words, count how many times each word appears using a dictionary.
words = ["kiran","tarun","varun","hari","kiran","tarun"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
# Merge two dictionaries, dict1 and dict2. If both have the same key, the value from dict2 should overwrite dict1’s value.
# 3. Merging Dictionaries
#
# Problem
#
# Merge two dictionaries, dict1 and dict2. If both have the same key, the value from dict2 should overwrite dict1’s value.

dict1 = {"name":'kiran',"age":22}
dict2 = {"name":"tarun","age":20}
#meging dictionaries
merged_dict = {**dict1,**dict2} # Python 3.5+
# print(dict1.update(dict2))
print(merged_dict)
# 4. Filtering a Dictionary
#
# Problem
#
# Filter a dictionary to include only keys that have values greater than a certain threshold.

grades = {"Kiran":79,"tarun":78,"varun":68,"david":75}
#  filtering dictionary based on value
passing_grades = {k: v for k, v in grades.items() if v >= 70}
print(passing_grades)
