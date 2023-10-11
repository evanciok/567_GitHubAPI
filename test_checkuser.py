from datetime import datetime
def my_brand(assignment):
  datetime_obj = datetime.now()
  datetime_string = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")
  print("=*=*=*= Evan Ciok =*=*=*=")
  print("=*=*=*= 2023F SSW 567-A =*=*=*=")
  print("=*=*=*= " + assignment + " =*=*=*=")
  print("=*=*=*= " + datetime_string + " =*=*=*=")
assignment_name = "HW04A - Develop With The Perspective Of The Tester In Mind"

import unittest
from checkuser import getInfo, getCommit

class test_checkuser(unittest.TestCase):
    def testInvalidUser(self): 
        self.assertEqual(getInfo("evancoik"),'request error 404')

    def testValidUser(self): 
        self.assertEqual(getInfo("evanciok"), ['567_GitHubAPI has 19 commits', 'cs555tm012023fall has 11 commits', 'Singleton-Visitor has 3 commits', 'SSW-567 has 3 commits', 'SSW567HW02 has 12 commits'])

    def testInvalidRepo(self): 
        self.assertEqual(getCommit("evanciok", "repo1"),'request error 404')
    
    def testValidRepo(self): 
        self.assertEqual(getCommit("evanciok", "cs555tm012023fall"), 11)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()