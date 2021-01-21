#!/usr/bin/env python3
import pandas as pd
import numpy as np
import time
import os
import glob


def cleaner():
    """ delete files in uploads folder
    """
    fileList = glob.glob('uploads/*.csv')
    # Iterate over the list of filepaths & remove each file.
    for filePath in fileList:
        try:
            os.remove(filePath)
        except OSError:
            print("Error while deleting file")


def appointment(slot_data, num_cols):
    """ fill the schedule columns for a specific slot in a day
        @slot_data: pandas dataframe
                    portion of the original dataframe that contains
                    only one slot(AM or PM) for a day.
    """
    s = slot_data.shape  # dataframe dimensions
    companies = []  # it stores assigned companies
    # fill with assigned companies
    for i in range(0, s[0]):
        for j in range(3, num_cols):
            val = slot_data.iloc[i][j]  # company name
            if val not in companies and type(val) == str:
                companies.append(val)

    # fill empty columns (hours) with companies
    for c in companies:
        for i in range(s[0]):
            # verify if the mentor has been assigned a meeting time previously
            row_hours = slot_data.iloc[i, num_cols:num_cols+20].values.tolist()
            if c in row_hours:
                row_empty = False
            else:
                row_empty = True  # no assigned previously
            last = slot_data.iloc[i, -1]
            if type(last) == str and c in last.split():
                last_empty = False
            else:
                last_empty = True  # no assigned previously
            comp_mentor = slot_data.iloc[i, 3:num_cols].values.tolist()
            if c in comp_mentor and row_empty and last_empty:
                # define window to work - AM or PM
                if slot_data.iloc[i][2] == 'AM':
                    j = num_cols
                    limit = num_cols + 10
                else:
                    j = num_cols + 10
                    limit = num_cols + 20
                space = slot_data.iloc[i, j]
                check_list = slot_data.iloc[:i, j].values.tolist()
                # searh for another position if there are conflicts
                while (type(space) == str or c in check_list) and j < limit:
                    j += 1
                    space = slot_data.iloc[i, j]
                    check_list = slot_data.iloc[:i, j].values.tolist()
                if j < limit:
                    slot_data.iloc[i, j] = c  # assign hour to a company
                else:
                    if type(slot_data.iloc[i, num_cols + 20]) == str:
                        # add to unavailable spot
                        slot_data.iloc[i, num_cols + 20] += " " + c
                    else:
                        # put in unavailable spot
                        slot_data.iloc[i, num_cols + 20] = c

    return slot_data


def create_schedule(filename):
    """
        creates a schedule for meetings based on a csv file

        filename: csv file where evey row has:
                            - The name of the mentor
                            - The day they reserved
                            (Monday, Tuesday, Wednesday, Thursday, or Friday)
                            - The time slot (AM, PM)
                            - The companies manually assigned to each mentor
        Output: It is a new csv file where new columns were added.
                Every column is a hour in the calendar, the spots in the
                calendar contains the company assinged.

    """
    # read csv file
    data = pd.read_csv('./uploads/' + filename)  # new pandas dataframe

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    slots = ['AM', 'PM']

    am_hours = ['8:00 a.m.', '8:20 a.m.', '8:40 a.m.', '9:00 a.m.',
                '9:20 a.m.', '9:40 a.m.', '10:00 a.m.', '10:20 a.m.',
                '10:40 a.m.', '11:00 a.m.']
    pm_hours = ['2:00 p.m.', '2:20 p.m.', '2:40 p.m.', '3:00 p.m.',
                '3:20 p.m.', '3:40 p.m.', '4:00 p.m.', '4:20 p.m.',
                '4:40 p.m.', '5:00 p.m.']

    data['Day'] = data['Day'].str.strip()  # clean extra spaces
    data['AM/PM'] = data['AM/PM'].str.strip()  # clean extra spaces
    num_cols = len(list(data.columns))
    if num_cols < 24:
        # add new columns for every 20min
        for col in am_hours:
            data[col] = np.nan
        for col in pm_hours:
            data[col] = np.nan
        data['unavailable spot'] = np.nan  # new column for unavailable spot
    else:
        num_cols = 0
        for c in list(data.columns):
            if c not in am_hours + pm_hours and c != 'unavailable spot':
                num_cols += 1

    slot_undefined = data[(data['Day'] == 'Undefined') &
                          (data['AM/PM'] == 'Undefined')]
    list_data = []  # store dataframes for every slot
    for day in days:
        for slot in slots:
            # slice dataframe in a specific slot
            slot_data = data[(data['Day'] == day) & (data['AM/PM'] == slot)]
            # generate appointments for one slot
            sorted_slot_data = appointment(slot_data, num_cols)
            # add modified dataframe slot
            list_data.append(sorted_slot_data)
    list_data.append(slot_undefined)
    # unify dataframes
    data_concat = pd.concat(list_data)
    t = time.time()
    cleaner()  # clean upload folder
    # store dataframe as csv file
    data_concat.to_csv('./uploads/schedule_from_list_{}.csv'.format(t),
                       index=False)
    return t
