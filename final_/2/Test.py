"""
Student Registered Successfully in Information Technology IT
Student Registered Successfully in Information Technology IT
Student Registered Successfully in Mathematics M
Student Registered Successfully in Mathematics M
Information Technology (IT) with (2 out of 3)
Sharaf Awad Qeshta
ID: 120220000
John Edward Smith
ID: 120220001
Mathematics (M) with (2 out of 3)
noor khalid bolbol
ID: 220220002
Sharaf Awad Qeshta
ID: 120220003
"""

from college import College
from student import Student

it = College("Information Technology", 3)
math = College("Mathematics", 3)

s1 = Student("Sharaf", "Awad", "Qeshta", "13:06:2001", 1, "464646546464", "333-333-4444")
s2 = Student("John", "Edward", "Smith", "08:09:2002", 1, "464646546464", "333-333-4444")

s3 = Student("noor", "khalid", "bolbol", "21:07:2000", 2, "464646546464", "333-333-4444")
s4 = Student("Sharaf", "Awad", "Qeshta", "12:08:1999", 1, "464646546464", "333-333-4444")

s1.set_college(it)
s2.set_college(it)

s3.set_college(math)
s4.set_college(math)

it.get_info()
math.get_info()
