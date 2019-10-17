## Unit Testing Assignment

by Chatchapong Chumpada.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| repetitive item        |  list with unique item|
| not a list             |  throw exception |
| repetitive list in list | unique item and list in list|


## Test Cases for Fraction

| Test case              |  Expected Result    |
|------------------------|---------------------|
| print fraction             |  print fraction in proper form |
| negative number on both numerator and denominator| positive proper form |
| negative number either numerator or denominator | negative proper form|
| not __int__ input     |throw exception|
| sum of two fraction|result of sum fraction in proper form |
| equle of two fraction|true if both are equle,false if neither equal|
| multiply | result of multiply fraction|
