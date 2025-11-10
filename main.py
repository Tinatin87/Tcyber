
from checker import check_password
from utils import strength_message

def main():
    while True:
        password = input("Enter Your Password (or type 'quit' to exit): ").strip()
        
        # თუ მომხმარებელი ჩაწერს quit ან exit → დატოვებს ციკლს
        if password.lower() in ("quit", "exit"):
            print("Goodbye!")
            print("Stay safe online!")
            break

        score = check_password(password)
        level = strength_message(score)

        print(f"Password strength score: {score}")
        print(f"Password strength level: {level}\n")

if __name__ == "__main__":
    main()