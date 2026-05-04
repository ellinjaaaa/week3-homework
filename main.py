from utils2 import generate_number, check_guess
from validators2 import is_valid_guess

def run_game():
    secret=generate_number()
    number_of_guesses=0
    player_win=False

    print("Tev ir 10 mēģinājumi, lai uzminētu skaitli!")

    while number_of_guesses<10:
        text=input("Izvēlies skaitli no 1 līz 100:")

        if not is_valid_guess(text):
            print("Nederīga ievade.")
            continue
            
        guess=int(text)
        number_of_guesses+=1

        print(f"Šis bija Tavs {number_of_guesses}. minējums.")

        result=check_guess(secret, guess)

        if result=="high":
            print("Tevis izvēlētais skaitlis ir par lielu!")
        elif result=="low":
            print("Tevis izvēlētais skaitlis ir par mazu!")
        else:
            print("Apsveicu! Tu uzminēji skaitli!")
            player_win=True
            break
    
    if not player_win:
        print(f"Pareizais skaitlis: {secret}.")

if __name__=="__main__":
    run_game() 