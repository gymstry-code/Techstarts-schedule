#!/usr/bin/env python3
import pandas as pd
import numpy as np


def appointment2(slot_data):
    # companies = slot_data.iloc[:, 3:10].values.tolist()
    # print(companies)
    s = slot_data.shape
    # print(s)
    # print(slot_data.head())
    companies = []
    for i in range(0, s[0]):
        for j in range(3, 10):
            val = slot_data.iloc[i][j]
            # print(val)
            # print(slot_data.iloc[i, 0])
            if not val in companies and type(val) == str:
                companies.append(val)
    print(companies)
    for c in companies:
        for i in range(s[0]):
            if c in slot_data.iloc[i, 3:10].values.tolist():
                if slot_data.iloc[i][2] == 'AM':
                    j = 10
                else:
                    j = 20
                space = slot_data.iloc[i, j]
                print("space: ", space)
                check_list = slot_data.iloc[:i, j].values.tolist()
                while type(space) == str or c in check_list:
                    j += 1
                    space = slot_data.iloc[i, j]
                    check_list = slot_data.iloc[:i, j].values.tolist()
                print("value: ", c, "position i: ", i, "position j: ", j, "current value: ", slot_data.iloc[i, j])
                # print(check_list)
                slot_data.iloc[i, j] = c
                print(slot_data.iloc[:,20:30])


    return slot_data



pd.set_option('display.max_columns', None)
data = pd.read_csv('./data/Techstars Challenge - Source Data.csv')
s = data.shape
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
slots = ['AM', 'PM']
am_hours = ['8:00 a.m.', '8:20 a.m.', '8:40 a.m.', '9:00 a.m.', '9:20 a.m.', '9:40 a.m.', '10:00 a.m.', '10:20 a.m.', '10:40 a.m.', '11:00 a.m.']
pm_hours = ['2:00 p.m.', '2:20 p.m.', '2:40 p.m.', '3:00 p.m.', '3:20 p.m.', '3:40 p.m.', '4:00 p.m.', '4:20 p.m.', '4:40 p.m.', '5:00 p.m.']

for col in am_hours:
    data[col] = np.nan
for col in pm_hours:
    data[col] = np.nan

m = data.shape
# day = data.iloc[0][1]
# slot = data.iloc[0][2]
# print(day, slot)
list_data = []
for day in days:
    for slot in slots:
        print(day)
        print(slot)
        # j = i
        # while data.iloc[i][1] == day and data.iloc[i][2] == slot:
        slot_data = data[(data['Day'] == day) & (data['AM/PM'] == slot)]
        # print(slot_data.head())
        sorted_slot_data = appointment2(slot_data)
        print(sorted_slot_data)
        # sorted_slot_data.to_csv('schedule_{}_{}.csv'.format(day, slot), index=False)
        list_data.append(sorted_slot_data)
data_concat = pd.concat(list_data)
data_concat.to_csv('./data/schedule_from_list.csv', index=False)
