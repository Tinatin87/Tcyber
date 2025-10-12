# ქულის ტექსტად გარდაქმნა

def strength_message(score: int) -> str:
    if score <= 3:
        return "პაროლი სუსტია "
    elif score <= 6:
        return "პაროლი საშუალოა "
    elif score <= 9:
        return "პაროლი საკმაოდ კარგია "
    else:
        return "პაროლი ძალიან ძლიერია "