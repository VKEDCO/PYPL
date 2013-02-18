#!/usr/bin/python

########################################################################################
# solution to the student records problem
# at http://www.vkedco.blogspot.com/2013/02/python-perl-square-bottom-line-relief.html
# bugs to vladimir dot kulyukin at gmail dot com
########################################################################################

import re
student_records = {
    0: 'J.P.;GPA=3.5;A1927;11/01/91',
    1: 'GPA=4.0;N.K.;12/01/90;A2732',
    2: 'A9803;GPA=3.25;M.D.;10/03/87',
    3: '05/01/89;A1248;GPA=2.87;D.W.',
    4: 'GPA=3.87;L.M.;03/17/89;A6752'    
    }

initials_regex = r'([A-Z]\.[A-Z]\.)'
gpa_regex = r'GPA=(\d\.\d{1,3})'
anum_regex = r'(A\d{4})'
date_regex = r'(\d{2}\/\d{2}\/\d{2})'

def process_student_record_line(line):
    student_record = {}
    m = None
    for s in line.split(';'):
        m = re.search(initials_regex, s)
        if m != None:
            student_record['Initials'] = m.group()
            continue
        m = re.search(gpa_regex, s)
        if m != None:
            student_record['GPA'] = m.group()
            continue
        m = re.search(anum_regex, s)
        if m != None:
            student_record['ANUM'] = m.group()
            continue
        m = re.search(date_regex, s)
        if m != None:
            student_record['BirthDate'] = m.group()
            continue
    return student_record

print
print process_student_record_line('J.P.;GPA=3.5;A1927;11/01/91')
print 

def build_student_record_table(student_record_lines):
    student_table = {}
    for (rec_num, line) in student_record_lines.iteritems():
        student_rec = process_student_record_line(line)
        student_table[student_rec['ANUM']] = student_rec
    return student_table

tab =  build_student_record_table(student_records)
## print tab

def display_student_record_table(student_record_table):
    for (anum, student_record) in student_record_table.iteritems():
        for (key, val) in student_record.iteritems():
            print str(key) + ' --> ' + str(val) 
        print

display_student_record_table(tab)

