import random

def generate_number():
    return random.randint(1, 100)

def check_guess(secret, guess):
    if guess>secret:
        return "high"
    elif guess<secret:
        return "low"
    else:
        return "correct"
    
if __name__ == "__main__":
    print(generate_number())