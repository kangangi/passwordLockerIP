class User:
  '''
  Class that generates new instances of users
  '''
  def __init__(self, login_username, password):
    '''
    ___init___ method that helps us define properties for our objects.
    Args: 
      name: New user name
      password: New user password
    '''
    self.login_username = login_username
    self.password = password

  
  
  