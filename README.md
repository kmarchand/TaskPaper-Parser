# TaskPaper Parser

Script to parse a [TaskPaper](http://www.hogbaysoftware.com/products/taskpaper) formatted file and print a summary of current, overdue and upcoming actions.

The current use is with something like [GeekTool](http://projects.tynsoe.org/en/geektool/) for listing the summary on the desktop, but it may be worked into an Alfred2 Workflow in the future.

## Usage

`python tpp.py <input file>`

The `<input file>` will be parsed for tasks containing the @today, @due(<date>), @start(<date>) tags.  Tasks with the @done tag are ignored.

The output will show the relevant tasks found in four sections.

Ex;

```
SUMMARY for <filename> [<date>]

TODAY
    
    [Project1] - Task 1 @today
    [Project1] - Task 2 @today
    [Project2] - Task 1 @today

OVERDUE

    [Project1] - Task 1 @due(<any date in the past>)
    [Project3] - Task 1 @due(<any date in the past>)

DUE THIS WEEK

    [Project3] - Task 2 @due(<any date in the next week>)
    [Project4] - Task 3 @due(<any date in the next week>)

STARTING THIS WEEK

    [Project1] - Task 4 @start(<any date in the next week>)
    [Project2] - Task 3 @start(<any date in the next week>)
```

If an error comes up for parsing any line in the file, it will be show at the bottom as:

```
ERROR PARSING THESE LINES
    (line text, error)
    (line text, error)
```

## Changes

* February 2 2014; Inital version.