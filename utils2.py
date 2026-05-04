import random

def generate_number():
    return random.randint(1, 100)

def check_guess(secret, guess):
    if guess>secret:
        return "Tevis izvēlētais skaitlis ir par lielu!"
    elif guess<secret:
        return "Tevis izvēlētais skaitlis ir par mazu!"
    else:
        return "Apsveicu! Tu uzminēji skaitli!"