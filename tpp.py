#!/usr/bin/python
#
# TaskPaper Parser
# K. Marchand 2014
#

from datetime import datetime, timedelta
from collections import namedtuple
from dateutil import parser
import sys
import re

tpfile = sys.argv[1]

with open(tpfile, 'rb') as f:
    tplines = f.readlines()

Flagged = namedtuple('Flagged', ['type', 'taskdate', 'project', 'task'])
flaglist = []
errlist = []

project = ''

for line in tplines:
    try:
        if '@done' in line:
            continue
        if ':\n' in line:
            project = line.strip()[:-1]
        if '@due' in line:
            duetag = re.search('\@due\((.*?)\)', line).group(1)
            taskdate = parser.parse(duetag)
            flaglist.append(
                Flagged('due', taskdate, project, line.strip()))
        if '@start' in line:
            starttag = re.search('\@start\((.*?)\)', line).group(1)
            taskdate = parser.parse(starttag)
            flaglist.append(
                Flagged('start', taskdate, project, line.strip()))
        if '@today' in line:
            flaglist.append(
                Flagged('today', datetime.now(), project, line.strip()))
    except Exception, e:
        errlist.append((line, e))

today = overdue = duethisweek = startthisweek = None

print 'SUMMARY for %s [%s]' % (tpfile, str(datetime.now())[:16])

print '\nTODAY\n'

for task in flaglist:
    if task.type == 'today':
        today = True
        print '\t[%s] %s' % (task.project, task.task)
if not today:
    print '\t (none)'

print '\nOVERDUE\n'

for task in flaglist:
    if task.type == 'due' and datetime.now() > task.taskdate:
        overdue = True
        print '\t[%s] %s' % (task.project, task.task)
if not overdue:
    print '\t (none)'

print '\nDUE THIS WEEK\n'

for task in flaglist:
    weeklater = datetime.now() + timedelta(days=7)
    if task.type == 'due' and datetime.now() < task.taskdate < weeklater:
        duethisweek = True
        print '\t[%s] %s' % (task.project, task.task)
if not duethisweek:
    print '\t (none)'

print '\nSTARTING THIS WEEK\n'

for task in flaglist:
    weeklater = datetime.now() + timedelta(days=7)
    if task.type == 'start' and datetime.now() < task.taskdate < weeklater:
        startthisweek = True
        print '\t[%s] %s' % (task.project, task.task)
if not startthisweek:
    print '\t (none)'

if len(errlist) != 0:
    print '\nERROR PARSING THESE LINES\n'
    for errtask in errlist:
        print '\t%s' % str(errtask)

print '\n'
