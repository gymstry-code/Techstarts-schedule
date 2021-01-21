# Techdule - Schedule Generator

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Techdule is a tool that helps the Program Associate and the Program Manager to  assign a specific time slot for each startup with their assigned mentors, in such a way that a mentor is not booked with two companies at the same time, nor a startup booked with more than one mentor at the same time.


# How to use it!

  - Go to the demo app:
  ![index_image](https://github.com/HeimerR/obj_detect/blob/main/imagenes_github/1.png)
  - Drag and drop the csv file
  - Download de new csv file thar contains the schedule
  ![index_image](https://github.com/HeimerR/obj_detect/blob/main/imagenes_github/1.png)


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

The app adds new columns. Every new column is the appointment time (interval 20min)

| Name | Day | AM/PM | Company1 | Company2 | 8:00 a.m. | 8:20 a.m. | 8:40 a.m. |
| ------ | ------ | ----- | ------ | ------ | ------ | ------ | ------ |
| John Doe | Monday | AM | A inc | B inc |

The app fills every spot with a list created with the companies availables. if there is a conflict (same time), the app search for the next empty spot.

| Name | Day | AM/PM | Company1 | Company2 | 8:00 a.m. | 8:20 a.m. | 8:40 a.m. |
| ------ | ------ | ----- | ------ | ------ | ------ | ------ | ------ |
| John Doe | Monday | AM | A inc | B inc | A inc | B inc |


## Autor
* [**Heimer Rojas**](https://github.com/HeimerR)

