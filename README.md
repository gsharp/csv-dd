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
Glen,20
Jesse,30
Sean,10
Sean,40
Jesse,50
Jesse,60
Glen,50
Jesse,40
Jesse,40
Glen,50
```
**Note: records can possibly duplicate**

## Output should:
=======
* output similar csv format
* populate right column with only unique id's
* populate left column with associated values (names) separated by ; and not duplicate
* columns should still split by ','

Example:
```
Sean,10
Glen,20
Jesse,30
Jesse;Glen,50
Sean;Jesse,40
Jesse,60
```
