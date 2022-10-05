# Pissoir-problem

This is a very naive (and therefore slow) implementation of the pissoir problem with maximum courtesy distance as presented in
the DorFuchs video "Das Pissoir-Problem" (https://www.youtube.com/watch?v=a36zHPlbd2g).

Prerequisites:

* Python 3.6+ (only tested in CPython 3.8 though)
* [matplotlib](https://pypi.org/project/matplotlib/)

The program calculates and plots the results of all pissoir problems up to a given n.

The program can be run from the command line like so: `<python> <path>\pissoir_problem.py <n> <print_progress>`.

Explanation of parameters:

* `<python>` - your Python version. Usually it's one those 3: `python`, `python3` or `py`.
* `<path>` - The path towards the script, relative to your current location
* `<n>` - describes the amount of pissoirs up to which you want to calculate
* `<print_progress>` - optional, i.e. you can just omit it. If you put anything here it'll print what step it's currently calculating (might be useful if you calculate larger `n`s, as the program is kinda slow and you might panic if you don't see any output for a prolonged period of time).

In case you omit all parameters or put anything that is not a number for `n`, the program will "manually" ask you for those inputs.

Example run on my computer:

    > python .\pissoir_problem.py 16 1
    Calculating n= 0... Took 0.00000s
    Calculating n= 1... Took 0.00000s
    Calculating n= 2... Took 0.00000s
    Calculating n= 3... Took 0.00000s
    Calculating n= 4... Took 0.00000s
    Calculating n= 5... Took 0.00000s
    Calculating n= 6... Took 0.00000s
    Calculating n= 7... Took 0.00100s
    Calculating n= 8... Took 0.00101s
    Calculating n= 9... Took 0.00300s
    Calculating n=10... Took 0.01404s
    Calculating n=11... Took 0.09077s
    Calculating n=12... Took 0.36844s
    Calculating n=13... Took 2.20706s
    Calculating n=14... Took 9.32787s
    Calculating n=15... Took 47.05341s
    Calculating n=16... Took 351.85369s
    
    --------------------------
    
    Solution for n= 0: 0
    Solution for n= 1: 1
    Solution for n= 2: 2
    Solution for n= 3: 4
    Solution for n= 4: 8
    Solution for n= 5: 20
    Solution for n= 6: 48
    Solution for n= 7: 216
    Solution for n= 8: 576
    Solution for n= 9: 1392
    Solution for n=10: 7200
    Solution for n=11: 43200
    Solution for n=12: 184320
    Solution for n=13: 1065600
    Solution for n=14: 4314240
    Solution for n=15: 21611520
    Solution for n=16: 150958080

![pissoir_problem_upto_16](https://user-images.githubusercontent.com/38440557/194154040-00befbf6-a07b-48a7-ae0f-1281261900ce.png)
