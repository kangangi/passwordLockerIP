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

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run
    '''
    Credentials.credentials_list = []

    
  def test_save_credential(self):
    '''
    test_save_credentials test case to test if the credentials into the credentials list
    '''
    self.new_credential.save_credential()
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_save_multiple_credential(self):
    '''
    test_save_multiple_credentials to check if we can save multiple credential objects to our credentials list
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("Test", "500")
    test_credential.save_credential()
    self.assertEqual(len(Credentials.credentials_list),2)

if __name__ == '__main__':
  unittest.main()