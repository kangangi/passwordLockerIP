import unittest #importing the unittest module
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the User class behaviours
  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
    '''
    Set up method to run before each test cases
    '''
    self.new_user = User ("Diana", "24" )
  

  def test_init(self):
    '''
    test_init case to test whether tre object is being initialised properly
    '''

    self.assertEqual(self.new_user.login_username, "Diana")
    self.assertEqual(self.new_user.password,"24")


  def test_save_user(self):
    '''
    test_save_user test case to test if the contact object is saved into the system
    '''
    self.new_user.save_user() 
    self.assertEqual(len(User.users),1)

if __name__ == '__main__':
  unittest.main()