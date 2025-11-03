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
       return score

# სიგრძის მიხედვით ქულები
    if length >= 20:
       score += 5
    elif length >= 16:
       score += 3
    elif length>= 12:
       score += 2
    elif length >= 8:
       score += 1
    else :
      print("Password length is too short. Your password strength is 0")
      return score

# სიმპოლოების მიხედვით ქულები
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
       score += 5
    if re.search(r"[0-9]", password):
       score += 2
    if re.search(r"[A-Z]", password):
      score += 2
    if re.search(r"[a-z]", password):
      score += 1
    return score

