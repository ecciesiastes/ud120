#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
import pickle

sys.path.append("../tools/")
### Load the dictionary containing the dataset
with open("../final_project/final_project_dataset.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

num_poi_n = 0
num_salary = 0
num_email = 0

num_total = 0
num_nan_payments = 0
num_nan_poi_payments = 0

for data in my_dataset:
    num_total += 1
    if str(data).find('Lay'.upper()) >= 0:
        lay = my_dataset[data]['total_payments']
    if str(data).find('Skilling'.upper()) >= 0:
        skilling = my_dataset[data]['total_payments']
    if str(data).find('Fastow'.upper()) >= 0:
        fastow = my_dataset[data]['total_payments']
    if my_dataset[data]["poi"] == True:
        num_poi_n += 1
    if my_dataset[data]["salary"] != 'NaN':
        num_salary += 1
    if my_dataset[data]["email_address"] != 'NaN':
        num_email += 1
    if my_dataset[data]["total_payments"] == 'NaN':
        num_nan_payments += 1
    if (my_dataset[data]["total_payments"] == 'NaN') & my_dataset[data]["poi"] == True:
        num_nan_poi_payments += 1

print('lay has %s.' % (lay))
print('skilling has %s.' % (skilling))
print('fastow has %s.' % (fastow))

print(max(lay, skilling, fastow))
print(num_poi_n)

print(num_salary)
print(num_email)

print('num_nan_payments has %s.' % (num_nan_payments))
print('num_total has %s.' % (num_total))
print(num_nan_payments / num_total)

print(num_nan_poi_payments / num_poi_n)
