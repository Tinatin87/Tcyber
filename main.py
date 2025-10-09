
from checker import check_password
from utils import strength_message
from common import common_passwords

def main():
   password = input("Enter Your Password: ")
   score, level = check_password(password)
   print(f"Password strength score: {score}")
   print(f"Password strength level: {level}")
