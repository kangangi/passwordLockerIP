class Credentials:
  '''
  Class that generates new instances of credentials
  '''
  credentials_list = []
  def __init__(self,account_name, account_password):
    '''
    __init method that helps us define properties for our objects.
    Args:
      account_name: New account name
      password: new account password
    '''
    self.account_name = account_name
    self.account_password = account_password
  
  def save_credential(self):
    '''
    save_credential method that saves objects into contact_list
    '''
    Credentials.credentials_list.append(self)

