import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
  '''
  Test class that defines test cases for contact class behaviours
  Args:
    unittest.TestCase: TestCase class that  helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases
    '''
    self.new_credential = Credentials("Twitter", "100")

  def test_init(self):
    '''
    Test init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_credential.account_name, "Twitter")
    self.assertEqual(self.new_credential.account_password, "100")

if __name__ == '__main__':
  unittest.main()