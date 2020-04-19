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



