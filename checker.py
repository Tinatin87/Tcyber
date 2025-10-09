import re

def check_password(password: str) -> int:
    score = 0
    length = len(password)
# პაროლების სიიდან წაკითხვა
    with open('common.txt', 'r') as f:
         common_passwords = f.read().split()
# როცა პაროლი ცნობილია
    if password in common_passwords:
       print("Password is in a common list. Your password strength is 0")
       exit()  

# სიგრძის მიხედვით ქულები
    if length >= 8:
       score += 1
    if length >= 12:
       score += 1
    if length>= 16:
       score += 1
    if length >= 20:
       score += 1

# სიმპოლოების მიხედვით ქულები
    if re.search(r"[a-z]", password):
      score += 1
    if re.search(r"[A-Z]", password):
      score += 2
    if re.search(r"[0-9]", password):
       score += 2
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
       score += 5
    return score

