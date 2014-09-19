# csv-dd
======

a little csv parser and de-duper

## Usage: 
======

`python csv-dd input.csv output.csv`

## Input:
========

* should be two columns csv format
* split by ','

Example:
```
20,Glen
30,Jesse
10,Sean
40,Sean
50,Jesse
60,Jesse
50,Glen
40,Jesse
40,Jesse
50,Glen
```
**Note: records can possibly duplicate**

## Output should:
=======
* output similar csv format
* populate left column with only unique number id's
* populate right column with associated values (names) separated by ; and not duplicate
* columns should still split by ','

Example:
```
10,Sean
20,Glen
30,Jesse
50,Jesse;Glen
40,Sean;Jesse
60,Jesse
```
