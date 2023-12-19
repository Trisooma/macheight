### app.py

run on command line using:
> ./app.py <integer_list> <sum>

### Run and check normal and edge cases
#### Basic Input:
> ./app.py 1,2,3,4,5,6 8
#### No Pairs:
> ./app.py 1,2,3,4,5,6 20
#### Negative Numbers:
> ./app.py -1,-2,3,4,-5,6 2
#### Duplicate Pairs:
> ./app.py 3,4,3,5,6,1 6
#### Zero as a Target:
> ./app.py -2,0,2 0
#### Invalid Input (Non-integer in the list):
> ./app.py 1,2,a,4,5,6 8
#### Invalid Input (Incorrect Number of Arguments):
> ./app.py 1,2,3,4,5,6
#### Large List:
> ./app.py $(seq -s, 1 1000000) 2000000