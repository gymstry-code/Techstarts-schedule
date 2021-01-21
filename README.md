# Techdule - Schedule Generator

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Techdule is a tool that helps the Program Associate and the Program Manager to  assign a specific time slot for each startup with their assigned mentors, in such a way that a mentor is not booked with two companies at the same time, nor a startup booked with more than one mentor at the same time.


# How to use it!

  - Go to the demo app: https://techstars-schedule.herokuapp.com/
  ![index_image](https://github.com/HeimerR/Techstarts-schedule/blob/main/0.png)
  - Drag and drop the csv file
  - Download de new csv file that contains the schedule
  ![index_image](https://github.com/HeimerR/Techstarts-schedule/blob/main/1.png)


### Tech

Techdule uses a number of open source projects to work properly:

* [Python](https://www.python.org/) - Programming language
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python micro web framework
* [Pandas](https://pandas.pydata.org/) - Python library for manipulating dataframes/tables/series
* [NumPy](https://numpy.org/) - Python library for manipulating  multi-dimensional arrays and matrices
* [codepen.io](https://codepen.io/TheLukasWeb/pen/qlGDa) - front end resourses


### How it works

The input csv file must have the following structure. The number of companies can be different

| Name | Day | AM/PM | Company1 | Company2 |
| ------ | ------ | ----- | ------ | ------ |
| John Doe | Monday | AM | A inc | B inc |

The app adds new columns. Every new column is the meeting time (interval 20min)

| Name | Day | AM/PM | Company1 | Company2 | 8:00 a.m. | 8:20 a.m. | 8:40 a.m. |
| ------ | ------ | ----- | ------ | ------ | ------ | ------ | ------ |
| John Doe | Monday | AM | A inc | B inc |

The app fills every spot with the available companies. if there is a conflict (same meeting time), the app search for the next empty spot. if there are no empty spots for a company with a mentor (extreme case: for instance if many mentors chose the same day), the company will be list in an extra column called "unavailable spot". 
The output CSV file can be used as an input too. Also, it can be updated manually (for instance a mentor who had not decided the day, now he/she has decided).

| Name | Day | AM/PM | Company1 | Company2 | 8:00 a.m. | 8:20 a.m. | 8:40 a.m. |
| ------ | ------ | ----- | ------ | ------ | ------ | ------ | ------ |
| John Doe | Monday | AM | A inc | B inc | A inc | B inc |


## Autor
* [**Heimer Rojas**](https://github.com/HeimerR)

