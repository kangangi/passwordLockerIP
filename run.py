#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_user(login_username, password):
  '''
  Function to create new user
  '''
  new_user = User(login_username,password)
  return new_user

def create_credentials(account_name, account_password):
  '''
  Function to create new credential
  '''
  new_credential = Credentials(account_name, account_password)
  return new_credential

def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()

def user_authenticate(name,password):
  ''' 
  Function to authenticate user
  '''
  return User.authenticate_user(name,password)

def save_credentials(credential):
  '''
  Function to save credential
  '''
  credential.save_credentials()

def del_credential(credential):
  '''
  Function to delete credential
  '''
  credential.delete_credential()

def display_credentials():
  '''
  Function that returns all saved credentials
  '''
  return Credentials.display_credential()

def main():
  print("Heyyy! Welcome to Password Locker")
  print("We can save your passwords for you")
  print("What is your name?")
  user_name = input()

  print(f"Hello {user_name}. Are you a new user or would you like to create an account")
  while True:
    print("Use these short code: nu - new user, li - log in")
    authentication_short_code = input().lower()
    if authentication_short_code =='nu':
      print("New account")
      print("-"*20)
      print("Username")
      login_username = input()
      print("Password")
      password = input()

      save_user(create_user(login_username,password))
      print('\n')
      print(f"Account for {login_username} created. Proceed to log in")
      print('\n')

    elif authentication_short_code == 'li':
      print("Enter your user name")
      login_username = input()
      print("Enter your password")
      password = input()

      authenticated_password = user_authenticate(login_username,password)
      if authenticated_password == password:
        print("You have successfully logged in")
      else:
       print("Invalid username and password try again")

    else:
      print("Invalid option, please use the short code")

if __name__ == '__main__':
  main()
      





    
  


