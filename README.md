# Task
The task is to find unknown mathematical formula y=f(x), which is hidden in a black-box machine. You can measure data
by the following request:

`/api/do_measurement?x=4`

You get a response in JSON like this:

`{"data": {"y": 188.58938971580736, "x": 4.0}}`

The full text of the task is here https://github.com/kiwicom/mlweekend

# Solution

The solution is written in Python 3 (tested on 3.5.4).

## Get data

get_data.py can be used to do a series of measurements on a given interval, with a given step and a number of
repetitions, e.g.

`python get_data.py -1 1.1 0.1 5`

performs measurements on the interval <-1.0,1.0>, with step 0.1, and with 5 repetitions for every x value. The data are
saved into txt file. Type `-h` for help.

There are 4 testing datasets obtained by the script in this repository:
- data0.txt - interval <-1.0,1.0>, step 0.1, rep 5
- data1.txt - interval <-5.0,5.0>, step 0.5, rep 5
- data2.txt - interval <-10,10>, step 1, rep 5
- data3.txt - interval <-100,100>, step 10, rep 5
