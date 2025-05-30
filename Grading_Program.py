student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for x in student_scores:
    if 91<=student_scores[x]<=100: student_grades[x]="Outstanding"
    elif 81<=student_scores[x]<=90: student_grades[x]="Exceeds Expectations"
    elif 71<=student_scores[x]<=80: student_grades[x]="Acceptable"
    elif 0<=student_scores[x]<=70: student_grades[x]="Fail"

    

#🚨 Don't change the code below 👇
print(student_grades)



#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

with open('testing_copy_2.py', 'w') as file:
  file.write('student_scores = {"Harry": 41, "Ron": 91, "Hermione": 89, "Draco": 69,"Neville": 71}\n\n')
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[8:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import testing_copy_2

import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def test_1(self): 
    with patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      expected_print = "{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_2(self): 
    with patch('sys.stdout', new=StringIO()) as fake_out:
      testing_copy_2.test_func()
      expected_print = "{'Harry': 'Fail', 'Ron': 'Outstanding', 'Hermione': 'Exceeds Expectations', 'Draco': 'Fail', 'Neville': 'Acceptable'}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 


print('\n\n\n.\n.\n.')
print('Checking if what you printed matches the target output for two different dictionaries...')
print('Running some tests on your code:')
print('.\n.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
os.remove('testing_copy_2.py') 
