from random import randint

class Credentials:
  '''
  Class that generates new instances of credentials
  '''
  credentials_list = []
  def __init__(self,account_name,account_username, account_password):
    '''
    __init method that helps us define properties for our objects.
    Args:
      account_name: New account name
      password: new account password
    '''
    self.account_name = account_name
    self.account_username = account_username
    self.account_password = account_password
  
  def save_credential(self):
    '''
    save_credential method that saves objects into contact_list
    '''
    Credentials.credentials_list.append(self)

  def delete_credential(self):
    '''
    delete_credential method that deletes a saved credential from the credential list
    '''
    Credentials.credentials_list.remove(self)

  @classmethod
  def display_credential(cls):
    '''
    method that returns a list of all credentials
    '''
    return cls.credentials_list

  @classmethod
  def generate_password(cls):
    '''
    method that generates a random password for the user
    '''
    mylist  = ["a","b","c","d","e","f", "g", "h", "i", "j","k","l", "m","n","o","p","q","r","s","t", "u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    random_pass = ""
    length = 0
    while (length < 7):
      random_character = mylist[randint(0,len(mylist) -1)]
      random_pass += random_character
      length += 1
    return random_pass


