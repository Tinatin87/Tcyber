
from checker import check_password
from utils import strength_message


def main():
   password = input("Enter Your Password: ")
   score = check_password(password)
   level = strength_message(score)

   print(f"Password strength score: {score}")
   print(f"Password strength level: {level}")

if __name__=="__main__":
     main()