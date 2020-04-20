#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_user(login_username, password):
  '''
  Function to create new user
  '''
  new_user = User(login_username,password)
  return new_user

def create_credentials(account_name,account_username, account_password):
  '''
  Function to create new credential
  '''
  new_credential = Credentials(account_name,account_username, account_password)
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
  credential.save_credential()

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

def generate_pass():
  '''
  Function that generates random password
  '''
  return Credentials.generate_password()

def find_credential(name):
  '''
  Function that finds credentials using the name of the account
  '''
  return Credentials.find_by_name(name)

def credential_exist(name):
  '''
  Function to check that credential exist
  '''
  return Credentials.name_exist(name)

def main():

  print("PASSWORD LOCKER")
  print("--"*20)
  print("An application that saves your account Details")
  print("\n")
  print("What is your name?")
  user_name = input()
  print("\n")

  print(f"Hello {user_name}. Are you a new user or would you like to create an account")

  while True:
    print("Use these short codes:\n - nu - new user \n -li - log in \n -ex - exit the password locker")
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
      print("\n")

      authenticated_password = user_authenticate(login_username,password)
      if authenticated_password == password:
        print("You have successfully logged in")
        print("\n")
        print("What would you like to do?")

        while True:
          print("Use the following short codes: \n - cc - create new credentials \n - fc - find a specific credential/delete a credential, \n - dc - display all  your accounts \n - lo - log-out")
          credentials_short_code = input().lower()

          if credentials_short_code == 'cc':
            print("New Credentials")
            print("-"*20)
            print("Account Name(eg Twitter)...")
            account_name = input()
            print(f"What is your username for {account_name}")
            account_username = input()
            print("\n")
            print("Would you like a generated password? (y/n)?")
            gen_pass = input().lower()
            if gen_pass == 'y':
              account_password = generate_pass()
              print(f"Password generated is {account_password}")
              save_credentials(create_credentials(account_name,account_username,account_password))
            else:
              print("Enter the account password, (should be longer than 7 characters long)")
              account_password = input()
              
              if len(account_password) >= 7:
                save_credentials(create_credentials(account_name,account_username,account_password))
                print(f"Account details for {account_name} have been saved")
                print("\n")

              else:
                print("Password is too short. Try again")

          elif credentials_short_code == "dc":
            if display_credentials():
              print("Here is a list of all your accounts and there credentials")
              print('/n')
              for credential in display_credentials():
                print(f"{credential.account_name} ,username: {credential.account_username}, password:  {credential.account_password}")
                print("\n")
            else:
              print("You don't seem to have any credentials saved")
              print("\n")

          elif credentials_short_code == "fc":
            print("Enter the name of account you are looking for e.g Twitter...")
            searched_name = input()

            if credential_exist(searched_name):
              searched_credential = find_credential(searched_name)
              print(f"{searched_credential.account_name} , username: {searched_credential.account_username}, password: {searched_credential.account_password} ")

              print(f"Would you like to delete credentials for {searched_credential.account_name}? (y/n)")
              delete_credential = input().lower()

              if delete_credential == 'y':
                del_credential(searched_credential)
                print("Credentials have been deleted")
              else:
                print("Credentials have not been deleted")
            else:
              print("The credentials for that name do not exist")

          elif credentials_short_code == 'lo':
            print("You have successfully logged out..")
            break
          
          else:
            print("I really didn't get that. Please use the short codes")

      else:
       print("Invalid username and password,try again")

    elif authentication_short_code == 'ex':
      print("Bye....")
      break

    else:
      print("Invalid option, please use the short code")

if __name__ == '__main__':
  main()
      





    
  


